# yourapp/management/commands/your_task.py

from django.core.management.base import BaseCommand
from ecomstore.marketplaces.models import FBAShipment  # Replace with your model
from datetime import datetime
from sp_api.api import FulfillmentInbound
from sp_api.base import Marketplaces, SellingApiException, Credentials
import tempfile
from ecomstore.settings import AMZN_SP_REFRESH_TOKEN, AMZN_SP_LWA_APP_ID,AMZN_SP_LWA_CLIENT_SECRET, ADMINS
from django.db.models import Q
from django.utils import timezone
import time
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Task to interact with the model'

    def handle(self, *args, **kwargs):

        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

                # Initialize the FulfillmentInbound API client
        fulfillment_inbound = FulfillmentInbound(credentials=credentials, marketplace=Marketplaces.US)



        output = ""  # Initialize an empty string to accumulate the output
        # Access the model and perform your task
        objects = FBAShipment.objects.filter(Q(status="pendingamazon") & ~Q(status="inactive"))
        output += """
            <table border="1" cellpadding="5" cellspacing="0">
            <tr>
            <th colspan="2" style="text-align:center; font-size:16px;">Pending Amazon Approval</th>
            </tr>
            <tr>
            <th>Products</th>
            <th>ASIN</th>
            <th>SKU</th>
            </tr>
            """

        for obj in objects:
            output += f"""<tr><td>{obj.products}</td><td>{obj.asin}</td><td>{obj.sku}</td></tr>"""
        output += "</table>"

        objects = FBAShipment.objects.filter(Q(status="holdshipping") & ~Q(status="inactive"))
        output += """
            <table border="1" cellpadding="5" cellspacing="0">
            <tr>
            <th colspan="2" style="text-align:center; font-size:16px;">Shipment on Hold</th>
            </tr>
            <tr>
            <th>Products</th>
            <th>ASIN</th>
            <th>SKU</th>
            </tr>
            """

        for obj in objects:
            output += f"""<tr><td>{obj.products}</td><td>{obj.asin}</td><td>{obj.sku}</td></tr>"""
        output += "</table>"

        objects = FBAShipment.objects.filter(Q(status="readytoship") & ~Q(status="inactive"))
        output += """
            <table border="1" cellpadding="5" cellspacing="0">
            <tr>
            <th colspan="2" style="text-align:center; font-size:16px;">Ready to ship</th>
            </tr>
            <tr>
            <th>Products</th>
            <th>ASIN</th>
            <th>SKU</th>
            <th>Quantity to ship</th>
            </tr>
            """

        for obj in objects:
            output += f"""<tr><td>{obj.products}</td><td>{obj.asin}</td><td>{obj.sku}</td><td>{obj.quantity_shipped}</td></tr>"""
        output += "</table>"

        # Access the model and perform your task
        objects = FBAShipment.objects.filter(~Q(status="inactive") & (Q(status="shipped") | Q(status="readytopack")))
        output += """
            <table border="1" cellpadding="5" cellspacing="0">
            <tr>
            <th colspan="2" style="text-align:center; font-size:16px;">Recently Shipped</th>
            </tr>
            <tr>
            <th>Shipment ID</th>
            <th>ASIN</th>
            <th>Products</th>
            <th>Quantity Shipped</th>
            <th>Quantity Received</th>
            <th>Shipped Date</th>
            <th>Received Date</th>
            </tr>
        """

        for obj in objects:
            output += f"""<tr><td>{obj.shipmentid}</td><td>{obj.asin}</td><td>{obj.products}</td><td>{obj.quantity_shipped}</td>"""  # Concatenate with a newline

            if 'FBA' in obj.shipmentid:
       	       try:
                  # Retrieve product types
                  response = fulfillment_inbound.shipment_items_by_shipment(shipment_id = obj.shipmentid)
                  payload = response.payload
                  for x in payload["ItemData"]:
                      output += f"""<td>{x['QuantityReceived']}</td><td>{obj.ship_date.date()}</td><td>{obj.received_date}</td></tr>"""

                      obj.quantity_received = x["QuantityReceived"]
                      obj.sku = x["SellerSKU"]
                      if obj.quantity_shipped == obj.quantity_received:
                          obj.status = "complete"
                          obj.received_date = timezone.now().date()
                      else:
                          if obj.quantity_received > 0:
                              obj.status = "inconsistent"
                              obj.received_date = timezone.now().date()
                      obj.save()
                      time.sleep(1)


               except SellingApiException as e:
                 output += f"""<td>{str(e)}</td></tr>"""
                 continue
        output += "</table>"

        objects = FBAShipment.objects.filter(Q(status="inconsistent") & ~Q(status="inactive"))
        output += """
            <table border="1" cellpadding="5" cellspacing="0">
            <tr>
            <th colspan="2" style="text-align:center; font-size:16px;">Inconsistencies</th>
            </tr>
            <tr>
            <th>Shipmentid</th>
            <th>Products</th>
            <th>Quantity Shipped</th>
            <th>Quantity Received</th>
            <th>Date Shipped</th>
            </tr>
            """
        for obj in objects:
            output += f"""<tr><td>{obj.shipmentid}</td><td>{obj.asin}</td><td>{obj.products}</td><td>{obj.quantity_shipped}</td>"""  # Concatenate with a newline

            if 'FBA' in obj.shipmentid:
       	       try:
                  # Retrieve product types
                  response = fulfillment_inbound.shipment_items_by_shipment(shipment_id = obj.shipmentid)
                  payload = response.payload
                  for x in payload["ItemData"]:
                      output += f"""<td>{x['QuantityReceived']}</td><td>{obj.ship_date.date()}</td><td>{obj.received_date}</td></tr>"""
                      obj.quantity_received = x["QuantityReceived"]
                      obj.sku = x["SellerSKU"]
                      if obj.quantity_shipped == obj.quantity_received:
                          obj.status = "complete"
                          obj.received_date = timezone.now().date()
                      else:
                          if obj.quantity_received > 0:
                              obj.status = "inconsistent"
                              obj.received_date = timezone.now().date()
                      obj.save()
                      time.sleep(1)


               except SellingApiException as e:
                 output += f"""<td>{str(e)}</td></tr>"""
                 continue
        output += "</table>"

        objects = FBAShipment.objects.filter(~Q(status="inactive") & (Q(status="casesubmitted") | Q(status="caseapproved") | Q(status="caserejected")))
        output += """
            <table border="1" cellpadding="5" cellspacing="0">
            <tr>
            <th colspan="2" style="text-align:center; font-size:16px;">Appeal Case Filed</th>
            </tr>
            <tr>
            <th>Shipmentid</th>
            <th>Products</th>
            <th>Quantity Shipped</th>
            <th>Quantity Received</th>
            <th>Date Shipped</th>
            <th>Case Status</th>
            </tr>
            """
        for obj in objects:
               output += f"""<tr><td>{obj.shipmentid}</td><td>{obj.products}</td><td>{obj.quantity_shipped}</td>"""
       	       try:
                  # Retrieve product types
                  response = fulfillment_inbound.shipment_items_by_shipment(shipment_id = obj.shipmentid)
                  payload = response.payload
                  for x in payload["ItemData"]:
                      output += f"""<td>{x['QuantityReceived']}</td><td>{obj.ship_date.date()}</td><td>{obj.status}</td></tr>"""

                      obj.quantity_received = x["QuantityReceived"]
                      obj.sku = x["SellerSKU"]
                      if obj.quantity_shipped == obj.quantity_received:
                          obj.status = "caseapproved"
                          obj.received_date = timezone.now().date()

                      obj.save()
                      time.sleep(1)


               except SellingApiException as e:
                 output += f"""<td>{str(e)}</td></tr>"""
                 continue

        output += "</table>"


        self.stdout.write(self.style.SUCCESS(output))
        admin_emails = [v for k,v in ADMINS]
        send_mail(
            subject="FBA Shipment Report",
            message="Here is your FBA shipment report.",
            from_email="sales@andrew-amanda.com",
            recipient_list=admin_emails,
            fail_silently=False,
            html_message=output  # This sends the table as an HTML-formatted message
        )
