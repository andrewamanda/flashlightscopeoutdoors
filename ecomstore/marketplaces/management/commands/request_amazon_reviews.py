# ecomstore/marketplaces/management/commands/request_amazon_reviews.py

from typing import Optional, Iterable, List
from datetime import datetime, timedelta, timezone
from collections import Counter
import io
import csv
import json

from django.core.management.base import BaseCommand
from django.utils.timezone import now as dj_now
from django.core.mail import EmailMultiAlternatives

from ecomstore.marketplaces.models import AmazonOrder_Excluded
from ecomstore.settings import (
    AMZN_SP_REFRESH_TOKEN,
    AMZN_SP_LWA_APP_ID,
    AMZN_SP_LWA_CLIENT_SECRET,
    ADMINS,
    DEFAULT_FROM_EMAIL,
)

# SP-API SDK
from sp_api.api import Orders, Solicitations
from sp_api.base import Marketplaces, SellingApiException

# Local rate limiter
from ecomstore.marketplaces.management.commands.spapi_rate import call_with_rate_limit


MARKETPLACE = Marketplaces.US
MP_ID = MARKETPLACE.marketplace_id


def _preview(items: Iterable[str], limit: int) -> str:
    items = list(items)
    if limit <= 0 or len(items) <= limit:
        return ", ".join(map(str, items)) if items else "(none)"
    return ", ".join(map(str, items[:limit])) + f" … (+{len(items) - limit} more)"


def _csv_bytes(header: List[str], rows: Iterable[List[str]]) -> bytes:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(header)
    for r in rows:
        w.writerow(r)
    return buf.getvalue().encode("utf-8")


def _get_error_details(e: Exception) -> tuple:
    """Safely extract error details from SP-API exceptions"""
    code = getattr(e, 'code', None) or type(e).__name__
    try:
        response = getattr(e, 'response', {})
        body_text = response.get('text', '') if hasattr(response, 'get') else str(response)
    except Exception:
        body_text = str(e)
    return code, body_text


def _explain_error_code(code: str, body: str) -> str:
    """Translate Amazon error codes to human-readable explanations"""
    explanations = {
        'ResourceNotFound': 'Order not eligible (already requested, outside time window, or not delivered)',
        'InvalidInput': 'Invalid order ID or wrong marketplace',
        'QuotaExceeded': 'Daily request limit reached',
        'AccessDenied': 'API permission issues - check credentials',
        'InternalError': 'Amazon API internal error - try again later',
    }

    # Try to extract more details from the body
    detail = ""
    try:
        error_data = json.loads(body)
        if 'errors' in error_data and len(error_data['errors']) > 0:
            detail = f" - {error_data['errors'][0].get('message', '')}"
    except:
        pass

    return explanations.get(code, f"Unknown error: {code}") + detail


class Command(BaseCommand):
    help = (
        "Send Amazon 'Request a Review' solicitations for shipped orders, "
        "skipping orders in AmazonOrder_Excluded. Let Amazon API handle eligibility checks."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--created-after",
            default=(dj_now() - timedelta(days=45))
            .astimezone(timezone.utc)
            .strftime("%Y-%m-%dT00:00:00Z"),
            help="ISO8601 timestamp to start pulling orders from (default: ~45 days back).",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="List which orders WOULD be sent, but do not call Amazon.",
        )
        parser.add_argument(
            "--channel",
            choices=["all", "fba", "fbm"],
            default="all",
            help="Restrict processing to FBA (AFN), FBM (MFN), or all (default).",
        )
        parser.add_argument(
            "--max-ids",
            type=int,
            default=50,
            help="Max IDs to show inline in the email for each list (full CSVs attached).",
        )
        parser.add_argument(
            "--statuses",
            nargs="+",
            default=["Shipped", "PartiallyShipped"],
            help="OrderStatuses to query (default: Shipped, PartiallyShipped).",
        )
        parser.add_argument(
            "--order-id",
            dest="order_ids",
            action="append",
            help="Process a specific Amazon order id (repeatable or comma-separated). "
                 "Example: --order-id 113-... --order-id 123-...,456-...",
        )

    def handle(self, *args, **opts):
        created_after = opts["created_after"]
        dry_run = opts["dry_run"]
        channel_filter = opts["channel"]
        max_ids = max(0, int(opts["max_ids"]))
        statuses = opts["statuses"]

        # Exclusion set
        excluded_ids = set(
            AmazonOrder_Excluded.objects.values_list("order_id", flat=True)
        )
        self.stdout.write(self.style.NOTICE(f"Loaded {len(excluded_ids)} excluded order IDs."))

        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        orders_api = Orders(credentials=credentials, marketplace=MARKETPLACE)
        sol_api = Solicitations(credentials=credentials, marketplace=MARKETPLACE)

        # Per-channel buckets
        channel_sent = {"AFN": [], "MFN": []}
        channel_skipped = {"AFN": [], "MFN": []}
        channel_unknown = []

        # Track API rejection reasons
        raw_skip_reasons = []

        # ---------- Per-order processing helper ----------
        def process_one_order(od: dict):
            order_id = od.get("AmazonOrderId")
            channel = od.get("FulfillmentChannel")

            if not order_id:
                channel_unknown.append(("UNKNOWN", "missing_order_id"))
                return

            if channel not in ("AFN", "MFN"):
                channel_unknown.append((order_id, "unknown_channel"))
                return

            # Optional channel filter
            if channel_filter == "fba" and channel != "AFN":
                return
            if channel_filter == "fbm" and channel != "MFN":
                return

            # Exclusion list
            if order_id in excluded_ids:
                channel_skipped[channel].append((order_id, "excluded_by_us"))
                return

            # SKIP ALL ELIGIBILITY CHECKS - just try to send (or dry-run)
            if dry_run:
                channel_sent[channel].append(f"{order_id} (dry-run)")
                return

            try:
                call_with_rate_limit(
                    sol_api.create_product_review_and_seller_feedback_solicitation,
                    amazonOrderId=order_id,
                    marketplaceIds=[MP_ID],
                    min_interval=1.1,
                )
                channel_sent[channel].append(order_id)
            except SellingApiException as e:
                code, body_text = _get_error_details(e)
                reason = f"amazon_rejected:{code}"
                channel_skipped[channel].append((order_id, reason))
                raw_skip_reasons.append((order_id, code, body_text))

        # ---------- If --order-id provided, process only those ----------
        raw_ids = opts.get("order_ids")
        total_pages = 0

        if raw_ids:
            wanted: List[str] = []
            for chunk in raw_ids:
                wanted.extend([x.strip() for x in chunk.split(",") if x.strip()])
            # de-dupe while preserving order
            seen = set()
            deduped = []
            for w in wanted:
                if w not in seen:
                    seen.add(w)
                    deduped.append(w)
            wanted = deduped

            for oid in wanted:
                try:
                    res = call_with_rate_limit(
                        orders_api.get_order,
                        order_id=oid,
                        min_interval=2.0,
                    )
                    payload = res.payload or {}
                    if isinstance(payload, dict) and "Orders" in payload and payload["Orders"]:
                        od = payload["Orders"][0]
                    else:
                        od = payload

                    if not od or not od.get("AmazonOrderId"):
                        channel_unknown.append((oid, "get_order_empty_payload"))
                        continue

                    process_one_order(od)
                except SellingApiException as e:
                    code, body_text = _get_error_details(e)
                    channel_unknown.append((oid, f"get_order_error:{code}"))
        else:
            # ---------- Paginated fetch ----------
            token = None
            while True:
                total_pages += 1
                resp = call_with_rate_limit(
                    orders_api.get_orders,
                    CreatedAfter=created_after,
                    OrderStatuses=statuses,
                    NextToken=token,
                    min_interval=2.0,
                ).payload

                for od in resp.get("Orders", []):
                    process_one_order(od)

                token = resp.get("NextToken")
                if not token:
                    break

        # ------- Summaries -------
        def summarize_skips(sl):
            return Counter(r for _, r in sl)

        afn_skips = summarize_skips(channel_skipped["AFN"])
        mfn_skips = summarize_skips(channel_skipped["MFN"])
        unk_reasons = Counter(r for _, r in channel_unknown)

        # ---------- Build email text ----------
        admin_emails = [v for _, v in ADMINS]

        text_lines = []
        text_lines.append("Amazon Review Solicitation Report")
        text_lines.append(f"Pages scanned: {total_pages}")
        text_lines.append("")

        # AFN
        text_lines.append(f"FBA (AFN) sent: {len(channel_sent['AFN'])}")
        text_lines.append(f"FBA (AFN) skipped: {len(channel_skipped['AFN'])}  Reasons: {dict(afn_skips)}")
        text_lines.append(f"  Sent IDs (preview): {_preview(channel_sent['AFN'], max_ids)}")
        text_lines.append("")

        # MFN
        text_lines.append(f"FBM (MFN) sent: {len(channel_sent['MFN'])}")
        text_lines.append(f"FBM (MFN) skipped: {len(channel_skipped['MFN'])}  Reasons: {dict(mfn_skips)}")
        text_lines.append(f"  Sent IDs (preview): {_preview(channel_sent['MFN'], max_ids)}")

        if channel_unknown:
            text_lines.append("")
            text_lines.append(f"UNKNOWN channel skipped: {len(channel_unknown)}  Reasons: {dict(unk_reasons)}")

        if raw_skip_reasons:
            text_lines.append("")
            text_lines.append("Amazon API rejection explanations (first 15):")
            for oid, code, body in raw_skip_reasons[:15]:
                explanation = _explain_error_code(code, body)
                text_lines.append(f"  {oid}: {explanation}")

            text_lines.append("")
            text_lines.append("Raw API responses (first 10):")
            for oid, code, body in raw_skip_reasons[:10]:
                body_short = (body or "").strip().replace("\n", " ")
                if len(body_short) > 400:
                    body_short = body_short[:400] + " …"
                text_lines.append(f"  {oid}: code={code}  body={body_short}")

        text_body = "\n".join(text_lines)

        # ---------- Build email HTML ----------
        def html_ul_preview(items, limit):
            items = list(items)
            if not items:
                return "<p>(none)</p>"
            if limit <= 0 or len(items) <= limit:
                return "<ul>" + "".join(f"<li>{str(i)}</li>" for i in items) + "</ul>"
            return (
                "<ul>"
                + "".join(f"<li>{str(i)}</li>" for i in items[:limit])
                + f"<li><i>… (+{len(items) - limit} more in CSV)</i></li>"
                + "</ul>"
            )

        html_parts = []
        html_parts.append("<h2>Amazon Review Solicitation Report</h2>")
        html_parts.append(f"<p>Pages scanned: <b>{total_pages}</b></p>")

        # AFN
        html_parts.append("<h3>FBA (AFN)</h3>")
        html_parts.append(f"<p>Sent: <b>{len(channel_sent['AFN'])}</b> &nbsp; Skipped: <b>{len(channel_skipped['AFN'])}</b></p>")
        html_parts.append(f"<p>Reasons: {dict(afn_skips)}</p>")
        html_parts.append("<p>Sent IDs (preview):</p>")
        html_parts.append(html_ul_preview(channel_sent["AFN"], max_ids))

        # MFN
        html_parts.append("<h3>FBM (MFN)</h3>")
        html_parts.append(f"<p>Sent: <b>{len(channel_sent['MFN'])}</b> &nbsp; Skipped: <b>{len(channel_skipped['MFN'])}</b></p>")
        html_parts.append(f"<p>Reasons: {dict(mfn_skips)}</p>")
        html_parts.append("<p>Sent IDs (preview):</p>")
        html_parts.append(html_ul_preview(channel_sent["MFN"], max_ids))

        if channel_unknown:
            html_parts.append("<h3>UNKNOWN Channel</h3>")
            html_parts.append(f"<p>Skipped: <b>{len(channel_unknown)}</b> &nbsp; Reasons: {dict(unk_reasons)}</p>")

        if raw_skip_reasons:
            html_parts.append("<h3>Amazon API Rejection Explanations (first 15)</h3>")
            html_parts.append("<ul>" + "".join(
                f"<li><b>{oid}</b>: {_explain_error_code(code, body)}</li>"
                for oid, code, body in raw_skip_reasons[:15]
            ) + "</ul>")

            html_parts.append("<h3>Raw API Responses (first 10)</h3>")
            html_parts.append("<ul>" + "".join(
                f"<li><b>{oid}</b>: code={code} &nbsp; body={ (body or '').strip()[:400].replace(chr(10),' ') + (' …' if body and len(body.strip())>400 else '') }</li>"
                for oid, code, body in raw_skip_reasons[:10]
            ) + "</ul>")

        html_body = "\n".join(html_parts)

        # ---------- CSV attachments ----------
        attachments = []

        def add_csv(name: str, header: List[str], rows: Iterable[List[str]]):
            data = _csv_bytes(header, rows)
            attachments.append((name, data, "text/csv"))

        if channel_sent["AFN"]:
            add_csv("sent_ids_afn.csv", ["amazon_order_id"], [[oid] for oid in channel_sent["AFN"]])
        if channel_sent["MFN"]:
            add_csv("sent_ids_mfn.csv", ["amazon_order_id"], [[oid] for oid in channel_sent["MFN"]])

        # ---------- Send email ----------
        admin_emails = [v for _, v in ADMINS]
        email = EmailMultiAlternatives(
            subject="Amazon Review Solicitation Status",
            body=text_body,
            from_email=DEFAULT_FROM_EMAIL,
            to=admin_emails,
            headers={"X-Auto-Generated": "request_amazon_reviews"},
        )
        email.attach_alternative(html_body, "text/html")
        for name, data, mimetype in attachments:
            email.attach(name, data, mimetype)
        email.send(fail_silently=False)

        self.stdout.write(
            self.style.SUCCESS(
                f"Complete! Sent: AFN={len(channel_sent['AFN'])}, MFN={len(channel_sent['MFN'])}. "
                f"Email sent to {len(admin_emails)} recipients."
            )
        )
