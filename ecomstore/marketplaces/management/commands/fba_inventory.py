# yourapp/management/commands/your_task.py

from django.core.management.base import BaseCommand
from ecomstore.marketplaces.models import FBAShipment  # Replace with your model
from datetime import datetime
from sp_api.api import Inventories
from sp_api.base import Marketplaces, SellingApiException, Credentials
import tempfile
from ecomstore.settings import AMZN_SP_REFRESH_TOKEN, AMZN_SP_LWA_APP_ID,AMZN_SP_LWA_CLIENT_SECRET, ADMINS, DEFAULT_FROM_EMAIL
from django.db.models import Q
from ecomstore.utils.email import send_mail_async
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
        inventories = Inventories(credentials=credentials, marketplace=Marketplaces.US)


        from ecomstore.marketplaces.models import FBAShipment  # Replace with your model name
        import time

        # Step 1: Get all SKUs that have at least one FBAShipment with status "inactive"
        #skus_with_inactive_status = FBAShipment.objects.filter(status="inactive").values_list('sku', flat=True)
        #print(list(skus_with_inactive_status))
        # Step 2: Query for distinct SKU values, excluding those that have any inactive status
        #unique_skus = FBAShipment.objects.exclude(sku__in=skus_with_inactive_status).exclude(sku__isnull=True).values_list('sku', flat=True).distinct()
        # Query the table for distinct SKU values
        #unique_skus = FBAShipment.objects.exclude(status="inactive").values_list('sku', flat=True).distinct()

        # Convert the QuerySet to a list (if needed)
        #sku_list = list(unique_skus)
        #print("Final sku list:")
        #print(sku_list)

        # Step 1: Query to get all unique SKUs
        all_skus = FBAShipment.objects.values_list('sku', flat=True).distinct()
        print("number of all skus = ", len(list(all_skus)))
        # Step 2: Query to get unique SKUs that have at least one 'inactive' status
        skus_with_inactive_status = FBAShipment.objects.filter(status="inactive").values_list('sku', flat=True).distinct()
        print("number of inactive skus = ", len(list(skus_with_inactive_status)))

        # Step 3: Reconstruct a list of SKUs by eliminating SKUs with 'inactive' status
        sku_list = [sku for sku in all_skus if sku not in skus_with_inactive_status]

        # Now valid_skus contains SKUs that do not have any 'inactive' status
        print("number of final skus = ", len(list(sku_list)))
        print(sku_list)

        output = ""  # Initialize an empty string to accumulate the output

        # Now you can loop through the individual SKUs
        for sku in sku_list:
            obj = FBAShipment.objects.filter(sku=sku).order_by('-ship_date').first()


            if sku:
       	       try:
                  # Retrieve product types
                  response = inventories.get_inventory_summary_marketplace(**{"details": True, "sellerSkus": [obj.sku]})
                  y = response.payload
                  #import json
                  #print(json.dumps(y, indent=4))
                  inventory = y["inventorySummaries"][0]
                  productName = inventory['productName']

                  output += f"""
                    <table border="1" cellpadding="5" cellspacing="0">
                    <tr>
                    <th colspan="2" style="text-align:center; font-size:16px;">{obj.products}</th>
                    <th colspan="13" style="text-align:left; font-size:12px;">{productName}</th>
                    </tr>
                    <tr>
                    <td>ASIN</td><td>{obj.asin}</td>
                    <td>SKU</td><td>{sku}</td>
                    <td>Last Shipped</td><td>{obj.ship_date.date()}</td>
                    <td>Last Received</td><td>{obj.received_date}</td>
                    </tr>
                    <tr>
                    <th>Fulfillable</th>
                    <th>Inbound Working</th>
                    <th>Inbound Shipped</th>
                    <th>Inbound Received</th>
                    <th>Total Reserved</th>
                    <th>Pending Customer</th>
                    <th>Inbound Transshipment</th>
                    <th>FC Processing</th>
                    <th>Total Unfulfillable</th>
                    <th>Customer Damaged</th>
                    <th>Warehouse Damaged</th>
                    <th>Distributor Damaged</th>
                    <th>Carrier Damaged</th>
                    <th>Defective</th>
                    <th>Expired</th>

                    </tr>
                    """

                  # Fulfillable and inbound info
                  x = inventory['inventoryDetails']

                  output += f"""
                    <td>{x['fulfillableQuantity']}</td>
                    <td>{x['inboundWorkingQuantity']}</td>
                    <td>{x['inboundShippedQuantity']}</td>
                    <td>{x['inboundReceivingQuantity']}</td>
                  """

                  # Reserved quantities
                  z = x['reservedQuantity']
                  output += f"""
                    <td>{z['totalReservedQuantity']}</td>
                    <td>{z['pendingCustomerOrderQuantity']}</td>
                    <td>{z['pendingTransshipmentQuantity']}</td>
                    <td>{z['fcProcessingQuantity']}</td>
                  """

                  # Unfulfillable quantities
                  z = x['unfulfillableQuantity']
                  output += f"""
                    <td>{z['totalUnfulfillableQuantity']}</td>
                    <td>{z['customerDamagedQuantity']}</td>
                    <td>{z['warehouseDamagedQuantity']}</td>
                    <td>{z['distributorDamagedQuantity']}</td>
                    <td>{z['carrierDamagedQuantity']}</td>
                    <td>{z['defectiveQuantity']}</td>
                    <td>{z['expiredQuantity']}</td></tr></table>

                  """

                  time.sleep(1)

               except Exception as e:
                 output += f"""
                    <td>Error</td><td>{str(e)}</td></tr>"""

                 # Close the table
                 output += "</table>"
                 continue
            else:
                continue

        self.stdout.write(self.style.SUCCESS(output))
        # Send email with the HTML table
        admin_emails = [v for k,v in ADMINS]
        send_mail(
            subject="Inventory Report",
            message="Here is your inventory report.",
            from_email="sales@andrew-amanda.com",
            recipient_list=admin_emails,
            fail_silently=False,
            html_message=output  # This sends the table as an HTML-formatted message
        )
