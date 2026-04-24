from ecomstore.checkout import google_checkout
from ecomstore.cart import cart
from ecomstore.checkout.models import Order, OrderItem, ShippingMethod, Promotion, GiftCertificate
from ecomstore.checkout.forms import CheckoutForm, GiftCertCheckoutForm
from ecomstore.checkout import authnet
from ecomstore import settings
from ecomstore.nameyourprice.util import is_auction, get_auction_price

from django.urls import reverse
import urllib

import random
from django.core.mail import send_mail
from ecomstore.settings import EMAIL_ORDER

from ecomstore.utils import checkout_audit
from django.contrib.auth.models import User
from django.utils.encoding import smart_str, smart_text




def get_checkout_url(request):
    """ returns the URL from the checkout module for cart """

    postdata = request.POST.copy()
    payment_type = postdata.get('payment_type','')
    if payment_type == 'Google':
        # use this for Google Checkout API:
        return google_checkout.get_checkout_url(request)
    if payment_type == 'CreditCard':
        # use this for our own-site checkout
        return reverse('checkout')
    checkout_stage = postdata.get('checkout_stage')
    if checkout_stage == 'Begin':
        # start the general checkout process
        return reverse('beginCheckout')

def process(request):
    """ takes a POST request containing valid order data; pings the payment gateway with the billing
    information and returns a Python dictionary with two entries: 'order_number' and 'message' based on
    the success of the payment processing. An unsuccessful billing will have an order_number of 0 and an error message,
    and a successful billing with have an order number and an empty string message.

    """
    # Transaction results
    APPROVED = '1'
    DECLINED = '2'
    ERROR = '3'
    HELD_FOR_REVIEW = '4'

    postdata = request.POST.copy()
    card_num = postdata.get('credit_card_number','')
    exp_month = postdata.get('credit_card_expire_month','')
    exp_year = postdata.get('credit_card_expire_year','')
    exp_date = exp_month + exp_year
    cvv = postdata.get('credit_card_cvv','')
    # amount = cart.cart_subtotal(request)
    amount = postdata.get('total_amt_due','')

    #if is_auction(request):
    #    amount = get_auction_price(request)

    checkout_audit._audit(request, 'checkout_process', 'Obtain credit card information: ' + card_num + '|' + exp_month + ' ' + exp_date + ',' + exp_year + '|' + cvv)

    results = {}

    response = authnet.do_auth_capture(amount=amount,
                                       card_num=card_num,
                                       exp_date=exp_date,
                                       card_cvv=cvv,
                                       bfname=smart_str(request.session.get('billing_name',None)),
                                       baddr=smart_str(request.session.get('billing_address_1',None)),
                                       bcity=request.session.get('billing_city',None),
                                       bstate=smart_str(request.session.get('billing_state',None)),
                                       bzip=request.session.get('billing_zip',None),
                                       bphone=request.session.get('Phone',None),
                                       bcountry=request.session.get('billing_country',None),
                                       #bcountry=request.session.get('billing_country_name',None),
                                       sfname=smart_str(request.session.get('shipping_name',None)),
                                       saddr=smart_str(request.session.get('shipping_address_1',None)),
                                       scity=smart_str(request.session.get('shipping_city',None)),
                                       sstate=smart_str(request.session.get('shipping_state',None)),
                                       szip=request.session.get('shipping_zip',None),
                                       scountry=request.session.get('shipping_country',None))
                                       #scountry=request.session.get('shipping_country_name',None))

    if response[0] == APPROVED:
        checkout_audit._audit(request, 'checkout_process', 'Credit card authorization response: ' + ', '.join(response))
        transaction_id = response[6]
        order = create_order(request, transaction_id)
        results = {'order_number': order.id, 'message': u''}
    if response[0] == DECLINED:
        checkout_audit._audit(request, 'checkout_process', 'Credit card authorization response: ' + ', '.join(response), 'Error')
        results = {'order_number': 0, 'message': u'There is a problem with your credit card.'}
    if response[0] == ERROR or response[0] == HELD_FOR_REVIEW:
        checkout_audit._audit(request, 'checkout_process', 'Credit card authorization response: ' + ', '.join(response), 'Error')
        results = {'order_number': 0, 'message': u'Error processing your credit card payment, your account has not been charged.'}

    return results

def process_giftcertificate(request):
    """ takes a POST request containing valid order data; pings the payment gateway with the billing
    information and returns a Python dictionary with two entries: 'order_number' and 'message' based on
    the success of the payment processing. An unsuccessful billing will have an order_number of 0 and an error message,
    and a successful billing with have an order number and an empty string message.

    """

    postdata = request.POST.copy()
    transaction_id = 'gift' + request.session.get('valid_giftcode','')
    order = create_order(request, transaction_id)
    results = {'order_number': order.id, 'message': u''}

    return results

def create_order(request, transaction_id):
    """ if the POST to the payment gateway successfully billed the customer, create a new order
    containing each CartItem instance, save the order with the transaction ID from the gateway,
    and empty the shopping cart

    """
    order = Order()
    if transaction_id.startswith('gift'):
        checkout_form = GiftCertCheckoutForm(request.POST, instance=order)
        order = checkout_form.save(commit=False)
    elif transaction_id.startswith('pi_'):
        for key, value in request.session.items():
            print('{} => {}'.format(key, value))
        checkout_form = CheckoutForm(request.session, instance=order)
        order = checkout_form.save(commit=False)
    else:
        checkout_form = CheckoutForm(request.POST, instance=order)
        order = checkout_form.save(commit=False)

    order.transaction_id = transaction_id
    order.ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if not order.ip_address:
        order.ip_address = request.META.get('REMOTE_ADDR')
    if not order.ip_address:
        order.ip_address = '127.0.0.1'

    order.user = User.objects.get(username='anonymous')
    if request.user.is_authenticated:
        order.user = request.user
    else:
        print ("user is not authenticated")
    order.status = Order.SUBMITTED

    postdata = request.POST.copy()
    smethod = request.POST.get('shipping_method',None)
    if not smethod:
        smethod = request.session['shippingLevel']
    shippingmethod = ShippingMethod.objects.get(name=smethod)

    try:
        if postdata['promotion']:
            pcode = postdata['promotion']
        else:
            pcode = request.session['promotion']
        promotion = Promotion.objects.get(code=pcode)
    except:
        promotion = None

    order.shipping_method = shippingmethod
    order.promotion = promotion

    from ecomstore.utils.models import base_country
    #billing_country_key = request.session.get('billing_country','')
    #order.billing_country = base_country.objects.get(id = billing_country_key)
    #shipping_country_key = request.session.get('shipping_country','')
    #order.shipping_country = base_country.objects.get(id = shipping_country_key)
    order.billing_country = request.session.get('billing_country','')
    order.shipping_country = request.session.get('shipping_country','')
    order.shipping_charged = request.session.get('shipping_charge','')

    order.save()

    save_order_details(request, order)

    return order

def _generate_giftcertificate_code():
    """ function for generating random cart ID values """
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$*'
    cart_id_length = 16
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def save_order_details(request, order):
    if order.pk:
        """ if the order save succeeded """
        cart_items = cart.get_cart_items(request)
        for ci in cart_items:
            """ create order item for each cart item """
            oi = OrderItem()
            oi.order = order
            oi.quantity = ci.quantity
            oi.price = ci.price  # now using @property
            oi.product = ci.product

            """ need to take care of the optional choices """
            oc = ci.cartitemoption_set.all()
            oi.options = ""
            for o in oc:
                oi.options += o.title + "-" + o.option
                if o.price > 0:
                    oi.options += "($"
                    oi.options += str(o.price)
                    oi.options += ")"
                oi.options += ";"

                if ci.product.slug == "gift-certificate":
                    count = ci.quantity
                    while count > 0:
                        count -= 1
                        gc = GiftCertificate()
                        gc.code = _generate_giftcertificate_code()
                        gc.face_value = o.price
                        gc.balance = gc.face_value
                        #gc.to_email = o.option[o.option.find("--")+2:o.option.find("(")+1]
                        gc.to_email = o.lucky_email
                        gc.from_email = order.email
                        gc.message = o.gift_message
                        gc.save()

                        email_msg = gc.from_email

                        email_msg = email_msg + " is sending you a gift certificate with certificate number: "
                        email_msg = email_msg + gc.code
                        email_msg = email_msg + ". The certificate has the value of $" + str(gc.face_value)

                        if o.gift_message:
                            email_msg += "\n\n Message from " + gc.from_email
                            email_msg += ":\n\n" + o.gift_message

                        subject = "You receive a gift certificate!"
                        src_email = EMAIL_ORDER

                        #email.send_email(gc.to_email, src_email, subject, email_msg)
                        send_mail(subject, email_msg, src_email, [gc.to_email, gc.from_email, EMAIL_ORDER], fail_silently=False)


            oi.save()
        # all set, clear the cart
        cart.empty_cart(request)

        # save profile info for future orders
        #if request.user.is_authenticated():
        #    from ecomstore.accounts import profile
        #    profile.set(request)
