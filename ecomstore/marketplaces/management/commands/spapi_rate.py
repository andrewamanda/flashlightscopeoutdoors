# marketplaces/spapi_rate.py
import time
import random
from typing import Callable, Any, Optional, Tuple, Dict

from sp_api.base.exceptions import SellingApiRequestThrottledException, SellingApiException

# Default Solicitations limits (adjust per operation if you know exact limits)
# Many solicitations endpoints are ~1 req/sec (burst 5). We stay at 1.1s spacing by default.
DEFAULT_MIN_INTERVAL = 1.1  # seconds between calls

def _read_reset_from_headers(exc: SellingApiException) -> Optional[float]:
    """
    Try to read rate-limit reset info from Amazon headers if present.
    Returns seconds to wait or None.
    """
    hdrs = getattr(exc, 'response', None)
    if not hdrs:
        return None
    try:
        # Some SDK versions expose headers on exc.response.headers
        headers = getattr(hdrs, 'headers', {}) or {}
        reset = headers.get('x-amzn-RateLimit-Reset')
        if reset is None:
            return None
        # It can be seconds or a timestamp fraction; treat as seconds float if possible
        return float(reset)
    except Exception:
        return None


def call_with_rate_limit(
    fn: Callable,
    /,
    *args: Any,
    min_interval: float = DEFAULT_MIN_INTERVAL,
    max_retries: int = 6,
    **kwargs: Any
):
    """
    Calls an SP-API function with:
      - minimum interval spacing between calls (simple client-side throttle)
      - exponential backoff + jitter on 429/QuotaExceeded

    Usage:
        actions = call_with_rate_limit(sol_api.get_solicitation_actions_for_order,
                                       amazonOrderId=order_id)
        call_with_rate_limit(sol_api.create_product_review_and_seller_feedback_solicitation,
                             amazonOrderId=order_id)

    You can override min_interval per call if an endpoint allows faster/lower.
    """
    # simple per-process last-call timestamp
    now = time.monotonic()
    last_ts = getattr(call_with_rate_limit, "_last_ts", None)
    if last_ts is not None:
        wait = min_interval - (now - last_ts)
        if wait > 0:
            time.sleep(wait)

    attempt = 0
    while True:
        try:
            result = fn(*args, **kwargs)
            # stamp success time
            setattr(call_with_rate_limit, "_last_ts", time.monotonic())
            return result
        except SellingApiRequestThrottledException as e:
            # Respect server hint if present
            server_wait = _read_reset_from_headers(e)
            if server_wait is not None and server_wait > 0:
                time.sleep(server_wait)
            else:
                # exponential backoff + jitter
                backoff = min(2 ** attempt, 32) + random.random()
                time.sleep(backoff)
            attempt += 1
            if attempt > max_retries:
                raise
        except SellingApiException:
            # Other SP-API errors: do not loop forever
            raise
