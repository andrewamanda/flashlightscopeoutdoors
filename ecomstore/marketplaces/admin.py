from django.db import models
from django.contrib import admin
from django_object_actions import DjangoObjectActions
from tinymce.widgets import TinyMCE
from ecomstore.marketplaces.models import *
from django.http import HttpResponse
import csv
from ckeditor.widgets import CKEditorWidget
import requests
import json
import simplejson
import random
from django.conf import settings
from PyPDF2 import PdfFileWriter, PdfFileReader
import base64, os
from ecomstore.utils.strops import *
import PyPDF2
import copy

from boto.mws.connection import MWSConnection
import time



JET_TOKEN_REQUEST = {"user": settings.JET_API_USER, "pass": settings.JET_SECRET}

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):

    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

        writer = csv.writer(response)
        if header:
            writer.writerow(list(field_names))
        for obj in queryset:
            writer.writerow([unicode(getattr(obj, field)).encode("utf-8","replace") for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv



from import_export import resources
from ecomstore.marketplaces.models import *
from import_export import fields

from import_export.admin import ImportExportModelAdmin



class AmazonOrderResource(resources.ModelResource):
    #order_id = fields.Field(column_name='order-id')
    #order_item_id = fields.Field(column_name='order-item-id')
    #purchase_date = fields.Field(column_name='purchase-date')
    #payments_date = fields.Field(column_name='payments-date')
    #buyer_email = fields.Field(column_name='buyer-email')
    #buyer_phone_number = fields.Field(column_name='buyer-phone-number')
    #sku = fields.Field(column_name='sku')
    #product_name = fields.Field(column_name='product-name')
    #quantity_purchased = fields.Field(column_name='quantity-purchased')
    #currency = fields.Field(column_name='currency')
    #item_price = fields.Field(column_name='item-price')
    #item_tax = fields.Field(column_name='item-tax')
    #shipping_price = fields.Field(column_name='shipping-price')
    #shipping_tax = fields.Field(column_name='shipping-tax')
    #ship_service_level = fields.Field(column_name='ship-service-level')
    #item_promotion_discount = fields.Field(column_name='item-promotion-discount')
    #item_promotion_id = fields.Field(column_name='item-promotion-id')
    #delivery_start_date = fields.Field(column_name='delivery-start-date')
    #delivery_end_date = fields.Field(column_name='delivery-end-date')
    #delivery_time_zone = fields.Field(column_name='delivery-time-zone')
    #delivery_Instructions = fields.Field(column_name='delivery-Instructions')
    #sales_channel = fields.Field(column_name='sales-channel')
    #is_business_order = fields.Field(column_name='is-business-order')
    #purchase_order_number = fields.Field(column_name='purchase-order-number')
    #price_designation = fields.Field(column_name='price-designation')

    class Meta:
        model = AmazonOrder
        #fields = ('id','order_id', 'buyer_email',)
        #exclude = ('purchase_date','payments_date')
        import_id_fields = ['order_id']

class AmazonOrderExportImportAdmin(ImportExportModelAdmin):
    list_display = ('store','order_id','email_sent','purchase_date','recipient_name','product_name','buyer_email','ship_country')
    search_fields = ('order_id','buyer_email','recipient_name')
    ordering = ['-purchase_date']
    list_filter = ('email_sent','store')
    list_editable = ('email_sent',)
    actions = [export_as_csv_action("CSV Export", fields=['order_id'])]
    resource_class = AmazonOrderResource

    actions = ['send_feedback_request_emails']

    def get_actions(self, request):
        actions = super(AmazonOrderExportImportAdmin, self).get_actions(request)
        return actions

    def send_feedback_request_emails_attempt_to_use_mws(self, request, queryset):
        # North America connection
        from ecomstore import settings
        mws = MWSConnection(settings.AMAZON_MWS_NA_AccessKeyID,settings.AMAZON_MWS_NA_SecretKey)
        mws.SellerId = settings.AMAZON_MWS_NA_MerchantID
        mws.Merchant = settings.AMAZON_MWS_NA_MerchantID

        import datetime
        start_date = (datetime.datetime.now()- datetime.timedelta(days=15)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat()
        end_date = (datetime.datetime.now()- datetime.timedelta(days=14)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat()

        orders = mws.list_orders(MarketplaceId=[settings.AMAZON_MWS_US_MarketPlaceID],OrderStatus=["Shipped"], CreatedBefore=end_date, CreatedAfter=start_date)
        #print "total order returned = ", len(orders.ListOrdersResult.Orders.Order)
        for order in orders.ListOrdersResult.Orders.Order:
            this_order_id = order.AmazonOrderId
            theData = mws.get_order(AmazonOrderId = this_order_id)
            #print "theData = ",theData
            #do what you want with the data
            #
            #EXAMPLE GET ORDER ITEMS
            order_items = mws.list_order_items(AmazonOrderId = this_order_id)
            #print "order_items = ", order_items


    def send_feedback_request_emails(self, request, queryset):
       for obj in queryset:
            emailStatus = obj.sendfeedbackrequest()
            self.message_user(request, emailStatus)
            if emailStatus.startswith("Posted"):
                 obj.email_sent = True
                 obj.save()

    send_feedback_request_emails.short_description = "Send Feedback Request Emails"


    pass

class AmazonOrder_ExcludedAdmin(admin.ModelAdmin):
    list_display = ('order_id','exclude_reason',)
    search_fields = ('order_id',)
    ordering = ['order_id']

    actions = ['solicit_feedback']

    def solicit_feedback(self, request, queryset):
       for obj in queryset:
            emailStatus = obj.sendfeedbackrequest()
            self.message_user(request, emailStatus)
            if emailStatus.startswith("Posted"):
                 obj.email_sent = True
                 obj.save()

    solicit_feedback.short_description = "Solicit Feedback"

class Amazon_SKU_4_ReviewAdmin(admin.ModelAdmin):
    list_display = ('SKU','title',)
    search_fields = ('SKU','title',)
    ordering = ['title']

from ecomstore.catalog.models import RichTextField
from ckeditor.widgets import CKEditorWidget

class VendorExpressOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number','total_cost','tracking','shipping_date','pay_expected_by','actual_payment_date','shipping_label',)
    search_fields = ('order_number',)
    ordering = ['shipping_date']
    list_editable = ['actual_payment_date']

    fieldsets = (
                 ('Basics', {'fields': (('order_number',),)}),
                 ('Shipping', {'fields': (('tracking','shipping_label'),)}),
                 ('Payments', {'fields': (('pay_expected_by','total_cost','actual_payment_date',),)}),
                 ('Details', {'fields': (('order_details',),)}),
                )

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

admin.site.register(AmazonOrder_Excluded, AmazonOrder_ExcludedAdmin)
admin.site.register(AmazonOrder, AmazonOrderExportImportAdmin)
admin.site.register(Amazon_SKU_4_Review, Amazon_SKU_4_ReviewAdmin)
admin.site.register(VendorExpressOrder, VendorExpressOrderAdmin)

class JetOrderItemsInline(admin.TabularInline):
    model = JETOrder_Items
    extra = 0

class JETOrderAdmin(admin.ModelAdmin):
    list_display = ('order_url','status','jet_request_directed_cancel','tracking_number','ship_date','order_placed_date',)
    list_editable = ('tracking_number','ship_date',)
    search_fields = ('order_url',)
    ordering = ['order_placed_date']
    list_filter = ('status','directed_cancel')

    fieldsets = (
                 ('Basics', {'fields': (('status','order_url','merchant_order_id','reference_order_id','customer_reference_order_id','fulfillment_node','alt_order_id','hash_email','exception_state','order_placed_date','order_transmission_date','jet_request_directed_cancel','directed_cancel'),)}),
                 ('Ship Detail', {'fields': (('tracking_number','ship_date',),)}),
                 ('Order Detail', {'fields': (('order_detail_request_shipping_carrier','order_detail_request_shipping_method','order_detail_request_service_level','order_detail_request_ship_by','order_detail_request_deliver_by'),)}),
                 ('Buyer', {'fields': (('buyer_name','buyer_phone_number',),)}),
                 ('Ship To', {'fields': (('shipping_to_recipient_name','shipping_to_recipient_phone_number','shipping_to_address_address1','shipping_to_address_address2','shipping_to_address_city','shipping_to_address_state','shipping_to_address_zip_code'),)}),
                 ('Order Totals', {'fields': (('order_totals_item_price_base_price','order_totals_item_price_item_tax','order_totals_item_price_item_shipping_cost','order_totals_item_price_item_shipping_tax','order_totals_item_fees',),)}),

                )
    inlines = [JetOrderItemsInline,]

    actions = ['import_all_jet_orders','cancel_jet_order','refund_jet_order','ack_jet_order','ship_jet_order']
    def get_actions(self, request):
        actions = super(JETOrderAdmin, self).get_actions(request)
        return actions

    def import_all_jet_orders(self, request, queryset):
        from django.template.loader import render_to_string

        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        #print "authHeader = " + authHeader
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        retStatus = ""
        base_order_url = "https://merchant-api.jet.com/api/orders/"
        status_list = ['created','ready','acknowledged','inprogress','complete']
        for status in status_list:
            url = base_order_url + status
            jetResponse = requests.get(url, headers=headers)
            orders = json.loads(jetResponse.text)
            for o in orders['order_urls']:
                jetOrders = JETOrder.objects.filter(order_url = o)
                if len(jetOrders) == 0:
                    jetOrder = JETOrder()
                    retStatus += "New Order: " + o
                else:
                    jetOrder = jetOrders[0]
                jetOrder.status = status
                jetOrder.order_url = o

                # populate order Details
                order_details_url = "https://merchant-api.jet.com/api/" + o
                jetResponse = requests.get(order_details_url, headers=headers)
                orderDetails = json.loads(jetResponse.text)

                jetOrder.merchant_order_id = orderDetails['merchant_order_id']
                jetOrder.reference_order_id = orderDetails['reference_order_id']
                jetOrder.customer_reference_order_id = orderDetails['customer_reference_order_id']
                jetOrder.fulfillment_node = orderDetails['fulfillment_node']
                jetOrder.alt_order_id = orderDetails['alt_order_id']
                jetOrder.hash_email = orderDetails['hash_email']
                jetOrder.exception_state = orderDetails.get('exception_state', 'None')
                jetOrder.order_placed_date = orderDetails['order_placed_date']
                jetOrder.order_transmission_date = orderDetails['order_transmission_date']
                jetOrder.jet_request_directed_cancel = orderDetails['jet_request_directed_cancel']

                jetOrder.order_detail_request_shipping_carrier = orderDetails['order_detail']['request_shipping_carrier']
                jetOrder.order_detail_request_shipping_method = orderDetails['order_detail'].get('request_shipping_method', 'None')
                jetOrder.order_detail_request_service_level = orderDetails['order_detail']['request_service_level']
                jetOrder.order_detail_request_ship_by = orderDetails['order_detail']['request_ship_by']
                jetOrder.order_detail_request_deliver_by = orderDetails['order_detail'].get('request_deliver_by', 'None')

                jetOrder.buyer_name = orderDetails['buyer']['name']
                jetOrder.buyer_phone_number = orderDetails['buyer']['phone_number']

                jetOrder.shipping_to_recipient_name = orderDetails['shipping_to']['recipient']['name']
                jetOrder.shipping_to_recipient_phone_number = orderDetails['shipping_to']['recipient']['phone_number']
                jetOrder.shipping_to_address_address1 = orderDetails['shipping_to']['address']['address1']
                jetOrder.shipping_to_address_address2 = orderDetails['shipping_to']['address']['address2']
                jetOrder.shipping_to_address_city = orderDetails['shipping_to']['address']['city']
                jetOrder.shipping_to_address_state = orderDetails['shipping_to']['address']['state']
                jetOrder.shipping_to_address_zip_code = orderDetails['shipping_to']['address']['zip_code']

                jetOrder.order_totals_item_price_base_price = orderDetails['order_totals']['item_price']['base_price']
                jetOrder.order_totals_item_price_item_tax = orderDetails['order_totals']['item_price']['item_tax']
                jetOrder.order_totals_item_price_item_shipping_cost = orderDetails['order_totals']['item_price']['item_shipping_cost']
                jetOrder.order_totals_item_price_item_shipping_tax = orderDetails['order_totals']['item_price']['item_shipping_tax']
                jetOrder.order_totals_item_fees = orderDetails['order_totals'].get('item_fees', 0.00)

                jetOrder.save()

                if jetOrder.pk:
                    order_items = orderDetails['order_items']
                    for ci in order_items:
                            id = ci.get('order_item_id', 'None')
                            orderItems = JETOrder_Items.objects.filter(order_item_id = id)
                            if len(orderItems) == 0:
                                oi = JETOrder_Items()
                            else:
                                oi = orderItems[0]
                            oi.jet_order = jetOrder
                            oi.order_item_id = ci.get('order_item_id', 'None')
                            oi.alt_order_item_id = ci.get('alt_order_item_id', 'None')
                            oi.merchant_sku = ci.get('merchant_sku', 'None')
                            oi.product_title = ci.get('product_title', 'None')
                            oi.request_order_quantity = ci.get('request_order_quantity', 0)
                            oi.request_order_cancel_quantity = ci.get('request_order_cancel_quantity', 0)
                            oi.adjustment_reason = ci.get('adjustment_reason', 'None')
                            oi.item_tax_code = ci.get('item_tax_code', 'None')
                            oi.url = ci.get('url', 'None')
                            oi.price_adjustment = ci.get('price_adjustment', 0.00)
                            oi.item_fees = ci.get('item_fees', 0.00)
                            oi.regulatory_fees = ci.get('regulatory_fees', 0.00)

                            oi.save()

        directedcancel_url = "https://merchant-api.jet.com/api/orders/directedCancel"
        testJet = requests.get(url, headers=headers)
        cancelledOrders = json.loads(testJet.text)['order_urls']

        for order_url in cancelledOrders:
            #print "directed cancel url = ", order_url
            jetOrder = JETOrder.objects.filter(order_url = o)[0]
            jetOrder.directed_cancel = 'yes'
            jetOrder.save()


        self.message_user(request, retStatus)

    import_all_jet_orders.short_description = "Import All JET Orders"

    def cancel_jet_order(self, request, queryset):
        from django.template.loader import render_to_string

        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        #print "authHeader = " + authHeader
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        retStatus = ""
        for sd in queryset:
            id = sd.merchant_order_id
            url = "https://merchant-api.jet.com/api/orders/" + id + "/shipped"

            cancels = {}
            cancels['alt_order_id'] = sd.alt_order_id

            shipments = []
            shipment = {}
            shipment['alt_shipment_id'] = sd.merchant_order_id + str(random.randint(1,10))
            shipment_items = []
            oi = sd.jetorder_items_set.all()
            for i in oi:
                shipment_item = {}
                shipment_item['merchant_sku'] = i.merchant_sku
                shipment_item['response_shipment_cancel_qty'] = i.request_order_cancel_quantity
                shipment_items.append(shipment_item)
            shipment['shipment_items'] = shipment_items
            shipments.append(shipment)

            cancels['shipments'] = shipments

            testJet = requests.put(url, headers=headers, data=json.dumps(cancels))

            retStatus += "Cancel Status: {}, content: {}".format(testJet.status_code, testJet.text)


        self.message_user(request, retStatus)

    cancel_jet_order.short_description = "Cancel Jet Order"

    def refund_jet_order(self, request, queryset):
        from django.template.loader import render_to_string

	#print "******* refund jet order"
        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        #print "authHeader = " + authHeader
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        retStatus = ""
        for sd in queryset:
            id = sd.reference_order_id
            alt_refund_id = sd.tracking_number
            url = "https://merchant-api.jet.com/api/refunds/" + id + "/" + alt_refund_id

            refunds = {}

            items = []
            i = sd.jetorder_items_set.all()
            for oi in i:
                item = {}
                item['order_item_id'] = oi.order_item_id
                item['alt_order_item_id'] = oi.alt_order_item_id
                item['total_quantity_returned'] = oi.request_order_cancel_quantity
                item['order_return_refund_qty'] = oi.request_order_cancel_quantity
                item['refund_reason'] = oi.adjustment_reason
                #item['refund_feedback'] = 'NA'
                item['notes'] = 'NA'
                refund_amount = {}
                refund_amount['principal'] = float(sd.order_totals_item_price_base_price)
                refund_amount['tax'] = 0
                refund_amount['shipping_cost'] = float(sd.order_totals_item_price_item_shipping_cost)
                refund_amount['shipping_tax'] = 0
                item['refund_amount'] = refund_amount

                items.append(item)

            refunds['items'] = items

            testJet = requests.post(url, headers=headers, data=json.dumps(refunds))

            retStatus += "Refund Status: {}, content: {}".format(testJet.status_code, testJet.text)


        self.message_user(request, retStatus)

    refund_jet_order.short_description = "Refund Jet Order"

    def ack_jet_order(self, request, queryset):
        from django.template.loader import render_to_string

        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        #print "authHeader = " + authHeader
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        retStatus = ""
        for sd in queryset:
            id = sd.merchant_order_id

            url = "https://merchant-api.jet.com/api/orders/" + id + "/acknowledge"
            order_items = sd.jetorder_items_set.all()
            ack_order_items = []
            for oi in order_items:
                ack_order_item = {}
                ack_order_item['order_item_id'] = oi.order_item_id
                ack_order_item['order_item_acknowledgement_status'] = "fulfillable"
                ack_order_items.append(ack_order_item)
            ack_order = {}
            ack_order['acknowledgement_status'] = "accepted"
            ack_order['order_items'] = ack_order_items

            testJet = requests.put(url, headers=headers, data=json.dumps(ack_order))
            retStatus += "- ack status: " + str(testJet.status_code) + ":" + testJet.text


        self.message_user(request, retStatus)

    ack_jet_order.short_description = "Acknowledge Jet Order"

    def ship_jet_order(self, request, queryset):
            from django.template.loader import render_to_string

            headers = {"Accept": "application/json"}
            testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
            reqJson = json.loads(testJet.text)
            authHeader = "bearer " + reqJson['id_token']
            #print "authHeader = " + authHeader
            headers = {"Content-Type":"application/json", "Authorization":authHeader}

            retStatus = ""
            orders = {}
            shipments = []
            for sd in queryset:
                shipment = {}
                shipment['shipment_tracking_number'] = sd.tracking_number
                shipment_items = []
                oi = sd.jetorder_items_set.all()
                for i in oi:
                    shipment_item = {}
                    shipment_item['merchant_sku'] = i.merchant_sku
                    shipment_item['response_shipment_sku_quantity'] = i.request_order_quantity
                    shipment_items.append(shipment_item)
                shipment['response_shipment_date'] = sd.ship_date.isoformat() + ".0000000-04:00"
                #print "date time in iso: ", sd.ship_date.isoformat() + ".0000000-04:00"
                shipment['carrier'] = 'USPS'
                shipment['shipment_items'] = shipment_items
                shipments.append(shipment)
                orders['shipments'] = shipments
                url = "https://merchant-api.jet.com/api/orders/" + sd.merchant_order_id + "/shipped"
                #print "url = ", url
                testJet = requests.put(url, headers=headers, data=json.dumps(orders))
                retStatus += "Ship Status: {}, content: {}".format(testJet.status_code, testJet.text)


            self.message_user(request, retStatus)

    ship_jet_order.short_description = "Ship JET order, one order a time"


admin.site.register(JETOrder, JETOrderAdmin)

class JetReturnMerchant_SkusInline(admin.TabularInline):
    model = JETReturn_merchant_skus
    extra = 0

class JETReturn_itemsInline(admin.TabularInline):
    model = JETReturn_items
    extra = 0



class JETReturnAdmin(admin.ModelAdmin):
    list_display = ('return_url','status',)
    search_fields = ('return_url',)
    list_filter = ('status',)
    inlines = [JetReturnMerchant_SkusInline,JETReturn_itemsInline]

    fieldsets = (
                 ('Basics', {'fields': (('status','return_url','agree_to_return_charge','alt_order_id','alt_return_authorization_id','merchant_order_id','merchant_return_authorization_id','merchant_return_charge','reference_order_id','reference_return_authorization_id','refund_without_return','return_date','return_status','shipping_carrier','tracking_number','return_charge_feedback'),)}),
                 #('Ship Detail', {'fields': (('tracking_number','ship_date',),)}),
                 #('Order Detail', {'fields': (('order_detail_request_shipping_carrier','order_detail_request_shipping_method','order_detail_request_service_level','order_detail_request_ship_by','order_detail_request_deliver_by'),)}),
                 #('Buyer', {'fields': (('buyer_name','buyer_phone_number',),)}),
                 #('Ship To', {'fields': (('shipping_to_recipient_name','shipping_to_recipient_phone_number','shipping_to_address_address1','shipping_to_address_address2','shipping_to_address_city','shipping_to_address_state','shipping_to_address_zip_code'),)}),
                 #('Order Totals', {'fields': (('order_totals_item_price_base_price','order_totals_item_price_item_tax','order_totals_item_price_item_shipping_cost','order_totals_item_price_item_shipping_tax','order_totals_item_fees',),)}),

                )

    actions = ['import_all_jet_returns','complete_jet_return']
    def get_actions(self, request):
        actions = super(JETReturnAdmin, self).get_actions(request)
        return actions

    def import_all_jet_returns(self, request, queryset):
        from django.template.loader import render_to_string

        headers = {"Accept": "application/json"}

        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        #print "text = ", testJet.text
        authHeader = "bearer " + reqJson['id_token']
        #print "authHeader = " + authHeader
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        retStatus = ""
        base_order_url = "https://merchant-api.jet.com/api/returns/"
        status_list = ['created','acknowledge','inprogress','completed by merchant']
        for status in status_list:
            url = base_order_url + status
            jetResponse = requests.get(url, headers=headers)
            returns = json.loads(jetResponse.text)
            for o in returns['return_urls']:
                jetReturns = JETReturn.objects.filter(return_url = o)
                if len(jetReturns) == 0:
                    jetReturn = JETReturn()
                    retStatus += "New Return: " + o
                else:
                    jetReturn = jetReturns[0]
                jetReturn.status = status
                jetReturn.return_url = o

                # populate return Details
                return_details_url = "https://merchant-api.jet.com/api/" + o
                jetResponse = requests.get(return_details_url, headers=headers)
                returnDetails = json.loads(jetResponse.text)

                jetReturn.agree_to_return_charge = returnDetails.get('agree_to_return_charge', False)
                jetReturn.alt_order_id = returnDetails.get('alt_order_id', 'None')
                jetReturn.alt_return_authorization_id = returnDetails.get('alt_return_authorization_id', 'None')
                jetReturn.merchant_order_id = returnDetails.get('merchant_order_id', 'None')
                jetReturn.merchant_return_authorization_id = returnDetails.get('merchant_return_authorization_id', 'None')
                jetReturn.merchant_return_charge = returnDetails.get('merchant_return_charge', 0.00)
                jetReturn.reference_order_id = returnDetails.get('reference_order_id', 'None')
                jetReturn.reference_return_authorization_id = returnDetails.get('reference_return_authorization_id', 'None')
                jetReturn.refund_without_return = returnDetails.get('refund_without_return', False)
                jetReturn.return_date = returnDetails.get('return_date', 'None')
                jetReturn.return_status = returnDetails.get('return_status', 'None')
                jetReturn.shipping_carrier = returnDetails.get('shipping_carrier', 'None')
                jetReturn.tracking_number = returnDetails.get('tracking_number', 'None')

                jetReturn.save()

                if jetReturn.pk:
                    return_items = returnDetails['items']
                    for ci in return_items:
                            id = ci.get('order_item_id', 'None')
                            returnItems = JETReturn_items.objects.filter(order_item_id = id)
                            if len(returnItems) == 0:
                                oi = JETReturn_items()
                            else:
                                oi = returnItems[0]
                            oi.jet_return = jetReturn

                            oi.order_item_id = ci.get('order_item_id', 'None')
                            oi.alt_order_item_id = ci.get('alt_order_item_id', 'None')
                            oi.total_quantity_returned = ci.get('total_quantity_returned', 0)
                            oi.order_return_refund_qty = ci.get('order_return_refund_qty', 0)
                            oi.notes = ci.get('notes', 'None')
                            oi.return_refund_feedback = ci.get('return_refund_feedback', 'None')
                            oi.refund_amount_principal = ci.get('refund_amount', 0.00).get('principal', 0.00)
                            oi.refund_amount_tax = ci.get('refund_amount', 0.00).get('tax', 0.00)
                            oi.refund_amount_shipping_cost = ci.get('refund_amount', 0.00).get('shipping_cost', 0.00)
                            oi.refund_amount_shipping_tax = ci.get('refund_amount', 0.00).get('shipping_tax', 0.00)

                            oi.save()

                    return_skus = returnDetails['return_merchant_SKUs']
                    for ci in return_skus:
                            id = ci.get('order_item_id', 'None')
                            returnSkus = JETReturn_merchant_skus.objects.filter(order_item_id = id)
                            if len(returnSkus) == 0:
                                oi = JETReturn_merchant_skus()
                            else:
                                oi = returnSkus[0]
                            oi.jet_return = jetReturn

                            oi.order_item_id = ci.get('order_item_id', 'None')
                            oi.alt_order_item_id = ci.get('alt_order_item_id', 'None')
                            oi.return_quantity = ci.get('return_quantity', 0)
                            oi.merchant_sku = ci.get('merchant_sku', 'None')
                            oi.merchant_sku_title = ci.get('merchant_sku_title', 'None')
                            oi.reason = ci.get('reason', 'None')

                            oi.requested_refund_amount_principal = ci.get('requested_refund_amount', 0.00).get('principal', 0.00)
                            oi.requested_refund_amount_tax = ci.get('requested_refund_amount', 0.00).get('tax', 0.00)
                            oi.requested_refund_amount_shipping_cost = ci.get('requested_refund_amount', 0.00).get('shipping_cost', 0.00)
                            oi.requested_refund_amount_shipping_tax = ci.get('requested_refund_amount', 0.00).get('shipping_tax', 0.00)

                            oi.save()



        self.message_user(request, retStatus)

    import_all_jet_returns.short_description = "Import All JET Returns"

    def complete_jet_return(self, request, queryset):
            from django.template.loader import render_to_string

            headers = {"Accept": "application/json"}
            testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
            reqJson = json.loads(testJet.text)
            authHeader = "bearer " + reqJson['id_token']
            #print "authHeader = " + authHeader
            headers = {"Content-Type":"application/json", "Authorization":authHeader}

            retStatus = ""
            returns = {}
            for sd in queryset:
                returns['merchant_order_id'] = sd.merchant_order_id
                returns['alt_order_id'] = sd.alt_order_id
                returns['agree_to_return_charge'] = sd.agree_to_return_charge
                returns['return_charge_feedback'] = sd.return_charge_feedback

                items = []
                oi = sd.jetreturn_items_set.all()
                for i in oi:
                    item = {}
                    item['order_item_id'] = i.order_item_id
                    item['alt_order_item_id'] = i.alt_order_item_id
                    item['total_quantity_returned'] = i.total_quantity_returned
                    item['order_return_refund_qty'] = i.order_return_refund_qty
                    item['return_refund_feedback'] = i.return_refund_feedback
                    item['notes'] = i.notes

                    refund_amount = {}
                    refund_amount['principal'] = i.refund_amount_principal
                    refund_amount['tax'] = i.refund_amount_tax
                    refund_amount['shipping_cost'] = i.refund_amount_shipping_cost
                    refund_amount['shipping_tax'] = i.refund_amount_shipping_tax

                    item['refund_amount'] = refund_amount

                    items.append(item)
                returns['items'] = items

                url = "https://merchant-api.jet.com/api/returns/" + sd.return_url.partition('state/')[2] + "/complete"
                #print "url = ", url
                #print "returns = ", simplejson.dumps(returns)
                testJet = requests.put(url, headers=headers, data=simplejson.dumps(returns))
                retStatus += "Ship Status: {}, content: {}".format(testJet.status_code, testJet.text)


            self.message_user(request, retStatus)

    complete_jet_return.short_description = "Complete Jet Return"


admin.site.register(JETReturn, JETReturnAdmin)


class FIMSOrderResource(resources.ModelResource):
    order_number = fields.Field(column_name='Order - Number', attribute='order_number')
    custom_field_1 = fields.Field(column_name='Custom - Field 1', attribute='custom_field_1')
    custom_field_2 = fields.Field(column_name='Custom - Field 2', attribute='custom_field_2')
    custom_field_3 = fields.Field(column_name='Custom - Field 3', attribute='custom_field_3')
    notes_from_buyer = fields.Field(column_name='Notes - From Buyer', attribute='notes_from_buyer')
    notes_internal = fields.Field(column_name='Notes - Internal', attribute='notes_internal')
    notes_to_buyer = fields.Field(column_name='Notes - To Buyer', attribute='notes_to_buyer')

    print ("order_number=", order_number)
    print ("custom_field_1=", custom_field_1)

    name = fields.Field(column_name='Ship To - Name', attribute='name')
    address_1 = fields.Field(column_name='Ship To - Address 1', attribute='address_1')
    address_2 = fields.Field(column_name='Ship To - Address 2', attribute='address_2')
    city = fields.Field(column_name='Ship To - City', attribute='city')
    company = fields.Field(column_name='Ship To - Company', attribute='company')
    country = fields.Field(column_name='Ship To - Country', attribute='country')
    phone = fields.Field(column_name='Ship To - Phone', attribute='phone')
    city = fields.Field(column_name='Ship To - City', attribute='city')
    zip = fields.Field(column_name='Ship To - Postal Code', attribute='zip')
    state = fields.Field(column_name='Ship To - State', attribute='state')
    email = fields.Field(column_name='Customer Email', attribute='email')
    #item_name = fields.Field(column_name='Custom - Field 1', attribute='item_name')
    #item_option = fields.Field(column_name='Item - Options', attribute='item_option')
    #item_qty = fields.Field(column_name='Item - Qty', attribute='item_qty')
    #item_price = fields.Field(column_name='Item - Price', attribute='item_price')
    total_weight = fields.Field(column_name='Weight - TotalOz', attribute='total_weight')
    #total_amount = fields.Field(column_name='Amount - Paid by Customer', attribute='total_amount')
    amount_paid_by_customer = fields.Field(column_name='Amount - Paid by Customer', attribute='amount_paid_by_customer')
    items_purchased = fields.Field(column_name='Products Purchased', attribute='items_purchased')
    marketplace_name = fields.Field(column_name='Market - Markeplace Name', attribute='marketplace_name')
    currency = fields.Field(column_name='Currency Used', attribute='currency')

    class Meta:
        model = ShipFIMS
        import_id_fields = (b'order_number',)
        #export_order = ('company_name', 'street_address', 'city', 'state', 'zip_code')

from django import forms
from django.contrib.admin import DateFieldListFilter

class FIMSOrderExportImportAdminForm(forms.ModelForm):
	airwaybill = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':12}))
	parcelId = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':12}))
	item_weight = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':4}))
	item_price = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':4}))
	total_amount = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':4}))
	total_weight = forms.CharField(required=False,widget=forms.TextInput(attrs={'size':4}))
	cost = forms.DecimalField(required=False,widget=forms.TextInput(attrs={'size':4}))



class FIMSOrderExportImportAdmin(ImportExportModelAdmin):
    #list_display = ('date','order_number','items','airwaybill','awb','total_amount','total_weight','mailviewtracking','fedextracking','shippinglabel', 'paid','cost','name','country', )
    #list_display = ('date','order_number','items','airwaybill','awb','total_amount','total_weight','mailviewtracking','shippinglabel', 'paid','cost','name','country', )
    list_display = ('date','order_number','items','airwaybill','awb','total_amount','total_weight','fedextracking','shippinglabel', 'paid','cost','name','country', 'mailviewtracking', )

    search_fields = ('date', 'order_number','name','airwaybill','parcelId','trackingNo',)
    list_filter = ('has_shipped','country','customer_claimed','customer_refunded','insurance_filed','parcel_returned',('date', DateFieldListFilter))
    list_editable = ('airwaybill','total_amount','total_weight','paid','cost')
    ordering = ['-date']
    actions = ['create_fims_label']
    resource_class = FIMSOrderResource


    form = FIMSOrderExportImportAdminForm

    list_per_page = 50

    pass

    def append_pdf(self, input,output):
        [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]

    def get_changelist_form(self, request, **kwargs):
        return FIMSOrderExportImportAdminForm

    def get_actions(self, request):
        actions = super(FIMSOrderExportImportAdmin, self).get_actions(request)
        return actions

    def create_fims_label(self, request, queryset):

       message = ''

       current_order = ''

       airwaybill = ''
       pkgWeight = 0

       #output = pyPdf.PdfFileWriter()
       folder = "FIMSLabels"
       batchLabels = []

       count = 1
       new_batch = False
       for obj in queryset:
            items = []
            order_number = obj.order_number

            if airwaybill is None or len(airwaybill) != 12:
                airwaybill = obj.airwaybill
            has_shipped = obj.has_shipped
            if not has_shipped:
                new_batch = True
            if has_shipped:
                message = message + "Order {} has been shipped before, are you sure you want to ship again?".format(order_number)
                full_filename = os.path.join(settings.MEDIA_ROOT, folder, order_number + '.pdf')
                if not new_batch:
                    batchLabels.append(full_filename)
                continue
            if count == 1:
                current_order = order_number
            #else:
            #    if current_order != order_number:
            #        self.message_user(request, "Please process one order at a time, you selected two orders {} and {}".format(obj.order_number, current_order))
            #        break
            name = obj.name
            address_1 = obj.address_1
            address_2 = obj.address_2 if obj.address_2 else ''
            address_3 = obj.address_3 if obj.address_3 else ''

            if len(address_1) > 35 or len(address_2) > 35 or len(address_3) > 35:
                message = message + "Order {} has an address line longer than 35 characters, please split".format(order_number)
                self.message_user(request,message)
                continue

            city = obj.city if obj.city else ''

            company = obj.company if obj.company else ''
            if len(company) > 35:
                message = message + "Order {} has a company line longer than 35 characters, please split".format(order_number)
                self.message_user(request,message)
                continue

            country = obj.country if obj.country else ''
            phone = obj.phone if obj.phone else ''
            zip = obj.zip if obj.zip else ''
            state = obj.state if obj.state else ''

            if len(city) > 20:
                if len(address_3) > 1:
                    address_3 = address_3 + ','
                address_3 = address_3 + city + ' '
            if len(state) > 10:
                if len(address_3) > 1:
                    address_3 = address_3 + ','
                address_3 = address_3 + city + ' ' + state
            address_3 = address_3[:34] if len(address_3) > 35 else address_3
            email = obj.email if obj.email else ''


            for i in obj.split_items():
                item = {}
                item['item_name'] = i.split('$')[0]
                item['item_price'] = i.split('$')[1] if len(i.split('$')) > 1 else 0
                item['item_weight'] = float(obj.average_weight()) / 16
                items.append(item)

            """
            if (len(obj.item_1()[0]) > 1):
                item = {}
                item['item_name'] = obj.item_1()[0]
                item['item_price'] = obj.item_1()[1] if obj.item_1()[1] else 0
                item['item_weight'] = float(obj.average_weight()) / 16
                items.append(item)


            if (len(obj.item_2()[0]) > 1):
                item2 = {}
                item2['item_name'] = obj.item_2()[0]
                item2['item_price'] = obj.item_2()[1] if obj.item_2()[1] else 0
                item2['item_weight'] = obj.average_weight() / 16
                items.append(item2)

            if (len(obj.item_3()[0]) > 1):
                item3 = {}
                item3['item_name'] = obj.item_3()[0]
                item3['item_price'] = obj.item_3()[1] if obj.item_3()[1] else 0
                item3['item_weight'] = obj.average_weight() / 16
                items.append(item3)

            if (len(obj.item_4()[0]) > 1):
                item4 = {}
                item4['item_name'] = obj.item_4()[0]
                item4['item_price'] = obj.item_4()[1] if obj.item_4()[1] else 0
                item4['item_weight'] = obj.average_weight() / 16
                items.append(item4)

            if (len(obj.item_5()[0]) > 1):
                item5 = {}
                item5['item_name'] = obj.item_5()[0]
                item5['item_price'] = obj.item_5()[1] if obj.item_5()[1] else 0
                item5['item_weight'] = obj.average_weight() / 16
                items.append(item5)

            if (len(obj.item_6()[0]) > 1):
                item6 = {}
                item6['item_name'] = obj.item_6()[0]
                item6['item_price'] = obj.item_6()[1] if obj.item_6()[1] else 0
                item6['item_weight'] = obj.average_weight() / 16
                items.append(item6)
            """

            #pkgWeight = pkgWeight + float(item['item_weight']) * int(obj.item_qty)
            #print "pkgWeight, item_weight, item_qty = {}, {}, {}".format(pkgWeight, obj.item_weight, obj.item_qty)
            pkgWeight = obj.total_weight
            labelType = 41 if float(pkgWeight) < 70.4 else 42

            #print "pkgWeight = {}, labelType = {}".format(pkgWeight, labelType)

            total_amount = obj.total_amount
            currency = "USD"
            if country == "CA":
                currency = "CAD"
            if country == "MX":
                currenty = "MXN"

            count = count + 1


            if order_number:
                 print ("order_number is {}".format(obj.order_number))
            else:
                 self.message_user(request, "order_number false {}".format(obj.order_number))
            if airwaybill is None or len(airwaybill) != 12:
                self.message_user(request, "Order {}: You must enter a valid 12 digit airway bill number: {}".format(order_number, airwaybill))
                continue
            ctx = {
                "airwaybill": airwaybill,
                "order_number": order_number,
                "name": name,
                "address_1": address_1,
                "address_2": address_2,
                "address_3": address_3,
                "city": city,
                "company": company,
                "country": country,
                "phone": phone,
                "zip": zip,
                "state": state,
                "email": email,
                "items": items,
                "pkgWeight": pkgWeight,
                "labelType": labelType,
                "currency": currency
            }
            base_template = "marketplaces/fims.txt"
            feedstr = render_to_string(base_template, ctx)
            feedstr = feedstr.encode('utf-8').strip()
            #print "feedstr =", feedstr



            #from django.views.static import serve
            #import os
            #filepath = '/Users/wangmingye/Downloads/Labels-636535000437113575.pdf'
            #return serve(request, os.path.basename(filepath), os.path.dirname(filepath))


            url = "https://www.shipfims.com/pkgFedex3/pkgFormService"
            headers = {"Accept": "application/xml", 'Referer': "https://shipfims.com"}

            #uncomment in production
            fims_status = requests.post(url, headers=headers, data=feedstr)
            content = fims_status.content
            #print "content = ", content

            #print "Response text = ", fims_status.text
            #print "Response status_code = ", fims_status.status_code

            content = content.decode()
            responseCode = find_between(content,'<responseCode>', '</responseCode>')
            #print "responseCode = ", responseCode
#            if responseCode == '0':
            if responseCode != '1':

                errors = find_between(content, '<errors>', '</errors>')
                #print "errors = ", errors
                self.message_user(request, "Order {}: Something wrong with your order: {} ".format(order_number, errors))
                self.message_user(request, content)
                continue

            parcelId = find_between(content, '<parcelId>', '</parcelId>')
            trackingNo = find_between(content, '<trackingNo>', '</trackingNo>')

            obj.parcelId = parcelId
            obj.trackingNo = trackingNo
            obj.has_shipped = True
            obj.save()
            #self.message_user(request, "Order {}: Label successfully created, ParcelID: {}".format(order_number, parcelId))
            self.message_user(request, "Order {}: Label successfully created, ParcelID: {}".format(order_number,trackingNo))



            bLabel = find_between(content, '<attached_label>', '</attached_label>')
            # create the folder if it doesn't exist.

            full_filename = os.path.join(settings.MEDIA_ROOT, folder, order_number + '.pdf')

            try:
                os.mkdir(os.path.join(settings.MEDIA_ROOT, folder))
            except:
                pass
            try:
                # save the uploaded file inside that folder.
                with open(full_filename, 'wb') as fout:
                    fout.write(base64.b64decode(bLabel))
            except Exception as ex:
                self.message_user(request, "Order {}: Label created, but unable to save the label to a file".format(order_number))
                import traceback
                traceback.print_exc()
                continue


            batchLabels.append(full_filename)


       #self.message_user(request, message)

       #output = PdfFileWriter()
       #for l in batchLabels:
       #     self.append_pdf(PdfFileReader(open(l,"rb")),output)

       from django.views.static import serve
       batch_filename = os.path.join(settings.MEDIA_ROOT, folder, current_order + '_combined.pdf')

       #output.write(open(batch_filename,"wb"))

       mergeFile = PyPDF2.PdfFileMerger()
       for l in batchLabels:
           print ("****l = ", l)
           mergeFile.append(PyPDF2.PdfFileReader(l, 'rb'))

       mergeFile.write(batch_filename)


       if len(batchLabels) > 0:
           return serve(request, os.path.basename(batch_filename), os.path.dirname(batch_filename))


    create_fims_label.short_description = "Create FIMS Label"



admin.site.register(ShipFIMS, FIMSOrderExportImportAdmin)

def build_fba_feed(queryset):
        entries = ''
        for sd in queryset:
                entries += sd.add2amazonfeed()
        if 'flashlight' in sd.get_department.lower():
            if marketplace == "com":
                base_template = 'marketplaces/Amazon_Other_Flashlights_base.txt'
            if marketplace == "ca":
                base_template = 'marketplaces/Amazon_CA_Other_Flashlights_base.txt'
            if marketplace == "mx":
                base_template = 'marketplaces/amazon_mx_outdoors_template_base.txt'
            if marketplace in ["eu", "uk", "de", "it", "es", "fr", "se", "tr"]:
                base_template = 'marketplaces/amazon_uk_sports_flashlightlatern_20190328_base.txt'
            if marketplace == "jp":
                base_template = 'marketplaces/amazon_uk_sports_flashlightlatern_20190328_base.txt'
            if marketplace == "au":
                base_template = 'marketplaces/amazon_au_FlashlightLanterns_base.txt'
            if marketplace == "sg":
                base_template = 'marketplaces/amazon_au_FlashlightLanterns_base.txt'

            if marketplace == "ae":
                base_template = 'marketplaces/amazon_ae_other_flashlight_base.txt'
            if marketplace == "sa":
                base_template = 'marketplaces/amazon_ae_other_flashlight_base.txt'


        if 'science' in sd.get_department.lower():
            base_template = "marketplaces/amazon_labsupplies_template.base.txt"
        feedstr = render_to_string(base_template)
        feedstr += entries
        return feedstr

from ecomstore.settings import AMZN_SP_REFRESH_TOKEN, AMZN_SP_LWA_APP_ID,AMZN_SP_LWA_CLIENT_SECRET


class FBAShipmentAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('products','shipmentid','amazonasin','ean','sku','quantity_shipped','tracking','quantity_received','in_stock_quantity','total_quantity','ship_date','status','reconcile_date',)
    search_fields = ('products','shipmentid', 'asin', 'sku')
    ordering = ['ship_date', 'products', 'reconcile_date', 'status']
    list_editable = ['quantity_received','reconcile_date','status',]
    list_filter = ('status',)

    actions = ['replenish_inventory','query_fba_shipments','query_fba_inventory']

    def replenish_inventory(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd_copy = copy.copy(sd) # (2) django copy object
            sd_copy.id = None   # (3) set 'id' to None to create new object
            sd_copy.shipmentid = "TBD"
            sd_copy.quantity_received = 0
            sd_copy.tracking_number = "TBD"
            sd_copy.status = "readytoship"

            sd_copy.save()    # initial save


            sd_copy.save()  # (7) save the copy to the database for M2M relations



    replenish_inventory.short_description = "Send/Replenish Inventory"

    def Create_Shipment(modeladmin, request, queryset):
        print("create fba button pushed")

    def Get_Shipment_Data(self, request, obj):
        #print("Save Tracking button pushed")
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        from ecomstore import settings
        mws = MWSConnection(settings.AMAZON_MWS_NA_AccessKeyID,settings.AMAZON_MWS_NA_SecretKey, host=settings.AMAZON_MWS_NA_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_NA_MerchantID
        mws.Merchant = settings.AMAZON_MWS_NA_MerchantID

        if 'FBA' in obj.shipmentid:
                ret = mws.get_transport_content(ShipmentId=obj.shipmentid)
                x = ret.GetTransportContentResult.TrackingId
                obj.tracking_number = x
                if x:
                    obj.status = "shipped"
                if not obj.sku:
                    ret = mws.list_inbound_shipment_items(ShipmentId=obj.shipmentid)
                    for x in ret.ListInboundShipmentItemsResult.ItemData:
                        obj.sku = x.SellerSKU
                        obj.quantity_shipped = x.QuantityShipped
                        obj.quantity_received = x.QuantityReceived
                obj.save()
                self.message_user(request, "ShipmentID, tracking: {} {} for sku {} ".format(obj.shipmentid, obj.tracking_number, obj.sku))

    def Get_Inventory_Data(self, request, obj):
        #print("Save Tracking button pushed")
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        from ecomstore import settings
        mws = MWSConnection(settings.AMAZON_MWS_NA_AccessKeyID,settings.AMAZON_MWS_NA_SecretKey, host=settings.AMAZON_MWS_NA_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_NA_MerchantID
        mws.Merchant = settings.AMAZON_MWS_NA_MerchantID

        if obj.sku:
            ret = mws.list_inventory_supply(SellerSkus=(obj.sku,), ResponseGroup='Detailed')
            for x in ret.ListInventorySupplyResult.InventorySupplyList:
                obj.in_stock_quantity = x.InStockSupplyQuantity
                obj.total_quantity = x.TotalSupplyQuantity
                obj.save()
                self.message_user(request, "ASIN/Products: {}/{} --- InStockSupplyQuantity/TotalSupplyQuantity: {}/{}".format(x.ASIN, obj.products, x.InStockSupplyQuantity, x.TotalSupplyQuantity))
        else:
            self.message_user(request, "No SKU found, retrieve the sku data first before run the inventory check")

    change_actions = ('Get_Shipment_Data', 'Get_Inventory_Data',)


    def query_fba_shipments(self, request, queryset):

        from sp_api.api import FulfillmentInbound
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import tempfile
        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        # Initialize the FulfillmentInbound API client
        fulfillment_inbound = FulfillmentInbound(credentials=credentials, marketplace=Marketplaces.US)

        for obj in queryset:
            if 'FBA' in obj.shipmentid:
       	       try:
                  # Retrieve product types
                  response = fulfillment_inbound.shipment_items_by_shipment(shipment_id = obj.shipmentid)
                  payload = response.payload
                  for x in payload["ItemData"]:
                      self.message_user(request, "ShipmentID/SKU: {}/{} Quantity Shipped/Received: {}/{}".format(x["ShipmentId"], x["SellerSKU"], x["QuantityShipped"], x["QuantityReceived"]))
                      obj.quantity_received = x["QuantityReceived"]
                      obj.sku = x["SellerSKU"]
                      obj.save()

                  import json
                  # Specify the file path where you want to write the JSON data
                  file_path = 'shipments.json'

                  # Write the JSON payload to the file
                  with open(file_path, 'w') as json_file:
                     json.dump(payload, json_file, indent=4)

               except SellingApiException as e:
                 print(f"Error submitting feed: {e}")
                 self.message_user(request, "ShipmentID {} Error: {}".format(obj.shipmentid, str(e) ))
                 continue



    query_fba_shipments.short_description = "Query FBA Shipments"

    def query_fba_inventory(self, request, queryset):
        from sp_api.api import Inventories
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import tempfile
        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )


        # Initialize the FulfillmentInbound API client
        inventories = Inventories(credentials=credentials, marketplace=Marketplaces.US)

        for obj in queryset:
            if obj.sku:
                ret = inventories.get_inventory_summary_marketplace(**{"details": True, "sellerSkus": [obj.sku]})
                import json
                # Specify the file path where you want to write the JSON data
                file_path = 'inventory.json'

                # Write the JSON payload to the file
                with open(file_path, 'w') as json_file:
                    json.dump(ret.payload, json_file, indent=4)


                y = ret.payload
                inventory = y["inventorySummaries"][0]

                # Create a custom message with relevant information

                message = "SKU/Products: {}/{}: ".format(inventory['sellerSku'], obj.products)
                self.message_user(request, message)
                x = inventory['inventoryDetails']
                message = "Fulfillable Quantity: {} && inboundWorkingQuantity: {} && inboundShippedQuantity: {} && inboundReceivingQuantity: {}".format(x['fulfillableQuantity'], x['inboundWorkingQuantity'],x['inboundShippedQuantity'],x['inboundReceivingQuantity'])
                self.message_user(request, message)

                z = x['reservedQuantity']
                message = "totalReservedQuantity: {} && pendingCustomerOrderQuantity: {} && pendingTransshipmentQuantity: {} && fcProcessingQuantity: {}".format(z['totalReservedQuantity'], z['pendingCustomerOrderQuantity'],z['pendingTransshipmentQuantity'],z['fcProcessingQuantity'])
                self.message_user(request, message)

                z = x['unfulfillableQuantity']
                message = "totalUnfulfillableQuantity: {} && customerDamagedQuantity: {} && warehouseDamagedQuantity: {} && distributorDamagedQuantity: {} && carrierDamagedQuantity: {} && defectiveQuantity/expiredQuantity: {}".format(z['totalUnfulfillableQuantity'], z['customerDamagedQuantity'],z['warehouseDamagedQuantity'],z['distributorDamagedQuantity'],z['carrierDamagedQuantity'],z['defectiveQuantity'],z['expiredQuantity'])
                self.message_user(request, message)


        #response = HttpResponse(content_type='text/tab-separated-values')
        #response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        #from ecomstore import settings
        #mws = MWSConnection(settings.AMAZON_MWS_NA_AccessKeyID,settings.AMAZON_MWS_NA_SecretKey, host=settings.AMAZON_MWS_NA_ENDPOINT)
        #mws.SellerId = settings.AMAZON_MWS_NA_MerchantID
        #mws.Merchant = settings.AMAZON_MWS_NA_MerchantID


        #for obj in queryset:
        #    if obj.sku:
        #        ret = mws.list_inventory_supply(SellerSkus=(obj.sku,), ResponseGroup='Detailed')
        #        for x in ret.ListInventorySupplyResult.InventorySupplyList:
        #            obj.in_stock_quantity = x.InStockSupplyQuantity
        #            obj.total_quantity = x.TotalSupplyQuantity
        #            obj.save()
        #            self.message_user(request, "ASIN/Products: {}/{} --- InStockSupplyQuantity/TotalSupplyQuantity: {}/{}".format(x.ASIN, obj.products, x.InStockSupplyQuantity, x.TotalSupplyQuantity))






    query_fba_inventory.short_description = "Query FBA Inventory"

admin.site.register(FBAShipment, FBAShipmentAdmin)
