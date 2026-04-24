# -*- coding: utf-8 -*-

from decimal import Decimal, ROUND_UP
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext
from django.utils.translation import gettext as _
from ecomstore.paypal_driver.driver import PayPal
from ecomstore.paypal_driver.models import PayPalResponse
from ecomstore.paypal_driver.utils import process_payment_request, \
    process_refund_request

from ecomstore.cart import cart
from ecomstore.utils import checkout_audit

from django.contrib import messages
from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME
from ecomstore.catalog.models import Product, Brand, Category


def setcheckout(request, return_url, cancel_url, error_url, template = "checout/paypal/setcheckout.html", currency = "USD"):
    """
    This method is not used in aimkon. It is incorporated into the checkout.views.checkout_payment method

    Django view to process PayPal SetExpressCheckout API call.
    If response 'Success' or 'SuccessWithWarning' comes, redirects user to the PayPal website to continue checkout process.
    If response 'Failed' or 'FailedWithWarning' comes, shows the error and redirects user to the 'payment page' to choose another POS or PayPal again.
    """
    
    #############################################################################
    # ROUTINES                                                                  #
    # 1) Perform and validate POST data                                         #
    # 2) Call Paypal driver                                                     #
    # 3) Execute the relevant method                                            #
    # 4) Accroding to the method response, redirect user to the given urls      #
    #############################################################################
    #print return_url
    if request.POST:
        # normalize the given amount
        amount = request.POST.get("amount")
        try:
            amount = Decimal(amount)
            amount = str(amount.quantize(Decimal(".01"), rounding = ROUND_UP))
        except:
            if request.user.is_authenticated:
                message = _("No given valid amount. Please check the amount that will be charged.")
                messages.error(request, message)
                #request.user.message_set.create(message = _("No given valid amount. Please check the amount that will be charged."))
            return HttpResponseRedirect(error_url)
        
        num_cart_items = request.POST.get('num_cart_items', None)
        cart_items = None
        if num_cart_items:
            cart_items = []
            for i in range(0, int(num_cart_items)):
                item = {
                    'NAME':   request.POST.get('cart_items[%s][NAME]' % i),
                    'NUMBER': request.POST.get('cart_items[%s][NUMBER]' % i),
                    'DESC':   request.POST.get('cart_items[%s][DESC]' % i),
                    'AMT':    request.POST.get('cart_items[%s][AMT]' % i),
                    'QTY':    request.POST.get('cart_items[%s][QTY]' % i)
                }
                cart_items.append(item)

        # call the PayPal driver (2)
        driver = PayPal()
        # call the relevant API method (3)
        result = driver.SetExpressCheckout(amount, currency, return_url, cancel_url, cart_items)
        #print driver.apierror
        # perform the response (4)
        if not result:
            #print driver.apierror
            # show the error message (comes from PayPal API) to the user and redirect him/her to the error page
            if request.user.is_authenticated:
                message = _(driver.setexpresscheckouterror)
                messages.error(request, message)
                #request.user.message_set.create(message = _(driver.setexpresscheckouterror))
            return HttpResponseRedirect(error_url)
        
        # send him/her to the PayPal website to check his/her order details out
        redirect_url = driver.paypal_url()
        return HttpResponseRedirect(redirect_url)
    
    amount = request.session.get('paypal_total_amt', 'error in Total amount due, please go back to shopping cart and check')
    #print amount
    promotion_code = request.session.get('promotion_code','')

    cart_items = cart.get_cart_items(request)
    cart_subtotal = cart.cart_subtotal(request)

    checkout_audit._audit(request, 'paypal_setcheckout', result)
    return render(request, template,locals())


def docheckout(request, error_url, success_url, template = "checkout/paypal/docheckout.html", currency = "USD"):
    """
    Django view to do the actual payment (charges actual money)
    It performs the relevant API method DoExpressCheckoutPayment
    """

    if request.POST:
        # normalize the given amount
        amount = request.POST.get("amount")
        try:
            amount = Decimal(amount)
            amount = str(amount.quantize(Decimal(".01"), rounding = ROUND_UP))
        except:
            if request.user.is_authenticated:
                message = _("No given valid amount. Please check the amount that will be charged.")
                messages.error(request, message)
                #request.user.message_set.create(message = _("No given valid amount. Please check the amount that will be charged."))
            checkout_audit._audit(request, 'paypal_docheckout', "No given valid amount. Please check the amount that will be charged.", 'Error')
            return HttpResponseRedirect(error_url)

        # perform GET
        token   = request.GET.get("token")
        payerid = request.GET.get("PayerID")

        if not token:
             from urllib.parse import urlparse, parse_qsl
             iurl = request.POST.get("fullpath")
             qs =  dict(parse_qsl(urlparse(iurl).query))
             token = qs['token']
             payerid = qs['PayerID']
        paypal_token = "amount={}, token={}, payerid={}".format(amount, token, payerid)
        checkout_audit._audit(request, 'paypal_docheckout: ',paypal_token, request.flavour)
        # charge from PayPal
        result, response = process_payment_request(request, amount, currency, token, payerid)
        # process the result
        if not result:
            # show the error message (comes from PayPal API) and redirect user to the error page
            message = _("Amount {} has not been charged, the paypal error message is {}, raw message: {}".format(amount, response.error_msg, response.raw_response))
            if request.user.is_authenticated:
                messages.error(request, message) 
                #request.user.message_set.create(message = _("Amount %s has not been charged, server error is '%s'" % (amount, response.raw_response)))
            checkout_audit._audit(request, 'paypal_docheckout', message, 'Error')
           
            return HttpResponseRedirect(error_url)

        # Now we are gone, redirect user to success page
        if request.user.is_authenticated:
            message = _("Amount %s has been successfully charged, your transaction id is '%s'" % (amount, response.trans_id))
            messages.error(request, message)
            #request.user.message_set.create(message = _("Amount %s has been successfully charged, your transaction id is '%s'" % (amount, response.trans_id)))

        message = _("Amount $%s has been successfully charged, your transaction id is '%s'" % (amount, response.trans_id))
        checkout_audit._audit(request, 'paypal_docheckout', message)
        
        return HttpResponseRedirect(success_url)

    success_url = success_url
    error_url = error_url
    amount = request.session.get('paypal_total_amt', '0.0')
    cart_items = request.session.get('cart_items')
    message = _("Return to %s to submit the amount of %s" % (success_url, amount))
    checkout_audit._audit(request, 'paypal_docheckout', message)

    shipping_name = request.session.get('shipping_name','')
    shipping_address_1 = request.session.get('shipping_address_1','')
    shipping_address_2 = request.session.get('shipping_address_2','')
    shipping_city = request.session.get('shipping_city','')
    shipping_state = request.session.get('shipping_state','')
    shipping_zip = request.session.get('shipping_zip','')
    shipping_country = request.session.get('shipping_country','')
    #shipping_country = request.session.get('shipping_country_name','')

    billing_name = request.session.get('billing_name','')
    billing_address_1 = request.session.get('billing_address_1','')
    billing_address_2 = request.session.get('billing_address_2','')
    billing_city = request.session.get('billing_city','')
    billing_state = request.session.get('billing_state','')
    billing_zip = request.session.get('billing_zip','')
    billing_country = request.session.get('billing_country','')
    #billing_country = request.session.get('billing_country_name','')

    if request.flavour == 'mobile':
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
            template = 'mobile/home/paypal/docheckout.html'

    return render(request, template,locals())



def dorefund(request, error_url, success_url, template = "checkout/paypal/dorefund.html"):
    if request.POST:
        # normalize the given amount
        amount = request.POST.get("amount")
        trans_id = request.POST.get("transactionid")
        try:
            amount = Decimal(amount)
            amount = str(amount.quantize(Decimal(".01"), rounding = ROUND_UP))
        except:
            if request.user.is_authenticated:
                message = _("No given valid amount. Please check the amount that will be charged.")
                messages.error(request, message)
                #request.user.message_set.create(message = _("No given valid amount. Please check the amount that will be charged."))
            return HttpResponseRedirect(error_url)
        
        response_obj = get_object_or_404(PayPalResponse, trans_id = trans_id)
        
        # charge from PayPal
        result, response = process_refund_request(response_obj, amount)
        # process the result
        if not result:
            # show the error message (comes from PayPal API) and redirect user to the error page
            if request.user.is_authenticated:
                message = _("Amount {} has not been charged, server error is '{}'".format(amount, response.error)) 
                messages.error(request, message)
                #request.user.message_set.create(message = _("Amount %s has not been charged, server error is '%s'" % (amount, response.error)))
            return HttpResponseRedirect(error_url)
        
        # Now we are gone, redirect user to success page
        if request.user.is_authenticated:
                message = _("Amount %s has been successfully refunded, your transaction id is '%s'" % (amount, response.trans_id))
                messages.error(request, message)
                #request.user.message_set.create(message = _("Amount %s has been successfully refunded, your transaction id is '%s'" % (amount, response.trans_id)))
        
        return HttpResponseRedirect(success_url)

    return render(request, template,
                              {'error_url': error_url,
                               'success_url': success_url,
                               }, )


