# -*- coding: utf-8 -*-

##################################################################################################
# Pluggable iParcel NVP (Name Value Pair) API implementation for Django.                          #
# This file includes the iParcel driver class that maps NVP API methods to such simple functions. #
#                                                                                                #
# Feel free to distribute, modify or use any open or closed project without any permission.      #
#                                                                                                #
# Author: Ozgur Vatansever                                                                       #
# Email: ozgurvt@gmail.com                                                                       #
##################################################################################################


import urllib, urllib2, datetime
from cgi import parse_qs
from decimal import Decimal, ROUND_UP
from ecomstore.utils import checkout_audit
import traceback
from ecomstore.utils.email import send_mail_async
from django.utils.encoding import smart_str, smart_unicode
from ecomstore.cart import cart

try:
    from django.conf import settings
except:
    pass

# Exception messages
TOKEN_NOT_FOUND_ERROR = "iParcel error occured. There is no TOKEN info to finish performing iParcel payment process. We haven't charged your money yet."
NO_PAYERID_ERROR = "iParcel error occured. There is no PAYERID info to finish performing iParcel payment process. We haven't charged your money yet."
GENERIC_PAYPAL_ERROR = "There occured an error while performing iParcel checkout process. We apologize for the inconvenience. We haven't charged your money yet."
GENERIC_PAYMENT_ERROR = "Transaction failed. Check out your order details again."
GENERIC_REFUND_ERROR = "An error occured, we can not perform your refund request"

class iParcel(object):
    """
    Pluggable Python iParcel Driver that implements NVP (Name Value Pair) API methods.
    There are simply 3 main methods to be executed in order to finish the iParcel payment process.
    You explicitly need to define iParcel username, password and signature in your project's settings file.

    Those are:
    1) SetExpressCheckout
    2) GetExpressCheckoutDetails (optional)
    3) DoExpressCheckoutPayment
    """
    def __init__(self, debug = False):
        # iParcel Credientials
        #self.private_key  = getattr(settings, "UPS_iParcel_Private_Key", None)
        #self.public_key  = getattr(settings, "UPS_iParcel_Public_Key", None)
        self.private_key  = 'e96e38ef-b9cd-4838-beba-8a45d71347dc'
        self.public_key  = '66bfb15d-67db-4747-a00e-04a2efc6a390'

        # Second step is to set the API end point and redirect urls correctly.
        self.iParcel_API_ENDPOINT    = "https://webservices.i-parcel.com/api"
        self.iPARCEL_REDIRECT_URL = "https://pay.i-parcel.com/v1/api/SetCheckout"

        # initialization
        #self.signature = urllib.urlencode(self.credientials) + '&'
        self.setexpresscheckouterror = None
        self.getexpresscheckoutdetailserror = None
        self.doexpresscheckoutpaymenterror = None
        self.refundtransactionerror = None
        self.apierror = None
        self.api_response = None
        self.token = None
        self.response = None
        self.refund_response = None

    def _get_value_from_qs(self, qs, value):
        """
        Gets a value from a querystring dict
        This is a private helper function, so DO NOT call this explicitly.
        """
        raw = qs.get(value)
        if type(raw) == list:
            try:
                return raw[0]
            except KeyError:
                return None
        else:
            return raw


    def iparcel_url(self, token = None):
        """
        Returns a 'redirect url' for iParcel payments.
        If token was null, this function MUST NOT return any URL.
        """
        token = token if token is not None else self.token
        if not token:
            return None
        #return self.iPARCEL_REDIRECT_URL + token
        return "https://pay.i-parcel.com/v1/Cart?key={}&tx={}".format(self.private_key, token)


    def GetQuote(self, request):
	from django.template.loader import render_to_string
        url_quote = self.iParcel_API_ENDPOINT + "/Quote"
	key = self.private_key

	print "******* key = ", key

	variables = {}
        template = "checkout/quotetemplate.txt"


	bCity = request.session.get('billing_city','')
	bCountryCode = request.session.get('billing_country','')
	bEmail = request.session.get('email','')
	bFname = request.session.get('billing_name','')
	bLname = request.session.get('billing_name','')
	bPhone = request.session.get('phone','')
	bZipcode = request.session.get('billing_zip','')
	bRegion = ""
	bStreet1 = request.session.get('billing_address_1','')
	bStreet2 = request.session.get('billing_address_2','')

	sCity = request.session.get('billing_city','')
	sCountryCode = request.session.get('billing_country','')
	sEmail = request.session.get('email','')
	sFname = request.session.get('billing_name','')
	sLname = request.session.get('billing_name','')
	sPhone = request.session.get('phone','')
	sZipcode = request.session.get('billing_zip','')
	sRegion = ""
	sStreet1 = request.session.get('billing_address_1','')
	sStreet2 = request.session.get('billing_address_2','')

	sku = "AA-DJHRUF"
	description = "This is a test product"

	htscode = "8513.10.4000"
	countryoforigin = "US"

	height = Decimal('2.00')
	length = Decimal('2.00')
	weight = Decimal('2.00')
	width = Decimal('10.00')

	price = 200
	quantity = 2

	variables.update({'bCity': bCity})
	variables.update({'bCountryCode': bCountryCode})
	variables.update({'bEmail': bEmail})
	variables.update({'bFname': bFname})
	variables.update({'bLname': bLname})
	variables.update({'bPhone': bPhone})
	variables.update({'bZipcode': bZipcode})
	variables.update({'bRegion': bRegion})
	variables.update({'bStreet1': bStreet1})
	variables.update({'bStreet2': bStreet2})

	variables.update({'sCity': sCity})
	variables.update({'sCountryCode': sCountryCode})
	variables.update({'sEmail': sEmail})
	variables.update({'sFname': sFname})
	variables.update({'sLname': sLname})
	variables.update({'sPhone': sPhone})
	variables.update({'sZipcode': sZipcode})
	variables.update({'sRegion': sRegion})
	variables.update({'street1': sStreet1})
	variables.update({'sStreet2': sStreet2})

	variables.update({'height': height})
	variables.update({'length': length})
	variables.update({'weight': weight})
	variables.update({'width': width})
	variables.update({'key': key})
	variables.update({'price': price})
	variables.update({'quantity': quantity})
	variables.update({'htscode': htscode})
	variables.update({'sku': sku})
	variables.update({'description': description})
	variables.update({'countryoforigin': countryoforigin})



        entry = render_to_string(template, variables)
        #entry = entry.replace("&lt;", "<")
        #entry = entry.replace("&gt;", ">")
        #entry = entry.encode('ascii',errors='ignore')

	print entry

	import requests
	headers = {'Content-Type': 'application/xml'}
 	resp = requests.post(url_quote, data=entry, headers=headers)
	print "post response = " + str(resp.status_code) + " " + resp.text

        return 1.0

    def SendiParcelRedirect(self, request):
	from django.template.loader import render_to_string
        url_redirect = self.iPARCEL_REDIRECT_URL
	key = self.private_key

	print "******* key = ", key

	variables = {}
        template = "checkout/iparcel_checkout_sample.txt"


	bCity = request.session.get('billing_city','')
	bCountryCode = request.session.get('billing_country','')
	bEmail = request.session.get('email','')
	bFname = request.session.get('billing_name','')
	bLname = request.session.get('billing_name','')
	bPhone = request.session.get('phone','')
	bZipcode = request.session.get('billing_zip','')
	bRegion = ""
	bStreet1 = request.session.get('billing_address_1','')
	bStreet2 = request.session.get('billing_address_2','')

	sCity = request.session.get('billing_city','')
	sCountryCode = request.session.get('billing_country','')
	sEmail = request.session.get('email','')
	sFname = request.session.get('billing_name','')
	sLname = request.session.get('billing_name','')
	sPhone = request.session.get('phone','')
	sZipcode = request.session.get('billing_zip','')
	sRegion = ""
	sStreet1 = request.session.get('billing_address_1','')
	sStreet2 = request.session.get('billing_address_2','')

	sku = "AA-DJHRUF"
	description = "This is a test product"

	htscode = "8513.10.4000"
	countryoforigin = "US"

	height = Decimal('10.00')
	length = Decimal('10.00')
	weight = Decimal('1.00')
	width = Decimal('10.00')

	price = 12
	quantity = 2

	variables.update({'bCity': bCity})
	variables.update({'bCountryCode': bCountryCode})
	variables.update({'bEmail': bEmail})
	variables.update({'bFname': bFname})
	variables.update({'bLname': bLname})
	variables.update({'bPhone': bPhone})
	variables.update({'bZipcode': bZipcode})
	variables.update({'bRegion': bRegion})
	variables.update({'bStreet1': bStreet1})
	variables.update({'bStreet2': bStreet2})

	variables.update({'sCity': sCity})
	variables.update({'sCountryCode': sCountryCode})
	variables.update({'sEmail': sEmail})
	variables.update({'sFname': sFname})
	variables.update({'sLname': sLname})
	variables.update({'sPhone': sPhone})
	variables.update({'sZipcode': sZipcode})
	variables.update({'sRegion': sRegion})
	variables.update({'street1': sStreet1})
	variables.update({'sStreet2': sStreet2})

	variables.update({'height': height})
	variables.update({'length': length})
	variables.update({'weight': weight})
	variables.update({'width': width})
	variables.update({'key': key})
	variables.update({'price': price})
	variables.update({'quantity': quantity})
	variables.update({'htscode': htscode})
	variables.update({'sku': sku})
	variables.update({'description': description})
	variables.update({'countryoforigin': countryoforigin})

    	import json

    	data = {}
    	data['key'] = key
        data['currency_code'] = "USD"
        data['page_currency'] = "EUR"
        data['discount_amount_cart'] = 0
        data['prepaidamount'] = "0.0000"
        data['reference_number'] = "MERC1234"
        data['return'] = "https:\/\/www.andrew-amanda.com\/return"
        data['shopping_url'] = "https:\/\/www.andrew-amanda.com\/"
        data['cancel_return'] = "https:\/\/www.andrew-amanda.com\/fail"
        data['image_url'] = "http:\/\/www.andrew-amanda.com\/static\/images\/siteImg\/logo_224x70.jpg"

        addressinfo = {}
        billing = {}
        billing['email'] = "sales@andrew-amanda.com"
        billing['first_name'] = "Andrew"
        billing['last_name'] = "Everett"
        billing['address1'] = "31 Reindeer Road"
        billing['address2'] = "Cottage 1"
        billing['city'] = "Kuusamo"
        billing['state'] = "Northern Ostrobothnia"
        billing['zip'] = "93999"
        billing['country'] = "FI"
        addressinfo['Billing'] = billing

        Shipping = {}
        Shipping['email'] = "sales@andrew-amanda.com"
        Shipping['first_name'] = "Andrew"
        Shipping['last_name'] = "Everett"
        Shipping['address1'] = "31 Reindeer Road"
        Shipping['address2'] = "Cottage 1"
        Shipping['city'] = "Kuusamo"
        Shipping['state'] = "Northern Ostrobothnia"
        Shipping['zip'] = "93999"
        Shipping['country'] = "FI"
        addressinfo['Shipping'] = Shipping

        data['AddressInfo'] = addressinfo


        itemdetailslist = []
        item1 = {}
        item1['item_number'] = "AA-AAFGGHG"
        item1['quantity'] = 1
        item1['item_name'] = "Acebeam M50"
        item1['amount'] = '20.0'
        item1['discount_amount'] = "0.0000"
        itemdetailslist.append(item1)

        item2 = {}
        item2['item_number'] = "AA-ABGECDC"
        item2['quantity'] = 1
        item2['item_name'] = "Acebeam TK18 Samsung"
        item2['amount'] = '20.0'
        item2['discount_amount'] = "0.0000"
        itemdetailslist.append(item2)

        data['ItemDetailsList'] = itemdetailslist

        data['day_phone_a'] = ""
        data['day_phone_b'] = "555-555-5555"
        data['cn'] = "You have been redirected to UPS i-parcel to complete your international checkout."
        data['ddp'] = "1"
        data['servicelevel'] = "115"





    	json_data = json.dumps(data)
    	print "******* json = ", json_data

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        import requests
        response = requests.post(url_redirect, data=json.dumps(data), headers=headers)


        #entry = render_to_string(template, variables)



        #query_string = urllib.urlencode(entry)
        #response = urllib2.urlopen(url_redirect, entry).read()

	#print "****** entry = ", entry
	print "****** response = ", response.text
    	res = json.loads(response.text)
	print "tx = ", res['tx']
    	checkout_audit._audit(request, 'iParcel_SetCheckoutRedirect', res)

	iparcel_checkout_url = "https://pay.i-parcel.com/v1/Cart?key=%&tx=%".format(key, res['tx'])
	from django.http import HttpResponseRedirect
	return res['tx']



    def SetExpressCheckout(self, request, amount, currency, return_url, cancel_url, cart_items=None, **kwargs):
        """
        To set up an Express Checkout transaction, you must invoke the SetExpressCheckout API
        to provide sufficient information to initiate the payment flow and redirect to iParcel if the
        operation was successful.

        @currency: Look at 'https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/e_howto_api_nvp_currency_codes'
        @amount : should be string with the following format '10.00'
        @return_url : should be in the format scheme://hostname[:uri (optional)]
        @cancel_url : should be in the format scheme://hostname[:uri (optional)]

        @returns bool

        If you want to add extra parameters, you can define them in **kwargs dict. For instance:
         - SetExpressCheckout(10.00, US, http://www.test.com/cancel/, http://www.test.com/return/, **{'SHIPTOSTREET': 'T Street', 'SHIPTOSTATE': 'T State'})

        More information can be found at https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/e_howto_api_ECCustomizing
        """
        parameters = {
            'key': self.private_key,
            'return' : return_url,
            'cancel_return' : cancel_url,
            'PAYMENTREQUEST_0_AMT' : amount,
            'currency_code' : currency,
            'PAYMENTREQUEST_0_SHIPTONAME' : smart_str(request.session.get('shipping_name','')),
            'PAYMENTREQUEST_0_SHIPTOSTREET' : smart_str(request.session.get('shipping_address_1','')),
            'PAYMENTREQUEST_0_SHIPTOCITY' : smart_str(request.session.get('shipping_city','')),
            'PAYMENTREQUEST_0_SHIPTOSTATE' : smart_str(request.session.get('shipping_state','')),
            'PAYMENTREQUEST_0_SHIPTOZIP' : request.session.get('shipping_zip',''),
            'PAYMENTREQUEST_0_SHIPTOSTREET2' : smart_str(request.session.get('shipping_address_2','')),
            'PAYMENTREQUEST_0_SHIPTOPHONENUM' : request.session.get('Phone',''),
            'PAYMENTREQUEST_0_SHIPTOCOUNTRYCODE' : request.session.get('shipping_country', '')
            #'PAYMENTREQUEST_0_SHIPTOCOUNTRYCODE' : request.session.get('shipping_country_code', '')

        }

        parameters.update(kwargs)

        if cart_items:
            ci_params = {}
            for i in range(0, len(cart_items)):
                item = cart_items[i]
                ci_params['L_PAYMENTREQUEST_0_NAME%s' % i] = item['NAME']
                ci_params['L_PAYMENTREQUEST_0_DESC%s' % i] = item['DESC']
                ci_params['L_PAYMENTREQUEST_0_AMT%s' % i] = item['AMT']
                ci_params['L_PAYMENTREQUEST_0_QTY%s' % i] = item['QTY']

                print 'item[' + str(i) + ']:' + item['NAME'] + ',' + item['NUMBER'] + ',' + item['DESC'] + ',' + str(item['AMT']) + ',' + str(item['QTY'])

            parameters.update(ci_params)

        query_string = self.signature + urllib.urlencode(parameters)
        response = urllib2.urlopen(self.NVP_API_ENDPOINT, query_string).read()
        response_dict = parse_qs(response)
        self.api_response = response_dict
        state = self._get_value_from_qs(response_dict, "ACK")
        if state in ["Success", "SuccessWithWarning"]:
            self.token = self._get_value_from_qs(response_dict, "TOKEN")
            checkout_audit._audit(request, 'paypal_SetExpressCheckout', response)

            return True

        self.setexpresscheckouterror = GENERIC_PAYPAL_ERROR
        self.apierror = self._get_value_from_qs(response_dict, "L_LONGMESSAGE0")
        checkout_audit._audit(request, 'paypal_SetExpressCheckout', 'paypal error: ' + self.apierror, 'Error')

        tb = traceback.format_exc()
        error_msg = "{}: {}".format(self.apierror, tb)
        subject = "An exception occured during check out"
        admin_emails = [v for k,v in settings.ADMINS]
        send_mail_async(subject, error_msg, settings.EMAIL_ORDER, admin_emails,fail_silently=False, html='')


        return False





    """
    If SetExpressCheckout is successfull use TOKEN to redirect to the browser to the address BELOW:

     - https://www.sandbox.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=TOKEN (for development only URL)

    """





    def GetExpressCheckoutDetails(self, return_url, cancel_url, token = None):
        """
        This method performs the NVP API method that is responsible from getting the payment details.
        This returns True if successfully fetch the checkout details, otherwise returns False.
        All of the parameters are REQUIRED.

        @returns bool
        """
        token = self.token if token is None else token
        if token is None:
            self.getexpresscheckoutdetails = TOKEN_NOT_FOUND_ERROR
            return False

        parameters = {
            'METHOD' : "GetExpressCheckoutDetails",
            'RETURNURL' : return_url,
            'CANCELURL' : cancel_url,
            'TOKEN' : token,
        }
        query_string = self.signature + urllib.urlencode(parameters)
        response = urllib2.urlopen(self.NVP_API_ENDPOINT, query_string).read()
        response_dict = parse_qs(response)
        self.api_response = response_dict
        state = self._get_value_from_qs(response_dict, "ACK")
        if not state in ["Success", "SuccessWithWarning"]:
            self.getexpresscheckoutdetailserror = self._get_value_from_qs(response_dict, "L_SHORTMESSAGE0")
            self.apierror = self.getexpresscheckoutdetailserror
            return False

        return True




    def DoExpressCheckoutPayment(self, request, currency, amount, token = None, payerid = None):
        """
        This method performs the NVP API method that is responsible from doing the actual payment.
        All of the parameters are REQUIRED.
        @currency: Look at 'https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/e_howto_api_nvp_currency_codes'
        @amount : should be string with the following format '10.00'
        @token : token that will come from the result of SetExpressionCheckout process.
        @payerid : payerid that will come from the url when iParcel redirects you after SetExpressionCheckout process.

        @returns bool
        """
        if token is None:
            self.doexpresscheckoutpaymenterror = TOKEN_NOT_FOUND_ERROR
            return False

        if payerid is None:
            self.doexpresscheckoutpaymenterror = NO_PAYERID_ERROR
            return False

        parameters = {
            'METHOD' : "DoExpressCheckoutPayment",
            'PAYMENTREQUEST_0_PAYMENTACTION' : 'Sale',
            'TOKEN' : token,
            'PAYMENTREQUEST_0_AMT' : amount,
            'PAYMENTREQUEST_0_CURRENCYCODE' : currency,
            'PAYERID' : payerid,
            'PAYMENTREQUEST_0_SHIPTONAME' : smart_str(request.session.get('shipping_name','')),
            'PAYMENTREQUEST_0_SHIPTOSTREET' : smart_str(request.session.get('shipping_address_1','')),
            'PAYMENTREQUEST_0_SHIPTOCITY' : smart_str(request.session.get('shipping_city','')),
            'PAYMENTREQUEST_0_SHIPTOSTATE' : smart_str(request.session.get('shipping_state','')),
            'PAYMENTREQUEST_0_SHIPTOZIP' : request.session.get('shipping_zip',''),
            'PAYMENTREQUEST_0_SHIPTOSTREET2' : smart_str(request.session.get('shipping_address_2','')),
            'PAYMENTREQUEST_0_SHIPTOPHONENUM' : request.session.get('Phone',''),
            'PAYMENTREQUEST_0_SHIPTOCOUNTRYCODE' : request.session.get('shipping_country', '')
            #'PAYMENTREQUEST_0_SHIPTOCOUNTRYCODE' : request.session.get('shipping_country_code', '')

        }

        cart_items = request.session.get('cart_items')
        if cart_items:
            ci_params = {}
            for i in range(0, len(cart_items)):
                item = cart_items[i]
                ci_params['L_PAYMENTREQUEST_0_NAME%s' % i] = item['NAME']
                ci_params['L_PAYMENTREQUEST_0_DESC%s' % i] = item['DESC']
                ci_params['L_PAYMENTREQUEST_0_AMT%s' % i] = item['AMT']
                ci_params['L_PAYMENTREQUEST_0_QTY%s' % i] = item['QTY']

            parameters.update(ci_params)

        query_string = self.signature + urllib.urlencode(parameters)
        response = urllib2.urlopen(self.NVP_API_ENDPOINT, query_string).read()
        response_tokens = {}
        for token in response.split('&'):
            response_tokens[token.split("=")[0]] = token.split("=")[1]
        for key in response_tokens.keys():
            response_tokens[key] = urllib2.unquote(response_tokens[key])

        state = self._get_value_from_qs(response_tokens, "ACK")
        self.response = response_tokens
        self.api_response = response
        if not state in ["Success", "SuccessWithWarning"]:
            self.doexpresscheckoutpaymenterror = GENERIC_PAYMENT_ERROR
            self.apierror = self._get_value_from_qs(response_tokens, "L_LONGMESSAGE0") + ", Error code: " + self._get_value_from_qs(response_tokens, "L_ERRORCODE0")
            checkout_audit._audit(request, 'paypal_DoExpressCheckoutPayment', 'paypal error: ' + self.apierror, 'Error')
            request.session['paypal_error'] = 'paypal error: ' + self.apierror

            tb = traceback.format_exc()
            error_msg = "{}: {}".format(self.apierror, tb)
            subject = "An exception occured during check out"
            admin_emails = [v for k,v in settings.ADMINS]
            send_mail_async(subject, error_msg, settings.EMAIL_ORDER, admin_emails,fail_silently=False, html='')


            return False
        checkout_audit._audit(request, 'paypal_DoExpressCheckoutPayment', self.response)

        return True



    def RefundTransaction(self, transid, refundtype, currency = None, amount = None, note = "Dummy note for refund"):
        """
        Performs iParcel API method for refund.

        @refundtype: 'Full' or 'Partial'

        Possible Responses:
         {'ACK': 'Failure', 'TIMESTAMP': '2009-12-13T09:51:19Z', 'L_SEVERITYCODE0': 'Error', 'L_SHORTMESSAGE0':
         'Permission denied', 'L_LONGMESSAGE0': 'You do not have permission to refund this transaction', 'VERSION': '53.0',
         'BUILD': '1077585', 'L_ERRORCODE0': '10007', 'CORRELATIONID': '3d8fa24c46c65'}

         or

         {'REFUNDTRANSACTIONID': '9E679139T5135712L', 'FEEREFUNDAMT': '0.70', 'ACK': 'Success', 'TIMESTAMP': '2009-12-13T09:53:06Z',
         'CURRENCYCODE': 'AUD', 'GROSSREFUNDAMT': '13.89', 'VERSION': '53.0', 'BUILD': '1077585', 'NETREFUNDAMT': '13.19',
         'CORRELATIONID': '6c95d7f979fc1'}
        """

        if not refundtype in ["Full", "Partial"]:
            self.refundtransactionerror = "Wrong parameters given, We can not perform your refund request"
            return False

        parameters = {
            'METHOD' : "RefundTransaction",
            'TRANSACTIONID' : transid,
            'REFUNDTYPE' : refundtype,
        }

        if refundtype == "Partial":
            extra_values = {
                'AMT' : amount,
                'CURRENCYCODE' : currency,
                'NOTE' : note
            }
            parameters.update(extra_values)

        query_string = self.signature + urllib.urlencode(parameters)
        response = urllib2.urlopen(self.NVP_API_ENDPOINT, query_string).read()
        response_tokens = {}
        for token in response.split('&'):
            response_tokens[token.split("=")[0]] = token.split("=")[1]

        for key in response_tokens.keys():
            response_tokens[key] = urllib2.unquote(response_tokens[key])

        state = self._get_value_from_qs(response_tokens, "ACK")
        self.refund_response = response_tokens
        self.api_response = response
        if not state in ["Success", "SuccessWithWarning"]:
            self.refundtransactionerror = GENERIC_REFUND_ERROR
            return False
        return True



    def DoDirectPayment(self, acct, expdate, cvv2, cardtype, first_name, last_name, amount, currency = "USD", **kwargs):
        """
        Calls the direct payment method of the iParcel API. The detailed explanation for that
        API call is available on:
        https://cms.paypal.com/us/cgi-bin/?cmd=_render-content&content_ID=developer/e_howto_api_nvp_r_DoDirectPayment

        @acct: credit card number(string): numeric characters only
        @expdate: expiry date for the credit card(string): format:MMYYYY
        @cvv2: card verification value(string): 3 or 4 digit length
        @cardtype: card type(string): Visa, Mastercard, Discover, Amex, Maestro or Solo.
        @first_name: First name of the customer
        @last_name: Surname of the customer
        @amount: Amount to be charged(decimal) (ex: Decimal('10.00'))
        @currency: Currency code: Default: USD

        @returns bool

        Extra parameters (**kwargs) contains several required and optional parameters such as ip_address, shipping
        address related inputs like street name, country, zipcode.

        This method sends an HTTP POST request. It contructs the necessary POST request with the given parameters.
        Then it fetches the result which looks like a raw query string and parses it.

        It returns True if the money can be successfully charged from the credit card by looking at the response code.
        Otherwise, it returns False and sets the generic error.
        """
        #################
        # BEGIN ROUTINE #
        #################
        # Firstly, validate the known actual parameters with the 'assert' keyword.
        assert len(expdate) == 6
        assert cardtype in ["Visa", "MasterCard", "Discover", "Amex", "Maestro", "Solo"]
        assert type(amount) == Decimal

        # Validate kwargs
        assert kwargs.get("ipaddress") is not None
        assert kwargs.get("street") is not None
        assert kwargs.get("city") is not None
        assert kwargs.get("state") is not None
        assert kwargs.get("countrycode") is not None
        assert kwargs.get("zip") is not None

        # We should format the amount before we put it into the POST data..
        amount = str(amount.quantize(Decimal(".01"), rounding = ROUND_UP))
        # Build up the query dictionary..
        query_dict = {
            "METHOD": "DoDirectPayment",
            "PAYMENTACTION": "Sale",
            "RETURNFMFDETAILS": 0,
            "CREDITCARDTYPE": cardtype.upper(),
            "ACCT": acct,
            "EXPDATE": expdate,
            "CVV2": cvv2,
            "FIRSTNAME": first_name,
            "LASTNAME": last_name,
            "CURRENCYCODE": currency,
            "AMT": amount,
            }
        # Include the kwargs dictionary into the query dictionary..
        for key, value in kwargs.items():
            # All names in the query dict must be uppercase..
            query_dict[key.upper()] = value

        query_string = self.signature + urllib.urlencode(query_dict)
        response = urllib.urlopen(self.NVP_API_ENDPOINT, query_string).read()
        response_dict = parse_qs(response)
        self.api_response = response
        self.response = response_dict
        state = self._get_value_from_qs(response_dict, "ACK")
        if not state in ["Success", "SuccessWithWarning"]:
            self.apierror = self._get_value_from_qs(response_dict, "L_LONGMESSAGE0")
            return False
        return True
        ###############
        # END ROUTINE #
        ###############


    def GetPaymentResponse(self):
        return self.response


    def GetRefundResponse(self):
        return self.refund_response
