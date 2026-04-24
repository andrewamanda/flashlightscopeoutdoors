import os
import urllib
import trml2pdf

#from django.conf import settings
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, Context
from django.shortcuts import get_object_or_404
from django.utils.encoding import smart_str, smart_text
from django.views.decorators.cache import never_cache
#from satchmo_store.shop.models import Order
from ecomstore.store.models import Config
from ecomstore.catalog.models import Product
from ecomstore.checkout.models import Order, OrderItem, ShippingMethod
from ecomstore.marketplaces.models import JETOrder, JET_ORDER_STATUS
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from ecomstore.settings import SITE_URL





def all_orders(request, template_name="process_order/all_orders.html"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'all_orders'
    orders = Order.objects.all()
    return render(request, template_name, locals())



def displayDoc(request, id, doc):
    # Create the HttpResponse object with the appropriate PDF headers for an invoice or a packing slip

    l = id.find("-")
    if l == -1:
        order_id = id
    else:
        h = id.rfind("-")
        order_id = id[l+1:h]

    #order = get_object_or_404(Order, pk=order_id)
    order = get_object_or_404(Order, invoice_number=id)
    shopDetails = Config.objects.get_current()
    filename_prefix = shopDetails.site.domain
    if doc == "invoice":
        filename = "%s-invoice.pdf" % filename_prefix
        template = "invoice.rml"
    elif doc == "packingslip":
        filename = "%s-packingslip.pdf" % filename_prefix
        template = "packing-slip.rml"
    elif doc == "shippinglabel":
        filename = "%s-shippinglabel.pdf" % filename_prefix
        template = "shipping-label.rml"
        order.status = 3
        order.save()
    else:
        return HttpResponseRedirect('/admin')
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    #icon_uri = config_value('SHOP', 'LOGO_URI')
    icon_uri = "https://" + SITE_URL + "/static/images/siteImg/logo_224x70.jpg"
    #icon_uri = "file:///C:\Aimkon\stores\aimkon2\satchmo\store\..\store\static/images/sample-log.bmp"
    t = loader.get_template(os.path.join('process_order/pdf', template))
    c = {
                'filename' : filename,
                'iconURI' : icon_uri,
                'shopDetails' : shopDetails,
                'order' : order,
                }
    try:
         pdf = trml2pdf.parseString(smart_str(t.render(c)))
    except:
         dirspot = os.getcwd()
         #print "dirspot****** = ",dirspot
         icon_uri = dirspot + "/ecomstore/static/images/siteImg/logo_224x70.jpg"
         c = {
                'filename' : filename,
                'iconURI' : icon_uri,
                'shopDetails' : shopDetails,
                'order' : order,
              }
         pdf = trml2pdf.parseString(smart_str(t.render(c)))
    response.write(pdf)
    return response
displayDoc = staff_member_required(never_cache(displayDoc))


def generate_invoice(order):



    shopDetails = Config.objects.get_current()
    filename_prefix = shopDetails.site.domain
    filename = "%s-invoice.pdf" % filename_prefix
    template = "invoice.rml"

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename


    icon_uri = "https://" + SITE_URL + "/static/images/siteImg/logo.jpg"
    t = loader.get_template(os.path.join('process_order/pdf', template))
    c = {
                'filename' : filename,
                'iconURI' : icon_uri,
                'shopDetails' : shopDetails,
                'order' : order,
                }
    try:
         pdf = trml2pdf.parseString(smart_str(t.render(c)))
    except:
         dirspot = os.getcwd()
         #print "dirspot*******",dirspot
         icon_uri = dirspot + "/ecomstore/static/images/siteImg/logo.jpg"
         c = {
                'filename' : filename,
                'iconURI' : icon_uri,
                'shopDetails' : shopDetails,
                'order' : order,
              }
         pdf = trml2pdf.parseString(smart_str(t.render(c)))
    response.write(pdf)
    return pdf

from ecomstore.utils.basic_auth_decorator import logged_in_or_basicauth
import datetime

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def process_orders_by_shipstation(request, template_name="process_order/shipstation_orders.xml"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'process orders by shipstation'
    if request.method == "GET":
        action = request.GET.get('action', None)
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)
        start_time = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
        end_time = datetime.datetime.strptime(end_date, "%m/%d/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
    else:
        action = request.GET.get('action')
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)


    if action == "export":
        orders = Order.objects.all().filter(last_updated__gte=start_time).exclude(last_updated__gte=end_time)
        return render(request, template_name, locals())
    elif action == "shipnotify":
        order_number = request.GET.get("order_number")
        carrier = request.GET.get("carrier")
        service = request.GET.get("service")
        tracking_number = request.GET.get("tracking_number")


        order = Order.objects.filter(invoice_number = order_number)[0]
        order.status = Order.SHIPPED
        order.tracking = tracking_number

        #print "Updating for order {} with tracking number {}".format(order_number,tracking_number)
        order.ship_date = datetime.datetime.now()
        order.save()

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=200)

@csrf_exempt
def process_orders_by_shipstation_4jet(request, template_name="process_order/shipstation_orders.xml"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'process jet orders by shipstation'
    if request.method == "GET":
        action = request.GET.get('action', None)
        #start_date = request.GET.get('start_date', None)
        #end_date = request.GET.get('end_date', None)
        #start_time = datetime.datetime.strptime(start_date, "%m/%d/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
        #end_time = datetime.datetime.strptime(end_date, "%m/%d/%Y %H:%M").strftime("%Y-%m-%d %H:%M")
    else:
        action = request.GET.get('action')
        start_date = request.GET.get('start_date', None)
        end_date = request.GET.get('end_date', None)


    if action == "export":
        jetorders = JETOrder.objects.all().filter(status="acknowledged")
        orders = []

        for o in jetorders:
                order = Order()
                order.id = o.reference_order_id
                order.invoice_number = o.reference_order_id
                order.date = datetime.datetime.now()
                if o.status == "acknowledged":
                        order.status = Order.SUBMITTED
                if o.status == "complete":
                        order.status = Order.SHIPPED
                order.last_updated = datetime.datetime.now()
                order.shipping_method = ShippingMethod.objects.get(name="Domestic Standard")
                order.transaction_id = o.merchant_order_id
                order.shipping_charged = o.order_totals_item_price_item_shipping_cost
                order.billing_name = o.shipping_to_recipient_name
                order.billing_address_1 = o.shipping_to_address_address1
                order.billing_address_2 = o.shipping_to_address_address2
                order.billing_city = o.shipping_to_address_city
                order.billing_state = o.shipping_to_address_state
                order.billing_zip = o.shipping_to_address_zip_code
                order.billing_country = "US"
                order.shipping_name = o.shipping_to_recipient_name
                order.shipping_address_1 = o.shipping_to_address_address1
                order.shipping_address_2 = o.shipping_to_address_address2
                order.shipping_city = o.shipping_to_address_city
                order.shipping_state = o.shipping_to_address_state
                order.shipping_zip = o.shipping_to_address_zip_code
                order.shipping_country = "US"
                order.isItGift = "No"
                order.giftmessage = " "
                order.email = o.hash_email
                order.phone = o.buyer_phone_number

                order.items = []
                for ji in o.jetorder_items_set.all():
                     item = OrderItem()
                     item.product = Product()
                     item.product.sku = ji.merchant_sku
                     item.product.name = ji.product_title
                     item.price = o.order_totals_item_price_base_price
                     item.quantity = ji.request_order_quantity
                     order.items.append(item)

                orders.append(order)



        return render(request, template_name, locals())
    elif action == "shipnotify":
        order_number = request.GET.get("order_number")
        carrier = request.GET.get("carrier")
        service = request.GET.get("service")
        tracking_number = request.GET.get("tracking_number")

        #print "********JET notifying: order_number = ", order_number
        #print "********JET notifying: tracking_number = ", tracking_number
        order = JETOrder.objects.get(reference_order_id = order_number)
        order.status = "inprogress"
        order.tracking_number = tracking_number

        #print "Updating for order {} with tracking number {}".format(order_number,tracking_number)
        order.ship_date = datetime.datetime.now()
        order.save()

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=200)


@csrf_exempt
def process_orders_by_shipworks(request, template_name="process_order/shipstation_orders.xml"):
    """ page displaying customer account information, past order list and account options """

@csrf_exempt
def process_orders_by_shipworks(request, template_name="process_order/shipstation_orders.xml"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'process orders by shipworks'

    module_version = '3.6.3'
    schema_version = '1.0.0'

    if request.method == "GET":
        action = request.GET.get('action', None)
        username = request.GET.get('username', None)
        password = request.GET.get('password', None)
    else:
        #print "*******shipworks, it is a POST"
        action = request.POST.get('action', None)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)


    if not (username == 'andrew-amanda' and password == 'Wei6ming'):
        errCode = '00001'
        errText = 'Authentication Failure'
        template_name = "process_order/shipworks_ErrorResponse.xml"
        return render(request, template_name, locals())

    if action == "getmodule":
        template_name = "process_order/shipworks_GetModule.xml"
        return render(request, template_name, locals())

    elif action == "getstore":
        template_name = "process_order/shipworks_GetStore.xml"
        return render(request, template_name, locals())
    elif action == "getstatuscodes":
        template_name = "process_order/shipworks_GetStatusCodes.xml"
        return render(request, template_name, locals())
    elif action == "getcount":
        start = request.POST.get('start', None)
        start = start.replace('T', ' ')
        orders = Order.objects.all().filter(last_updated__gte=start)
        order_count = len(orders)
        template_name = "process_order/shipworks_GetCount.xml"
        return render(request, template_name, locals())
    elif action == "getorders":
        start = request.POST.get('start', None)
        start = start.replace('T', ' ')

        maxcount = request.POST.get('maxcount')
        orders = Order.objects.all().filter(last_updated__gte=start)
        order_count = len(orders)
        template_name = "process_order/shipworks_GetOrders.xml"
        return render(request, template_name, locals())

    else:
        return HttpResponse(status=200)
