from ecomstore.checkout.models import Order, OrderItem
from django.shortcuts import get_object_or_404
from ecomstore.catalog.models import Product
from django.contrib.auth.models import User

def create_new_order_from_jet(order_details):
    order = Order()

    order.email = order_details['hash_email']
    order.phone = order_details['buyer']['phone_number']

    #shipping information
    order.shipping_name = order_details['shipping_to']['recipient']['name']
    order.shipping_address_1 = order_details['shipping_to']['address']['address1']
    order.shipping_address_2 = order_details['shipping_to']['address']['address2']
    order.shipping_city = order_details['shipping_to']['address']['city']
    order.shipping_state = order_details['shipping_to']['address']['state']
    order.shipping_country = "US"

    #shipping_country_key = request.session.get('shipping_country','')
    #order.shipping_country = base_country.objects.get(id = shipping_country_key)

    order.shipping_zip = order_details['shipping_to']['address']['zip_code']

    #billing information
    #order.billing_name = request.session.get('billing_name','')
    #order.billing_address_1 = request.session.get('billing_address_1','')
    #order.billing_address_2 = request.session.get('billing_address_2','')
    #order.billing_city = request.session.get('billing_city','')
    #order.billing_state = request.session.get('billing_state','')
    #order.billing_country = request.session.get('billing_country','')
    #order.billing_zip = request.session.get('billing_zip','')

    order.status = Order.SUBMITTED
    order.transaction_id = order_details['reference_order_id']

    order.invoice_number = order_details['merchant_order_id']

    order.user = User.objects.get(username='jet.com')


    #gift information
    #order.isItGift = request.session.get('isItGift','')
    #order.pricePrinted = request.session.get('pricePrinted','')
    #order.giftmessage = request.session.get('giftmessage','')

    #order.isItAuction = is_auction(request)

    order.shipping_method = None
    order.promotion = None
    #order.shipping_charged = request.session.get('shipping_charge','')

    order.save()

    if order.pk:
        """ if the order save succeeded """
        cart_items = order_details['order_items']
        for ci in cart_items:
            """ create order item for each cart item """
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci['request_order_quantity']
            oi.price = ci['item_price']['base_price']  # now using @property
            #print "merchant sku=",ci['merchant_sku'].lstrip().rstrip()
            oi.product = get_object_or_404(Product.active, slug=ci['merchant_sku'].lstrip().rstrip())
            oi.save()

    return "Success"
