from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse, QueryDict

from ecomstore.checkout.forms import CreditCardForm, AddressForm
from ecomstore.checkout.models import Order, OrderItem, ShippingMethod, Promotion, ProductOnlyPromotion, referral, GiftCertificate, StripePaymentAttempt
from ecomstore.checkout import *
from ecomstore.checkout.checkout import save_order_details
from ecomstore.cart import cart
from ecomstore.utils import email,checkout_audit,strops
from ecomstore.utils.strops import normalize_str
from ecomstore.utils.states import abbreviation_us


from ecomstore.accounts import profile
from ecomstore.accounts.forms import UserProfileForm
from ecomstore.nameyourprice.util import is_auction, get_auction_price, Auction_Paid

from django.core.mail import EmailMessage
from django.contrib import messages
import json as simplejson

from ecomstore.process_order.views import generate_invoice, displayDoc


from ecomstore.stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW, NUM_OF_NEW_ARRIVALS, CACHE_TIMEOUT, SITE_VERSION
from ecomstore.catalog.models import Product, Category, Brand
from datetime import datetime
from decimal import Decimal, ROUND_UP
from django.utils.translation import gettext as _

from ecomstore.paypal_driver.driver import PayPal
from ecomstore.paypal_driver.models import PayPalResponse
from ecomstore.paypal_driver.utils import process_payment_request, \
    process_refund_request

import random

from ecomstore import settings

from ecomstore.accounts import profile
from django.core.mail import send_mail
from ecomstore.settings import EMAIL_ORDER
from django.contrib.auth.models import User, AnonymousUser

from ecomstore.utils.models import base_country
import traceback
from types import SimpleNamespace
from ecomstore.utils.email import send_mail_async


from django.utils.encoding import smart_str, smart_text
from django.core.cache import cache



def checkout_begin(request, template_name='checkout/addresses.html'):
    """ checkout form page to collect user shipping and billing information """
    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    if SITE_VERSION == "NEW_SKIN":
        template_name = "2023/checkout/addresses.html"

    if request.method == 'POST':


        postdata = request.POST.copy()
        form = AddressForm(postdata)
        if form.is_valid():
             checkout_audit._audit(request, 'checkout_begin', 'collecting the address')

             request.session['email'] = postdata.get('email','')
             request.session['phone'] = postdata.get('phone','')
             request.session['shipping_name'] = normalize_str(postdata.get('shipping_name',''))
             request.session['shipping_address_1'] = normalize_str(postdata.get('shipping_address_1',''))
             request.session['shipping_address_2'] = normalize_str(postdata.get('shipping_address_2',''))
             request.session['shipping_city'] = normalize_str(postdata.get('shipping_city',''))
             request.session['shipping_zip'] = normalize_str(postdata.get('shipping_zip',''))
             request.session['shipping_country'] = normalize_str(postdata.get('shipping_country',''))
             if request.session['shipping_country'] == 'US':
                   request.session['shipping_state'] = abbreviation_us(normalize_str(postdata.get('shipping_state','')))
             else:
                   request.session['shipping_state'] = normalize_str(postdata.get('shipping_state',''))
             request.session['billing_name'] = normalize_str(postdata.get('billing_name',''))
             request.session['billing_address_1'] = normalize_str(postdata.get('billing_address_1',''))
             request.session['billing_address_2'] = normalize_str(postdata.get('billing_address_2',''))
             request.session['billing_city'] = normalize_str(postdata.get('billing_city',''))
             request.session['billing_zip'] = normalize_str(postdata.get('billing_zip',''))
             request.session['billing_country'] = normalize_str(postdata.get('billing_country',''))
             if request.session['billing_country'] == 'US':
                   request.session['billing_state'] = abbreviation_us(normalize_str(postdata.get('billing_state','')))
             else:
                   request.session['billing_state'] = normalize_str(postdata.get('billing_state',''))

             checkout_audit._audit(request, 'checkout_begin', 'Shipping Name:{}, Billing Name:{},Email:{}, Phone:{}'.format(request.session.get('shipping_name'), request.session.get('billing_name'),request.session.get('email'), request.session.get('phone')))

             checkout_audit._audit(request, 'checkout_begin', 'Shipping Address:{}{}, City:{}, State:{}, Zip:{}, Country:{}'.format(request.session.get('shipping_address_1'), request.session.get('shipping_address_2'), request.session.get('shipping_city'), request.session.get('shipping_state'), request.session.get('shipping_zip'), request.session.get('shipping_country')))
             checkout_audit._audit(request, 'checkout_begin', 'Billing Address:{}{}, City:{}, State:{}, Zip:{}, Country:{}'.format(request.session.get('billing_address_1'), request.session.get('billing_address_2'), request.session.get('billing_city'), request.session.get('billing_state'), request.session.get('billing_zip'), request.session.get('billing_country')))

             if postdata.get('saveinfo') == "on":
                 form = UserProfileForm(postdata)
                 if form.is_valid():
                     profile.set(request)


             next_page = reverse('shipping_method')
             print ("next_page is ", next_page)
             return HttpResponseRedirect(next_page)
        else:
            error_message = u'Correct the errors below'
    else:
        if request.user.is_authenticated:
            user_profile = profile.retrieve(request)
            form = AddressForm(instance=user_profile)
        else:
            form = AddressForm()
    page_title = 'Checkout'
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/addresses.html'


         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)

    return render(request, template_name, locals())

def checkout_shipping_method(request, template_name='checkout/shipping_method.html'):

    if SITE_VERSION == "NEW_SKIN":
        template_name = "2023/checkout/shipping-method.html"

    """ checkout form page to collect shipping method information """
    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()


        checkout_audit._audit(request, 'checkout_shipping_method', 'Setting the shipping method')

        request.session['shippingLevel'] = postdata.get('shippingLevel','Standard Express')
        if postdata.get('isItGift') == "on":
            request.session['isItGift'] = 'Yes'
        else:
            request.session['isItGift'] = 'No'
        if postdata.get('pricePrinted') == "on":
            request.session['pricePrinted'] = 'Yes'
        else:
            request.session['pricePrinted'] = 'No'

        request.session['giftmessage'] = postdata.get('giftmessage','')
        if request.session['giftmessage'] == "":
            request.session['giftmessage'] = "no message"

        if postdata.get('haveNote') == "on":
            request.session['haveNote'] = 'Yes'
        else:
            request.session['haveNote'] = 'No'
        request.session['note'] = postdata.get('note','')
        if request.session['note'] == "":
            request.session['note'] = "no message"


        if postdata.get('isItReferral') == "on":
            request.session['isItReferral'] = 'Yes'
        else:
            request.session['isItReferral'] = 'No'

        request.session['referralCode'] = postdata.get('referralCode','')

        if "i-Parcel" in postdata.get('shippingLevel','Standard Express'):
            from ecomstore.iparcel_driver.driver import iParcel
            driver = iParcel()
            token = driver.SendiParcelRedirect(request)
            redirect_url = driver.iparcel_url(token)
            return HttpResponseRedirect(redirect_url)

        next_page = reverse('payment')
        print ("current page is ", request.path, " next_page is ", next_page)
        return HttpResponseRedirect(next_page)

    calendar_months = [ "jan", "feb", "mar", "apr", "may", "jun",
                    "jul", "aug", "sep", "oct", "nov", "dec" ]
    now = datetime.now( )
    month_name = calendar_months[ now.month-1 ]
    todays_file = month_name + "_" + ("%02d" % now.day)
    calendar_spec = "calendar_" + todays_file + ".jpg"

    if request.session['shipping_country'] == "US":
        shipping_methods = ShippingMethod.objects.exclude(name__contains="International")
    else:
        shipping_methods = ShippingMethod.objects.filter(name__contains="International")

    page_title = 'Checkout'
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/shipping_method.html'


         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)

    return render(request, template_name, locals())

def checkout_payment(request, return_url, cancel_url, error_url, template_name='checkout/payment.html', currency = "USD"):
    """ checkout form page to collect shipping method information """


    if SITE_VERSION == "NEW_SKIN":
        template_name = "2023/checkout/payment.html"

    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()

        if postdata['payment_type'] == "GiftCertificateOrder":
            checkout_audit._audit(request, 'checkout_payment', 'Start the giftcertificate payment')
            response = checkout.process_giftcertificate(request)
            order_number = response.get('order_number',0)
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)

        if postdata['payment_type'] == "CreditCardOrder":
            form = CreditCardForm(postdata)
            if form.is_valid():
                checkout_audit._audit(request, 'checkout_payment', 'Start the credit card payment')

                response = checkout.process(request)
                order_number = response.get('order_number',0)
                error_message = response.get('message','')
                if order_number:
                    request.session['order_number'] = order_number
                    receipt_url = reverse('checkout_receipt')
                    return HttpResponseRedirect(receipt_url)
            else:
                error_message = u'Correct the credit card errors below'

        if postdata['payment_type'] == "PaypalOrder":
            checkout_audit._audit(request, 'checkout_payment', 'Start the paypal payment for ' + request.session.get('email'))

            # normalize the given amount
            amount = request.POST.get("total_amt_due")
            try:
                amount = Decimal(amount)
                #amount = str(amount.quantize(Decimal(".01"), rounding = ROUND_UP))
            except:
                tb = traceback.format_exc()
                error_msg = "{}: {}".format(_(driver.setexpresscheckouterror), tb)
                subject = "An exception occured during check out"
                admin_emails = [v for k,v in settings.ADMINS]
                send_mail_async(subject, error_msg, settings.EMAIL_ORDER, admin_emails,fail_silently=False, html='')

                if request.user.is_authenticated:
                    messages.error(request, _(driver.setexpresscheckouterror))
                    #request.user.message_set.create(message = _("No given valid amount. Please check the amount that will be charged."))
                return HttpResponseRedirect(error_url)

            cart_items = None
            shopping_cart_items = cart.get_cart_items(request)
            cart_items = []

            sub_amount = Decimal(0.0)
            for i in shopping_cart_items:
                oc = i.cartitemoption_set.all()
                extra_desc =""
                extra_price = 0
                for o in oc:
                    extra_price += o.price
                    extra_desc += o.title
                    extra_desc += "-" + o.option
                    if o.price > 0:
                       extra_desc += "($"
                       extra_desc += str(o.price)
                       extra_desc += ")"
                       extra_desc += ";"


                item = {
                    'NAME':   i.name,
                    'NUMBER': i.product.sku,
                    'DESC':   (i.product.slug + '-' + extra_desc),
                    'AMT':    str(i.price + extra_price),
                    'QTY':    i.quantity
                }
                cart_items.append(item)
                sub_amount += (i.price + extra_price) * i.quantity


            shipping_price = request.POST.get('shipping_charge')
            shipping_price = Decimal(shipping_price)
            shipping_price = str(shipping_price.quantize(Decimal(".01"), rounding = ROUND_UP))
            item = {
                'NAME':   'Shipping -- ' + request.POST.get('shipping_method_name'),
                'NUMBER': '0',
                'DESC':   request.POST.get('shipping_description'),
                'AMT':    shipping_price,
                'QTY':    int(1)
            }
            cart_items.append(item)

            coupon_discount = Decimal(request.POST.get('discount'))
            if coupon_discount > 0:
                coupon_discount -= coupon_discount * 2
                coupon_discount = str(coupon_discount.quantize(Decimal(".01"), rounding = ROUND_UP))
                item = {
                    'NAME':   'Promotion - ' + request.POST.get('promotion_code'),
                    'NUMBER': '1',
                    'DESC':   (request.session.get('promotion_desc', '')),
                    'AMT':    str(coupon_discount),
                    'QTY':    int(1)
                }
                cart_items.append(item)

            auction_discount = 0.00
            if is_auction(request):
                auction_discount = Decimal(get_auction_price(request)) - sub_amount
                auction_discount = str(auction_discount.quantize(Decimal(".01"), rounding = ROUND_UP))
                item = {
                    'NAME':   'Total discount from your auction ',
                    'NUMBER': '1',
                    'DESC':   'Auction deal',
                    'AMT':    str(auction_discount),
                    'QTY':    int(1)
                }
                cart_items.append(item)

            gift_discount = Decimal(request.session.get('gift_discount'))
            if gift_discount > 0:
                gift_discount -= gift_discount * 2
                gift_discount = str(gift_discount.quantize(Decimal(".01"), rounding = ROUND_UP))
                item = {
                    'NAME':   'Gift certificate  -- ' + str(request.session.get('valid_giftcode')),
                    'NUMBER': '2',
                    'DESC':   'Paid by the gift certificate',
                    'AMT':    str(gift_discount),
                    'QTY':    int(1)
                }
                cart_items.append(item)


            amount = sub_amount + Decimal(shipping_price) + Decimal(coupon_discount) + Decimal(gift_discount)
            if is_auction(request):
                amount += Decimal(auction_discount)

            amount = amount.quantize(Decimal(".01"), rounding = ROUND_UP)


            request.session['paypal_total_amt'] = str(amount)


            # save the cart_items to the request session, so that the following DoExpressCheckoutPayment method can pass the cart item details to the paypal
            request.session['cart_items'] = cart_items

            # call the PayPal driver (2)
            driver = PayPal()
            # call the relevant API method (3)
            result = driver.SetExpressCheckout(request, amount, currency, return_url, cancel_url, cart_items)
            if driver.apierror:
                checkout_audit._audit(request, 'paypal_payment', 'paypal error: ' + driver.apierror + ': ' + return_url)
                tb = traceback.format_exc()
                error_msg = "{}: {} - total amount: {}".format(_(driver.apierror), tb, amount)
                subject = "An exception occured during Paypal check out"
                admin_emails = [v for k,v in settings.ADMINS]
                send_mail_async(subject, error_msg, settings.EMAIL_ORDER, admin_emails,fail_silently=False, html='')


            # perform the response (4)
            if not result:
                #print driver.apierror
                # show the error message (comes from PayPal API) to the user and redirect him/her to the error page
                if request.user.is_authenticated:
                    messages.error(request, _(driver.setexpresscheckouterror))
                    #request.user.message_set.create(message = _(driver.setexpresscheckouterror))
                return HttpResponseRedirect(error_url)

            # send him/her to the PayPal website to check his/her order details out
            redirect_url = driver.paypal_url()
            # For the mobile PayPal checkout, use a normal browser redirect instead of
            # the old AJAX/JSON handoff. The AJAX path was fragile on mobile devices:
            # the Set-Cookie/session update from this response could be missed before
            # the browser left for PayPal, so PayPal sometimes received incomplete
            # amount/address/session details. A direct 302 keeps the server session
            # and PayPal handoff in the normal checkout flow.
            if request.flavour == 'mobile' and request.POST.get('paypal_direct_redirect') == '1':
                 return HttpResponseRedirect(redirect_url)

            if request.flavour == 'mobile':
                 response = simplejson.dumps({'paypal_url':redirect_url})
                 return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')
            return HttpResponseRedirect(redirect_url)

        if postdata['payment_type'] == "Google":
            checkout_audit._audit(request, 'checkout_payment', 'Start the Google checkout payment')

            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)

        if postdata['payment_type'] == "ApplyPromotion":
            code = postdata['promoCode']
            curr = datetime.now()
            promoCodes = Promotion.objects.filter(valid_until__gte=curr).exclude(valid_from__gte=curr)
            valid = False
            exclude_brand = None

            auction = is_auction(request)
            for pcode in promoCodes:
                if pcode.code.lower() == code.lower() and not auction:
                    valid = True
                    promoObj = Promotion.objects.get(code=code)
                    if promoObj.exclude:
                        exclude_brand = promoObj.exclude
                        cart_items = cart.get_cart_items(request)
                        for item in cart_items:
                            if exclude_brand.name == item.product.brand.name:
                                 valid = False

            if valid == True:
                request.session['promotion_code'] = code
                next_page = reverse('payment')
                checkout_audit._audit(request, 'ApplyPromotion', 'The promotion code is applied: ' + code)

                return HttpResponseRedirect(next_page)
            else:
                request.session['promotion_code'] = ''
                request.session['discount'] = 0.0
                if not auction:
                    if exclude_brand:
                       error_message = u'This promotion code can not be applied to a shopping cart with {} products'.format(exclude_brand.name)
                    else:
                       error_message = u'This promotion code is either invalid or has expired. Please enter a valid promotion code'
                else:
                    error_message = u'This promotion code can not be applied toward a deal or clearance purchase'
                checkout_audit._audit(request, 'ApplyPromotion', 'The promotion code ' + code + ' is invalid')

        if postdata['payment_type'] == "GiftCertificate":
            has_gift_certificate = cart.is_giftcertificate_in_cart(request)
            if has_gift_certificate:
                error_message = u'You have gift certificate in your shopping cart. Gift certificates cannot be used to purchase other gift certificates'
            else:
                giftCode = postdata['giftCode']
                try:
                   giftcert = GiftCertificate.objects.get(code = giftCode)
                   if giftcert and (giftcert.balance + giftcert.value_in_cart > 0):
                       request.session['valid_giftcode'] = giftCode
                       next_page = reverse('payment')
                       return HttpResponseRedirect(next_page)
                   else:
                       error_message = u'This code is invalid or has zero balance, please enter a valid gift certificate code'
                except GiftCertificate.DoesNotExist:
                   error_message = u'This gift certificate code is invalid'
                   request.session['valid_giftcode'] = ''

                   tb = traceback.format_exc()
                   error_msg = "{}: {}".format(error_message, tb)
                   subject = "An exception occured applying gift certificate: {}".format(giftCode)
                   admin_emails = [v for k,v in settings.ADMINS]
                   send_mail_async(subject, error_msg, settings.EMAIL_ORDER, admin_emails,fail_silently=False, html='')


    form = CreditCardForm()

    page_title = 'Checkout'

    email = request.session.get('email','')
    phone = request.session.get('phone','')

    shipping_name = request.session.get('shipping_name','')
    shipping_address_1 = request.session.get('shipping_address_1','')
    shipping_address_2 = request.session.get('shipping_address_2','')
    shipping_city = request.session.get('shipping_city','')
    shipping_state = request.session.get('shipping_state','')
    shipping_zip = request.session.get('shipping_zip','')
    shipping_country = request.session.get('shipping_country','')
    #shipping_country_key = request.session.get('shipping_country','')
    #shipping_country_obj = base_country.objects.get(id = shipping_country_key)
    #shipping_country = shipping_country_obj.name_en

    #request.session['shipping_country_code'] = shipping_country_obj.iso2
    #request.session['shipping_country_name'] = shipping_country

    billing_name = request.session.get('billing_name','')
    billing_address_1 = request.session.get('billing_address_1','')
    billing_address_2 = request.session.get('billing_address_2','')
    billing_city = request.session.get('billing_city','')
    billing_state = request.session.get('billing_state','')
    billing_zip = request.session.get('billing_zip','')
    billing_country = request.session.get('billing_country','')
    #billing_country_key = request.session.get('billing_country','')
    #billing_country_obj = base_country.objects.get(id = billing_country_key)
    #billing_country = billing_country_obj.name_en
    #request.session['billing_country_name'] = billing_country



    isItGift = request.session.get('isItGift','')
    pricePrinted = request.session.get('pricePrinted','')
    giftmessage = request.session.get('giftmessage','')

    haveNote = request.session.get('haveNote','')
    note = request.session.get('note','')


    if is_auction(request):
         promotion_code = ''
    else:
         promotion_code = request.session.get('promotion_code','')

    isItReferral = request.session.get('isItReferral','')
    referralCode = request.session.get('referralCode','')

    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)

    shipping_method_name = request.session.get('shippingLevel','')
    shippingmethod = ShippingMethod.objects.filter(name=shipping_method_name).first()
    if shippingmethod is None:
        # Production-safe guard: the mobile shipping form can arrive without the
        # expected shippingLevel value if a browser/privacy setting or middleware
        # interferes with the POST. Previously this raised IndexError and caused
        # a 500/blank page. Send the customer back to shipping selection and log
        # enough context for debugging.
        checkout_audit._audit(request, 'checkout_payment', 'Invalid or missing shippingLevel in session: {}'.format(shipping_method_name))
        try:
            subject = 'Checkout error: missing/invalid shipping method'
            message = 'Path: {}\nSession shippingLevel: {}\nPOST: {}\nUser-Agent: {}\nIP: {}'.format(
                request.path,
                shipping_method_name,
                dict(request.POST),
                request.META.get('HTTP_USER_AGENT', ''),
                request.META.get('HTTP_X_FORWARDED_FOR') or request.META.get('REMOTE_ADDR', ''),
            )
            admin_emails = [v for k, v in settings.ADMINS]
            send_mail_async(subject, message, settings.SERVER_EMAIL, admin_emails, fail_silently=True, html='')
        except Exception:
            pass
        messages.error(request, 'Please select a shipping method before continuing to payment.')
        return HttpResponseRedirect(reverse('shipping_method'))

    shipping_charge = cart.shipping_charge(request)
    shipping_description = shippingmethod.description

    request.session['shipping_charge'] = str(shipping_charge)
    request.session['shipping_desc'] = shipping_description


    discount = 0.0
    description = ''
    if promotion_code != '':
      try:
        promotion = Promotion.objects.get(code=promotion_code)
        curr = datetime.now()
        promoCodes = Promotion.objects.filter(valid_until__gte=curr).exclude(valid_from__gte=curr)
        if promotion not in promoCodes:
            checkout_audit._audit(request, 'checkout_payment', 'The cached promotion code has expired: ' + promotion_code)
            error_message = u'The cached promotion code has expired'

        else:
            description = promotion.description
            if (promotion.minimum_price < cart_subtotal) and (promotion.discount_amount != 0):
                try:
                    pop = promotion.productonlypromotion
                    discount = cart.cart_productonlypromotion(request, pop, cart_subtotal)
                except ProductOnlyPromotion.DoesNotExist:
                    discount = promotion.discount_amount
            else:
                if (promotion.minimum_price < cart_subtotal) and (promotion.discount_percentage != 0.0):
                    try:
                       pop = promotion.productonlypromotion
                       discount = cart.cart_productonlypromotion(request, pop, cart_subtotal)

                    except ProductOnlyPromotion.DoesNotExist:
                       cart_subtotal_4_nonsale = cart.cart_subtotal_4_nonsale(request)
                       discount = cart_subtotal_4_nonsale * promotion.discount_percentage
            checkout_audit._audit(request, 'checkout_payment', 'Promotion Amount: ' + str(discount))
      except Promotion.DoesNotExist:
         checkout_audit._audit(request, 'checkout_payment', 'The cached promotion code no longer exists: ' + promotion_code)




    total_amt_due = Decimal(cart_subtotal) + Decimal(shipping_charge) - Decimal(discount)
    total_amt_due = total_amt_due.quantize(Decimal(".01"), rounding = ROUND_UP)

    valid_giftcode = request.session.get('valid_giftcode','')
    gift_discount = 0.0
    if valid_giftcode != '':
        giftcert = GiftCertificate.objects.filter(code = valid_giftcode)[0]
        if giftcert:
            giftcert.balance += giftcert.value_in_cart
            giftcert.value_in_cart = 0
            if giftcert.balance >= total_amt_due:
               gift_discount = total_amt_due
            else:
               gift_discount = giftcert.balance
            giftcert.value_in_cart = gift_discount
            giftcert.balance -= gift_discount
            giftcert.save()

    request.session['gift_discount'] = str(gift_discount)


    total_amt_due -= Decimal(gift_discount)
    if is_auction(request):
        total_amt_due = Decimal(get_auction_price(request)) + Decimal(shipping_charge)


    request.session['total_amt_due'] = str(total_amt_due)
    request.session['discount'] = str(discount)
    request.session['promotion_code'] = promotion_code
    request.session['promotion_desc'] = description

    has_gift_certificate = cart.is_giftcertificate_in_cart(request) or (gift_discount != 0.0)


    # the following is for paypal

    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    merchant_id = settings.GOOGLE_CHECKOUT_MERCHANT_ID

    if request.flavour == 'mobile':
         template_name = 'mobile/home/payment.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)

    return render(request, template_name, locals())

def checkout_paypal(request, template_name='checkout/paypal/setcheckout.html'):
    """ page to start the paypal process """

    amount = request.session.get('total_amt_due', 'error in Total amount due, please go back to shopping cart and check')

    return render(request, template_name, locals())

def paypal_success_page(request):
    """ if the POST to the payment gateway successfully billed the customer, create a new order
    containing each CartItem instance, save the order with the transaction ID from the gateway,
    and empty the shopping cart

    """

    checkout_audit._audit(request, 'paypal_success_page', "About to create an order")
    order = Order()

    order.email = request.session.get('email','')
    order.phone = request.session.get('phone','')

    #shipping information
    order.shipping_name = request.session.get('shipping_name','')
    order.shipping_address_1 = request.session.get('shipping_address_1','')
    order.shipping_address_2 = request.session.get('shipping_address_2','')
    order.shipping_city = request.session.get('shipping_city','')
    order.shipping_state = request.session.get('shipping_state','')
    order.shipping_country = request.session.get('shipping_country','')

    #shipping_country_key = request.session.get('shipping_country','')
    #order.shipping_country = base_country.objects.get(id = shipping_country_key)

    order.shipping_zip = request.session.get('shipping_zip','')

    #billing information
    order.billing_name = request.session.get('billing_name','')
    order.billing_address_1 = request.session.get('billing_address_1','')
    order.billing_address_2 = request.session.get('billing_address_2','')
    order.billing_city = request.session.get('billing_city','')
    order.billing_state = request.session.get('billing_state','')
    order.billing_country = request.session.get('billing_country','')

    #billing_country_key = request.session.get('billing_country','')
    #order.billing_country = base_country.objects.get(id = billing_country_key)

    order.billing_zip = request.session.get('billing_zip','')

    order.status = Order.SUBMITTED
    order.transaction_id = 'Paid by Paypal'

    order.ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if not order.ip_address:
        order.ip_address = request.META.get('REMOTE_ADDR')
    if not order.ip_address:
        order.ip_address = '127.0.0.1'

    order.user = User.objects.get(username='anonymous')
    if request.user.is_authenticated:
        order.user = request.user


    #gift information
    order.isItGift = request.session.get('isItGift','')
    order.pricePrinted = request.session.get('pricePrinted','')
    order.giftmessage = request.session.get('giftmessage','')

    order.isItAuction = is_auction(request)
    if order.isItAuction:
         order.auction_price = Decimal(get_auction_price(request))

    try:
        shippingmethod = ShippingMethod.objects.get(name=request.session.get('shippingLevel',''))
    except:
        shippingmethod = None
    try:
        promotion = Promotion.objects.get(code=request.session.get('promotion_code',''))
    except:
        promotion = None

    order.shipping_method = shippingmethod
    order.promotion = promotion
    order.shipping_charged = request.session.get('shipping_charge','')

    order.save()
    checkout_audit._audit(request, 'paypal_success_page', "Order saved, details to be created")


    save_order_details(request, order)
    checkout_audit._audit(request, 'paypal_success_page', "Order details created")

    request.session['order_number'] = order.id

    receipt_url = reverse('checkout_receipt')
    if request.flavour == 'mobile':
         receipt_url = reverse('checkout_receipt_mobile')
    return HttpResponseRedirect(receipt_url)

def paypal_cancel_page(request):
    return HttpResponse("You have cancelled your PayPal Payment Process")

def paypal_error_page(request,template = "checkout/paypal/paypalerror.html"):

    paypal_error = request.session.get('paypal_error', 'No error message returned, contact customer service for more information')
    if request.flavour == 'mobile':
         template = 'mobile/home/paypal/paypalerror.html'
         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)
    return render(request, template, locals())




def show_checkout(request, template_name='checkout/checkout.html'):
    """ checkout form page to collect user shipping and billing information """
    if cart.is_empty(request):
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            response = checkout.process(request)
            order_number = response.get('order_number',0)
            error_message = response.get('message','')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)
        else:
            error_message = u'Correct the errors below'
    else:
        if request.user.is_authenticated:
            user_profile = profile.retrieve(request)
            form = CheckoutForm(instance=user_profile)
        else:
            form = CheckoutForm()
    page_title = 'Checkout'
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)

    return render(request, template_name, locals())

def receipt(request, template_name='checkout/receipt.html'):
    """ page displayed with order information after an order has been placed successfully """
    request.session['promotion_code'] = ''

    total_amt_due = request.session.get('total_amt_due', None)
    promotion_code = request.session.get('promotion_code', None)
    promotion_desc = request.session.get('promotion_desc', None)
    discount = request.session.get('discount', None)
    shipping = request.session.get('shippingLevel', None)
    shipping_charge = request.session.get('shipping_charge', None)
    shipping_desc = request.session.get('shipping_desc', None)

    if not total_amt_due:
        home_url = reverse('home')
        return HttpResponseRedirect(home_url)

    # we use the auction_price to persist the actual final price minus shipping,
    # this is for the generation of the invoice
    effective_final = Decimal(total_amt_due) - Decimal(shipping_charge)

    order_number = request.session.get('order_number','')
    if order_number:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
    else:
        cart_url = reverse('show_cart')
        return HttpResponseRedirect(cart_url)

    order_number = order.invoice_number

    if not order_number:
        now = datetime.now( )
        scramble_order_id = order.id + random.randint(1,10)
        order_number = str(now.year) + str(now.month) + str(now.day) + '-' + str(scramble_order_id) +'-' + str(random.randint(1,1000000))
        if request.flavour == "mobile":
             order_number = "M{}".format(order_number)

        order.invoice_number = order_number

        order.note = request.session.get('note', '')

        order.isItAuction = is_auction(request)
        #if order.isItAuction:
        #    order.auction_price = Decimal(get_auction_price(request))
        order.auction_price = effective_final

        order.save()

        if is_auction(request):
            Auction_Paid(request)



        subject = "Your order with " + settings.SITE_NAME + " " + order_number
        dst_email = request.session.get('email', None)
        src_email = settings.EMAIL_ORDER

        checkout_audit._audit(request, 'Receipt', 'Preparing Order receipt')

        try:
            email_msg = "Greetings, \n\n"

            email_msg += "You have successfully placed an order with order number: "
            email_msg += str(order_number)
            email_msg += "\n\nYour order will be processed within one business day. Thank you for your business. "
            email_msg += "\n\n" + settings.SITE_NAME + " Sales Team\n\n"

            email_msg += "Attached is your invoice. To open the invoice, you need Adobe Reader installed. Adobe Reader is "
            email_msg += "a free software that lets you view and print PDF files. If you do not have Adobe Reader on your computer, you can download it at:\n\n"
            email_msg += "http://get.adobe.com/reader/"

            pdf = generate_invoice(order)
            #email.send_pdf(subject, email_msg, src_email, dst_email, pdf, order_number)
            EmailMsg = EmailMessage(subject,email_msg,src_email,[dst_email, EMAIL_ORDER],headers={'Reply-To':src_email})
            #EmailMsg.content_subtype = "html"
            EmailMsg.attach(str(order_number) + '.pdf',pdf,'application/pdf')
            EmailMsg.send()
        except:
            tb = traceback.format_exc()
            checkout_audit._audit(request, "Generating Receipt Error:"," {}".format(tb))
            error_msg = "Generating Receipt Error: {}".format(tb)
            subject = "An exception occured during check out"
            admin_emails = [v for k,v in settings.ADMINS]
            send_mail_async(subject, error_msg, settings.EMAIL_ORDER, admin_emails,fail_silently=False, html='')


            email_msg = "Greetings, \n\n"

            email_msg += "You have successfully placed an order with order number: "
            email_msg += str(order_number)
            email_msg += ". Please login to your account on " + settings.SITE_URL + " to check the order detail, shipping status and view your invoice."
            email_msg += " If you do not have an account with us, you may write to us with your order number to request a copy of the invoice."
            email.send_email(dst_email, src_email, subject, email_msg)

        checkout_audit._audit(request, 'Receipt', 'Order receipt sent')

        #message = EmailMessage(subject, email_msg, src_email, [dst_email])
        #message.attach('invoice.pdf', pdf_invoice, 'application/pdf')
        #message.send()



        referralCode = request.session.get('referralCode','')
        if referralCode:
            referrals = referral.objects.filter(referralCode=referralCode)
            if referrals:
               referralObj = referrals[0]
               referral_email = referralObj.email
               referralObj.orders.add(order);
               referralObj.save()
               email_msg = "Thank you for your referral for order " + order_number
               email.send_email(referral_email, src_email, "Order referral", email_msg)
               checkout_audit._audit(request, 'Receipt', 'this order was referred by ' + referral_email)



    valid_giftcode = request.session.get('valid_giftcode','')
    if valid_giftcode != '':
        giftcert = GiftCertificate.objects.filter(code = valid_giftcode)[0]
        if giftcert:
            gift_discount = giftcert.value_in_cart
            giftcert.value_in_cart = 0
            giftcert.orders_redeemed.add(order)
            giftcert.save()



    if request.flavour == 'mobile':
         template_name = 'mobile/home/receipt.html'
         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)

    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    return render(request, template_name, locals())

from django.http.response import HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from ecomstore.cart.cart import CART_ID_SESSION_KEY


def _stripe_audit(request, stage, message, status='Success'):
    try:
        checkout_audit._audit(request, stage, message)
    except Exception:
        # Auditing must never interrupt checkout/payment recovery.
        pass


def _safe_json_dumps(value):
    return json.dumps(value, default=str)


def _session_snapshot(request):
    """Return a JSON-safe copy of the current checkout session."""
    snapshot = {}
    for key, value in request.session.items():
        try:
            json.dumps(value)
            snapshot[key] = value
        except TypeError:
            snapshot[key] = str(value)
    return snapshot


def _get_request_ip(request):
    forwarded = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if forwarded:
        return forwarded.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', '127.0.0.1')


def _get_request_flavour(request):
    return getattr(request, 'flavour', '') or request.session.get('flavour', '') or 'full'


def _build_payment_attempt(request, amount, currency):
    session_data = _session_snapshot(request)
    user = request.user if getattr(request, 'user', None) and request.user.is_authenticated else None
    return StripePaymentAttempt.objects.create(
        cart_id=request.session.get(CART_ID_SESSION_KEY, ''),
        user=user,
        amount=int(amount),
        currency=(currency or 'usd').lower(),
        email=request.session.get('email', ''),
        ip_address=_get_request_ip(request),
        flavour=_get_request_flavour(request),
        session_data=_safe_json_dumps(session_data),
        status=StripePaymentAttempt.STATUS_CREATED,
    )


def _request_from_attempt(attempt):
    session_data = {}
    if attempt.session_data:
        try:
            session_data = json.loads(attempt.session_data)
        except Exception:
            session_data = {}
    if attempt.cart_id and not session_data.get(CART_ID_SESSION_KEY):
        session_data[CART_ID_SESSION_KEY] = attempt.cart_id

    post = QueryDict('', mutable=True)
    user = attempt.user or AnonymousUser()
    meta = {'REMOTE_ADDR': attempt.ip_address or '127.0.0.1'}
    return SimpleNamespace(session=session_data, POST=post, META=meta, user=user, flavour=attempt.flavour or 'full')


def _get_attempt_for_payment_intent(payment_intent):
    attempt = None
    pi_id = payment_intent.get('id') if isinstance(payment_intent, dict) else payment_intent.id
    metadata = payment_intent.get('metadata', {}) if isinstance(payment_intent, dict) else getattr(payment_intent, 'metadata', {})
    attempt_id = None
    try:
        attempt_id = metadata.get('stripe_payment_attempt_id')
    except Exception:
        attempt_id = None

    if attempt_id:
        attempt = StripePaymentAttempt.objects.filter(id=attempt_id).first()
    if not attempt:
        attempt = StripePaymentAttempt.objects.filter(payment_intent_id=pi_id).first()
    return attempt


def _generate_invoice_number_for_order(request, order):
    now = datetime.now()
    scramble_order_id = order.id + random.randint(1, 10)
    order_number = str(now.year) + str(now.month) + str(now.day) + '-' + str(scramble_order_id) + '-' + str(random.randint(1, 1000000))
    if getattr(request, 'flavour', '') == 'mobile':
        order_number = "M{}".format(order_number)
    return order_number


def _finalize_paid_order(request, order):
    """Generate invoice number and send receipt email once.

    The normal receipt page still displays the order.  This helper makes the
    webhook path complete the order without requiring the customer's browser to
    come back successfully.
    """
    if order.invoice_number:
        return order

    total_amt_due = request.session.get('total_amt_due', None)
    shipping_charge = request.session.get('shipping_charge', '0')
    try:
        effective_final = Decimal(total_amt_due) - Decimal(shipping_charge)
    except Exception:
        effective_final = order.total

    order_number = _generate_invoice_number_for_order(request, order)
    order.invoice_number = order_number
    order.note = request.session.get('note', '')
    order.isItAuction = is_auction(request)
    order.auction_price = effective_final
    order.save()

    if is_auction(request):
        try:
            Auction_Paid(request)
        except Exception:
            checkout_audit._audit(request, 'Stripe webhook', 'Auction_Paid failed for order {}'.format(order.id))

    subject = "Your order with " + settings.SITE_NAME + " " + order_number
    dst_email = request.session.get('email', None) or order.email
    src_email = settings.EMAIL_ORDER

    try:
        email_msg = "Greetings, \n\n"
        email_msg += "You have successfully placed an order with order number: "
        email_msg += str(order_number)
        email_msg += "\n\nYour order will be processed within one business day. Thank you for your business. "
        email_msg += "\n\n" + settings.SITE_NAME + " Sales Team\n\n"
        email_msg += "Attached is your invoice. To open the invoice, you need Adobe Reader installed. Adobe Reader is "
        email_msg += "a free software that lets you view and print PDF files. If you do not have Adobe Reader on your computer, you can download it at:\n\n"
        email_msg += "http://get.adobe.com/reader/"

        pdf = generate_invoice(order)
        EmailMsg = EmailMessage(subject, email_msg, src_email, [dst_email, EMAIL_ORDER], headers={'Reply-To': src_email})
        EmailMsg.attach(str(order_number) + '.pdf', pdf, 'application/pdf')
        EmailMsg.send()
    except Exception:
        tb = traceback.format_exc()
        checkout_audit._audit(request, "Stripe receipt error", " {}".format(tb))
        error_msg = "Generating Stripe receipt error: {}".format(tb)
        admin_emails = [v for k, v in settings.ADMINS]
        send_mail_async("An exception occured during Stripe check out", error_msg, settings.EMAIL_ORDER, admin_emails, fail_silently=False, html='')

        fallback_msg = "Greetings, \n\n"
        fallback_msg += "You have successfully placed an order with order number: "
        fallback_msg += str(order_number)
        fallback_msg += ". Please login to your account on " + settings.SITE_URL + " to check the order detail, shipping status and view your invoice."
        fallback_msg += " If you do not have an account with us, you may write to us with your order number to request a copy of the invoice."
        email.send_email(dst_email, src_email, subject, fallback_msg)

    try:
        referralCode = request.session.get('referralCode', '')
        if referralCode:
            referrals = referral.objects.filter(referralCode=referralCode)
            if referrals:
                referralObj = referrals[0]
                referral_email = referralObj.email
                referralObj.orders.add(order)
                referralObj.save()
                email.send_email(referral_email, src_email, "Order referral", "Thank you for your referral for order " + order_number)
    except Exception:
        checkout_audit._audit(request, 'Stripe receipt', 'Referral handling failed for order {}'.format(order.id))

    try:
        valid_giftcode = request.session.get('valid_giftcode', '')
        if valid_giftcode != '':
            giftcert = GiftCertificate.objects.filter(code=valid_giftcode)[0]
            if giftcert:
                giftcert.value_in_cart = 0
                giftcert.orders_redeemed.add(order)
                giftcert.save()
    except Exception:
        checkout_audit._audit(request, 'Stripe receipt', 'Gift certificate handling failed for order {}'.format(order.id))

    checkout_audit._audit(request, 'Stripe receipt', 'Order receipt sent for order {}'.format(order.id))
    return order


def _complete_stripe_payment_intent(payment_intent_id, request=None, source='browser'):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
    if payment_intent.status != 'succeeded':
        return None, 'Stripe PaymentIntent {} is {}'.format(payment_intent_id, payment_intent.status)

    existing_order = Order.objects.filter(transaction_id=payment_intent_id).first()
    attempt = _get_attempt_for_payment_intent(payment_intent)

    if existing_order:
        if attempt and not attempt.order_id:
            attempt.order = existing_order
            attempt.status = StripePaymentAttempt.STATUS_COMPLETED
            attempt.save(update_fields=['order', 'status', 'updated_at'])
        return existing_order, None

    if not attempt and request is not None:
        attempt = _build_payment_attempt(request, payment_intent.amount, payment_intent.currency)
        attempt.payment_intent_id = payment_intent_id
        attempt.status = StripePaymentAttempt.STATUS_SUCCEEDED
        attempt.save()

    if not attempt:
        return None, 'No StripePaymentAttempt found for {}'.format(payment_intent_id)

    payment_request = request or _request_from_attempt(attempt)

    try:
        order = checkout.create_order(payment_request, payment_intent_id)
        _finalize_paid_order(payment_request, order)
        attempt.order = order
        attempt.status = StripePaymentAttempt.STATUS_COMPLETED
        attempt.error_message = ''
        attempt.save(update_fields=['order', 'status', 'error_message', 'updated_at'])
        return order, None
    except Exception:
        tb = traceback.format_exc()
        attempt.status = StripePaymentAttempt.STATUS_FAILED
        attempt.error_message = tb
        attempt.save(update_fields=['status', 'error_message', 'updated_at'])
        admin_emails = [v for k, v in settings.ADMINS]
        send_mail_async(
            "Stripe payment succeeded but order creation failed",
            "PaymentIntent: {}\nSource: {}\n\n{}".format(payment_intent_id, source, tb),
            settings.EMAIL_ORDER,
            admin_emails,
            fail_silently=False,
            html='',
        )
        return None, tb


# below are for Stripe integration
@csrf_exempt
def createpayment(request):
      stripe.api_key = settings.STRIPE_SECRET_KEY

      data = json.loads(request.body)
      amount = int(data['total'])
      currency = data.get('currency', 'usd')
      attempt = _build_payment_attempt(request, amount, currency)

      try:
          intent = stripe.PaymentIntent.create(
              amount=amount,
              currency=currency,
              receipt_email=request.session.get('email', None) or None,
              metadata={
                  'stripe_payment_attempt_id': str(attempt.id),
                  'cart_id': request.session.get(CART_ID_SESSION_KEY, ''),
                  'email': request.session.get('email', ''),
              },
          )
          attempt.payment_intent_id = intent.id
          attempt.save(update_fields=['payment_intent_id', 'updated_at'])

          if 'shipping_zip' in request.session:
              zip = request.session['shipping_zip']
          else:
              zip = "00000"
          checkout_audit._audit(request, 'stripe_createpayment', 'User:{}, Cart ID:{}, Zip:{}, Attempt:{}, Payload:{}'.format(request.user, request.session.get(CART_ID_SESSION_KEY,''), zip, attempt.id, data))
          return JsonResponse({
              'publishableKey': settings.STRIPE_PUBLISHABLE_KEY,
              'hidePostalCodeInput': settings.STRIPE_HIDE_POSTALCODE_INPUT,
              'shippingPostalCode': zip,
              'receipt_email': request.session.get('email', None) or settings.RECEIPT_EMAIL,
              'clientSecret': intent.client_secret,
          })
      except Exception as e:
          attempt.status = StripePaymentAttempt.STATUS_FAILED
          attempt.error_message = traceback.format_exc()
          attempt.save(update_fields=['status', 'error_message', 'updated_at'])
          print ("********* Error: ", str(e))
          return JsonResponse({'error':str(e)}, status=403)


@csrf_exempt
def paymentcomplete(request):
  if request.method == "POST":
    try:
        data = json.loads(request.POST.get("payload"))
    except Exception:
        checkout_audit._audit(request, 'stripe_paymentcomplete_failed', 'Invalid payload: {}'.format(request.POST.get("payload")))
        return HttpResponse("Invalid Stripe payment payload", status=400)

    checkout_audit._audit(request, 'stripe_paymentcomplete', 'User:{}, Cart ID:{}, Payload:{}'.format(request.user, request.session.get(CART_ID_SESSION_KEY,''), data))

    payment_intent_id = data.get('id')
    if not payment_intent_id:
        return HttpResponse("Missing Stripe payment id", status=400)

    order, error = _complete_stripe_payment_intent(payment_intent_id, request=request, source='browser')
    if order:
        request.session['order_number'] = order.id
        receipt_url = reverse('checkout_receipt_mobile') if getattr(request, 'flavour', '') == 'mobile' else reverse('checkout_receipt')
        return HttpResponseRedirect(receipt_url)

    checkout_audit._audit(request, 'checkout_stripe_payment failed', error or payment_intent_id)
    return HttpResponse("Payment was received, but order creation is pending. Please contact customer service with payment id {}.".format(payment_intent_id), status=202)

  return HttpResponse("Method not allowed", status=405)


@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    webhook_secret = getattr(settings, 'STRIPE_WEBHOOK_SECRET', '')
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE', '')

    if not webhook_secret:
        return HttpResponse("STRIPE_WEBHOOK_SECRET is not configured", status=400)

    try:
        event = stripe.Webhook.construct_event(payload, sig_header, webhook_secret)
    except ValueError:
        return HttpResponse("Invalid payload", status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse("Invalid signature", status=400)

    event_type = event.get('type')
    payment_intent = event.get('data', {}).get('object', {})
    payment_intent_id = payment_intent.get('id')

    if event_type == 'payment_intent.succeeded' and payment_intent_id:
        order, error = _complete_stripe_payment_intent(payment_intent_id, request=None, source='webhook')
        if error:
            # Return 200 so Stripe does not endlessly retry for problems that
            # need manual/admin attention; the attempt is marked failed and an
            # admin email is sent by _complete_stripe_payment_intent().
            return JsonResponse({'received': True, 'order_created': False, 'error': error})
        return JsonResponse({'received': True, 'order_created': True, 'order_id': order.id})

    if event_type == 'payment_intent.payment_failed' and payment_intent_id:
        attempt = _get_attempt_for_payment_intent(payment_intent)
        if attempt:
            attempt.status = StripePaymentAttempt.STATUS_FAILED
            attempt.error_message = json.dumps(payment_intent.get('last_payment_error', {}), default=str)
            attempt.save(update_fields=['status', 'error_message', 'updated_at'])

    return JsonResponse({'received': True})

@csrf_exempt
def makeapayment(request, template_name='checkout/payment_standalone.html'):
    """ make a standalone payment to Stripe """


    page_title = 'Send a Payment'

    return render(request, template_name, locals())

@csrf_exempt
def makeapaymentcomplete(request):
  print ("request method = ", request.method)
  if request.method=="POST":
    print ("POST = ", request.POST)
    """
    if data["status"] == "succeeded":
        checkout_audit._audit(request, 'make_a_payment:', request.POST.get("payload"))

        order = checkout.create_order(request, data['id'])

    else:
        checkout_audit._audit(request, 'make_a_payment: failed, id = :', data['id'])
    """
