from django.conf import settings
from django.db import models
from django.template.loader import render_to_string
import logging
from django.core.mail import EmailMessage
from datetime import datetime
from datetime import timedelta
from django.utils.safestring import mark_safe

# Create your models here.

class MyDateTimeField(models.DateTimeField):
    def get_prep_value(value):
        from dateutil.parser import parse
        from datetime import timedelta
        td = float(value[-5:])/100
        timediff = timedelta(hours=td)
        return parse(value).replace(tzinfo=None) - timediff

class AmazonOrder_Excluded(models.Model):
    order_id = models.CharField(max_length=30, unique=True)
    exclude_reason = models.CharField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean() # performs regular validation then clean()
        super(AmazonOrder_Excluded, self).save(*args, **kwargs)


    def clean(self):
        if self.order_id:
            self.order_id = self.order_id.strip()



    def __str__(self):
        return str(self.order_id)

    def __unicode__(self):
        return str(self.order_id)

    class Meta:
        db_table = 'amazon_orders_excluded'

JET_ORDER_STATUS = (
                  ('created' , 'created'),
                  ('ready' , 'ready'),
                  ('acknowledged' , 'acknowledged'),
                  ('inprogress' , 'inprogress'),
                  ('complete', 'complete'),
                 )

JET_ORDER_DIRECTED_CANCEL = (
                  ('yes' , 'yes'),
                  ('no' , 'no'),
                 )

class JETOrder(models.Model):
    status = models.CharField(max_length=20, default='created', choices=JET_ORDER_STATUS)
    order_url = models.CharField(max_length=100)
    directed_cancel = models.CharField(max_length=20, default='no', choices=JET_ORDER_DIRECTED_CANCEL)
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    ship_date = models.DateTimeField(null=True, blank=True)

    merchant_order_id = models.CharField(max_length=50, null=True, blank=True)
    reference_order_id = models.CharField(max_length=50, null=True, blank=True)
    customer_reference_order_id = models.CharField(max_length=50, null=True, blank=True)
    fulfillment_node = models.CharField(max_length=50, null=True, blank=True)
    alt_order_id = models.CharField(max_length=50, null=True, blank=True)
    hash_email = models.CharField(max_length=100, null=True, blank=True)
    exception_state = models.CharField(max_length=50, null=True, blank=True)
    order_placed_date = models.CharField(max_length=100, null=True, blank=True)
    order_transmission_date = models.CharField(max_length=100, null=True, blank=True)
    jet_request_directed_cancel = models.CharField(max_length=10, default="false")


    order_detail_request_shipping_carrier = models.CharField(verbose_name='Request shipping carrier', max_length=20, null=True, blank=True)
    order_detail_request_shipping_method = models.CharField(verbose_name='Request shipping method', max_length=20, null=True, blank=True)
    order_detail_request_service_level = models.CharField(verbose_name='Request service level', max_length=20, null=True, blank=True)
    order_detail_request_ship_by = models.CharField(verbose_name='Request ship by', max_length=40, null=True, blank=True)
    order_detail_request_deliver_by = models.CharField(verbose_name='Request deliver by', max_length=40, null=True, blank=True)

    buyer_name = models.CharField(verbose_name='Name', max_length=30, null=True, blank=True)
    buyer_phone_number = models.CharField(verbose_name='Phone number', max_length=20, null=True, blank=True)

    shipping_to_recipient_name = models.CharField(verbose_name='Recipient name', max_length=30, null=True, blank=True)
    shipping_to_recipient_phone_number = models.CharField(verbose_name='Recipient phone number', max_length=20, null=True, blank=True)
    shipping_to_address_address1 = models.CharField(verbose_name='Recipient address 1',max_length=40, null=True, blank=True)
    shipping_to_address_address2 = models.CharField(verbose_name='Recipient address 2',max_length=40, null=True, blank=True)
    shipping_to_address_city = models.CharField(verbose_name='City',max_length=30, null=True, blank=True)
    shipping_to_address_state = models.CharField(verbose_name='State',max_length=20, null=True, blank=True)
    shipping_to_address_zip_code = models.CharField(verbose_name='Zip code',max_length=20, null=True, blank=True)

    order_totals_item_price_base_price = models.DecimalField(verbose_name='Base price',max_digits=9,decimal_places=2,null=True, blank=True)
    order_totals_item_price_item_tax = models.DecimalField(verbose_name='Item tax',max_digits=9,decimal_places=2,null=True, blank=True)
    order_totals_item_price_item_shipping_cost = models.DecimalField(verbose_name='Item shipping cost',max_digits=9,decimal_places=2,null=True, blank=True)
    order_totals_item_price_item_shipping_tax = models.DecimalField(verbose_name='Item Shipping tax',max_digits=9,decimal_places=2,null=True, blank=True)
    order_totals_item_fees = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    #fee_adjustments not implemented



    def __str__(self):
        return str(self.order_url)
    def __unicode__(self):
        return str(self.order_url)

    class Meta:
        db_table = 'jet_orders'

class JETOrder_Items(models.Model):
    order_item_id = models.CharField(max_length=50, null=True, blank=True)
    alt_order_item_id = models.CharField(max_length=50, null=True, blank=True)
    merchant_sku = models.CharField(max_length=50, null=True, blank=True)
    product_title = models.CharField(max_length=200, null=True, blank=True)
    request_order_quantity = models.IntegerField(default=0, null=True, blank=True)
    request_order_cancel_quantity = models.IntegerField(default=0, null=True, blank=True)
    adjustment_reason = models.CharField(max_length=200, null=True, blank=True)
    item_tax_code = models.CharField(max_length=20, null=True, blank=True)
    url = models.CharField(max_length=200, null=True, blank=True)
    price_adjustment = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    item_fees = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    # item_price not implemented
    # fee_adjustments not implemented
    regulatory_fees = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)

    jet_order = models.ForeignKey(JETOrder, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return str('order_item' + str(self.id))
    def __unicode__(self):
        return str('order_item' + str(self.id))

    class Meta:
        db_table = 'jet_order_items'


JET_RETURN_STATUS = (
                  ('created' , 'created'),
                  ('acknowledge' , 'acknowledge'),
                  ('inprogress' , 'inprogress'),
                  ('completed by merchant', 'completed by merchant'),
                 )

JET_RETURN_REFUND_FEEDBACK = (
                  ('other' , 'other'),
                  ('item damaged' , 'item damaged'),
                  ('not shipped in original packaging' , 'not shipped in original packaging'),
                  ('customer opened item', 'customer opened item'),
                 )

JET_RETURN_CHARGE_FEEDBACK = (
                  ('other' , 'other'),
                  ('outsideMerchantPolicy' , 'outsideMerchantPolicy'),
                  ('notMerchantError' , 'notMerchantError'),
                 )


class JETReturn(models.Model):
    status = models.CharField(max_length=30, default='created', choices=JET_RETURN_STATUS)
    return_url = models.CharField(max_length=100)

    agree_to_return_charge = models.BooleanField(default=False)
    alt_order_id  = models.CharField(max_length=50, null=True, blank=True)
    alt_return_authorization_id  = models.CharField(max_length=50, null=True, blank=True)
    merchant_order_id  = models.CharField(max_length=50, null=True, blank=True)
    merchant_return_authorization_id  = models.CharField(max_length=50, null=True, blank=True)
    merchant_return_charge  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    reference_order_id  = models.CharField(max_length=100, null=True, blank=True)
    reference_return_authorization_id  = models.CharField(max_length=50, null=True, blank=True)
    refund_without_return  = models.BooleanField(default=False)

    return_date  = models.CharField(max_length=100, null=True, blank=True)
    return_status  = models.CharField(max_length=100, null=True, blank=True)
    shipping_carrier  = models.CharField(max_length=50, null=True, blank=True)
    tracking_number   = models.CharField(max_length=50, null=True, blank=True)

    return_charge_feedback   = models.CharField(max_length=30, default='notMerchantError', choices=JET_RETURN_CHARGE_FEEDBACK)



    def __str__(self):
        return str(self.return_url)
    def __unicode__(self):
        return str(self.return_url)

    class Meta:
        db_table = 'jet_returns'

class JETReturn_merchant_skus(models.Model):
    order_item_id = models.CharField(max_length=50, null=True, blank=True)
    alt_order_item_id = models.CharField(max_length=50, null=True, blank=True)
    merchant_sku = models.CharField(max_length=50, null=True, blank=True)

    merchant_sku_title  = models.CharField(max_length=200, null=True, blank=True)
    reason  = models.CharField(max_length=200, null=True, blank=True)

    return_quantity  = models.IntegerField(default=0, null=True, blank=True)
    requested_refund_amount_principal  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    requested_refund_amount_tax  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    requested_refund_amount_shipping_cost  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    requested_refund_amount_shipping_tax  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)

    jet_return = models.ForeignKey(JETReturn, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return str('return_skus' + str(self.order_item_id))

    def __unicode__(self):
        return str('return_skus' + str(self.order_item_id))

    class Meta:
        db_table = 'jet_return_skus'

class JETReturn_items(models.Model):
    order_item_id = models.CharField(max_length=50, null=True, blank=True)
    alt_order_item_id = models.CharField(max_length=50, null=True, blank=True)
    total_quantity_returned  = models.IntegerField(default=0)
    order_return_refund_qty   = models.IntegerField(default=0)
    notes  = models.CharField(max_length=200, null=True, blank=True)
    return_refund_feedback   = models.CharField(max_length=40, default='customer opened item', choices=JET_RETURN_REFUND_FEEDBACK)
    refund_amount_principal  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    refund_amount_tax  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    refund_amount_shipping_cost  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    refund_amount_shipping_tax  = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)

    jet_return = models.ForeignKey(JETReturn, null=True, blank=True, on_delete=models.CASCADE)


    def __str__(self):
        return str('return_item' + str(self.order_item_id))

    def __unicode__(self):
        return str('return_item' + str(self.order_item_id))

    class Meta:
        db_table = 'jet_return_items'



class AmazonOrder(models.Model):
    store = models.CharField(max_length=30, null=True, blank=True, default="andrew-amanda")
    email_sent = models.BooleanField(default=False)
    order_id = models.CharField(max_length=30)
    order_item_id = models.CharField(max_length=30)
    purchase_date = models.CharField(max_length=30)
    payments_date = models.CharField(max_length=30, null=True, blank=True)
    buyer_email = models.EmailField(max_length=50)
    buyer_phone_number = models.CharField(max_length=20, null=True, blank=True)
    sku = models.CharField(max_length=30, null=True, blank=True)
    product_name = models.CharField(max_length=300)
    quantity_purchased = models.IntegerField()
    currency = models.CharField(max_length = 10, null=True, blank=True)
    item_price = models.DecimalField(max_digits=9,decimal_places=2)
    item_tax = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    shipping_price = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    shipping_tax = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    ship_service_level = models.CharField(max_length = 20)
    recipient_name = models.CharField(max_length = 200)
    ship_address_1 = models.CharField(max_length = 200)
    ship_address_2 = models.CharField(max_length = 200, null=True, blank=True)
    ship_address_3 = models.CharField(max_length = 200, null=True, blank=True)
    ship_city = models.CharField(max_length = 50, null=True, blank=True)
    ship_state = models.CharField(max_length = 50, null=True, blank=True)
    ship_postal_code = models.CharField(max_length = 20, null=True, blank=True)
    ship_country = models.CharField(max_length = 30, null=True, blank=True)
    ship_phone_number = models.CharField(max_length = 50, null=True, blank=True)
    item_promotion_discount = models.DecimalField(max_digits=9,decimal_places=2, blank=True, null = True)
    item_promotion_id = models.CharField(max_length=50, blank=True, null = True)
    delivery_start_date = models.CharField(max_length=30, null=True, blank=True)
    delivery_end_date = models.CharField(max_length=30, null=True, blank=True)
    delivery_time_zone = models.CharField(max_length = 10, null=True, blank=True)
    delivery_Instructions = models.CharField(max_length = 200, null=True, blank=True)
    sales_channel = models.CharField(max_length = 20, null=True, blank=True)
    is_business_order = models.BooleanField(default=False)
    purchase_order_number = models.CharField(max_length=30, null=True, blank=True)
    price_designation = models.CharField(max_length=30, null=True, blank=True)
    tracking_number = models.CharField(max_length=25, null=True, blank=True)

    def save(self, *args, **kwargs):
        try:
            self.full_clean() # performs regular validation then clean()
            super(AmazonOrder, self).save(*args, **kwargs)
        except Exception as e:
            pass

    def clean(self):
        if self.order_id:
            self.order_id = self.order_id.strip()
        if self.ship_country:
            self.ship_country = self.ship_country.strip()


    def sendfeedbackrequest(self):
        status = "Not sent: order {}".format(self.order_id)
        try:
           exclude = AmazonOrder_Excluded.objects.get(order_id=self.order_id)
           status = "Excluded: Order {} is excluded".format(exclude.order_id)
           #print status
        except:
            if (self.ship_country == 'US' or self.ship_country == 'CA') and self.email_sent == False:
                 purchase_date = self.purchase_date
                 purchase_date = purchase_date[:10]
                 pDate = datetime.strptime(purchase_date, "%Y-%m-%d")
                 today = datetime.today()
                 waiting_days = today - timedelta(days=14)
                 if self.ship_country == 'CA':
                      waiting_days = today - timedelta(days=30)
                 if pDate < waiting_days:
                      email = self.buyer_email
                      name = self.recipient_name
                      template = "marketplaces/amazonfeedbackrequest.html"
                      from_email = "james@roadtamerus.com"

                      if self.ship_country == 'CA':
                           template = "marketplaces/amazon_ca_feedbackrequest.html"

                      if self.store == 'jetbeamstore':
                           from_email = "sales@jetbeamstore.com"
                           template = "marketplaces/amazon_jetbeamstore_feedbackrequest.html"

                      msg = render_to_string(template, {'email': email, 'name': name, 'product_name': self.product_name, 'order_id': self.order_id})
                      subject = "[important] How did we do? (Amazon order: {})".format(self.order_id)

                      EmailMsg = EmailMessage(subject,msg,from_email,[email],headers={'Reply-To':from_email})
                      EmailMsg.content_subtype = "html"
                      try:
                         EmailMsg.send()
                         status = "Posted: Order {} feedback request sent".format(self.order_id)
                      except Exception as e:
                         status = "Error: Order {} feedback did not post, {}".format(self.order_id, str(e))
                         logging.error("In Exc sending mail to %s -- Error: %s", self.order_id, e)

        return status


    def __str__(self):
        return str(self.order_id)

    def __unicode__(self):
        return str(self.order_id)

    class Meta:
        db_table = 'amazon_orders'

class Amazon_SKU_4_Review(models.Model):
    SKU = models.CharField(max_length=30)
    title = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean() # performs regular validation then clean()
        super(Amazon_SKU_4_Review, self).save(*args, **kwargs)


    def clean(self):
        if self.SKU:
            self.SKU = self.SKU.strip()



    def __str__(self):
        return str(self.SKU)

    def __unicode__(self):
        return str(self.SKU)

    class Meta:
        db_table = 'amazon_sku_4_review'

from ecomstore.catalog.models import RichTextField
class VendorExpressOrder(models.Model):
    order_number = models.CharField(max_length=30)
    order_details = RichTextField()
    total_cost = models.DecimalField(max_digits=9,decimal_places=2)
    tracking = models.CharField(max_length=30)
    shipping_date = models.DateTimeField(auto_now_add=True)
    pay_expected_by = models.DateField()
    actual_payment_date = models.DateField(blank=True, null=True)
    shipping_label = models.FileField(upload_to='vendorexpress/',blank=True)


    def __str__(self):
        return str(self.order_number)

    def __unicode__(self):
        return str(self.order_number)

    class Meta:
        db_table = 'amazon_vendor_express_orders'

class ShipFIMS(models.Model):
    order_number = models.CharField(max_length=30)
    custom_field_1 = models.CharField(max_length=40,blank=True, null=True)
    custom_field_2 = models.CharField(max_length=40,blank=True, null=True)
    custom_field_3 = models.CharField(max_length=40,blank=True, null=True)
    notes_from_buyer = models.CharField(max_length=40,blank=True, null=True)
    notes_internal = models.CharField(max_length=400,blank=True, null=True)
    notes_to_buyer = models.CharField(max_length=40,blank=True, null=True)

    name = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100,blank=True, null=True)
    address_3 = models.CharField(max_length=100,blank=True, null=True)

    city = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=20)
    phone = models.CharField(max_length=20, blank=True, null=True)
    zip = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    #item_name = models.CharField(max_length=100, blank=True, null=True)
    #item_option = models.CharField(max_length=30, blank=True, null=True)
    #item_qty = models.CharField(max_length=10, blank=True, null=True)
    #item_price = models.CharField(max_length=10, blank=True, null=True)
    #item_weight = models.CharField(max_length=10, blank=True, null=True)

    total_amount = models.CharField(max_length=10, blank=True, null=True)

    has_shipped = models.BooleanField(default=False)

    airwaybill = models.CharField(max_length=12, blank=True, null=True)
    parcelId = models.CharField(max_length=20, blank=True, null=True)
    trackingNo = models.CharField(max_length=20, blank=True, null=True)

    total_weight = models.CharField(max_length=20, blank=True, null=True)

    date = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    cost = models.DecimalField(max_digits=5,decimal_places=2,null=True, blank=True)

    amount_paid_by_customer = models.CharField(max_length=10, blank=True, null=True)
    marketplace_name = models.CharField(max_length=10, blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    items_purchased = models.CharField(max_length=400,blank=True, null=True)
    insured_amount = models.CharField(max_length=10, blank=True, null=True)
    customer_claimed = models.BooleanField(default=False)
    customer_refunded = models.BooleanField(default=False)
    insurance_filed = models.BooleanField(default=False)
    parcel_returned = models.BooleanField(default=False)
    parcel_returned_date = models.DateField(blank=True, null=True)







    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'fims_orders'

    def awb(self):
        url = "https://www.fedex.com/apps/fedextrack/?action=track&language=english&tracknumbers={}".format(self.airwaybill)
        return mark_safe(u'<a href="%s" target="_blank">%s</a>' % (url, 'track'))
    awb.allow_tags = True

    def split_items(self):
        try:
            items = self.notes_internal.split(',')
        except:
            err = "Please specify the items of the order in the internal notes"
            items =[err]
        return items

    def items(self):
        it = self.split_items()
        count = 1
        for i in it:
            if count > 1:
                s = s + ',' + i
            else:
                s = i
            count = count + 1
        return s

    def average_weight(self):
        arrSize = len(self.split_items())
        return float(self.total_weight)/arrSize

    def save(self, *args, **kwargs):
        self.notes_internal = self.notes_internal.replace('\n', ',')

        print ("self.itemss = ", self.split_items())
        total_amount = 0
        items = self.split_items()
        item_names = ''
        for i in items:
            try:
                total_amount = total_amount + float(i.split('$')[1])
                item_names = item_names + i.split('$')[0]
            except:
                continue
        self.total_amount = total_amount
        self.items_purchased = item_names

        self.currency = "USD"
        if self.marketplace_name and "JP" in self.marketplace_name:
            self.currency = "YEN"
        if self.marketplace_name and "DE" in self.marketplace_name:
            self.currency = "EURO"
        if self.marketplace_name and "IT" in self.marketplace_name:
            self.currency = "EURO"
        if self.marketplace_name and "ES" in self.marketplace_name:
            self.currency = "EURO"
        if self.marketplace_name and "UK" in self.marketplace_name:
            self.currency = "EURO"
        if self.marketplace_name and "FR" in self.marketplace_name:
            self.currency = "EURO"
        if self.marketplace_name and "CA" in self.marketplace_name:
            self.currency = "Canada CAD"
        if self.marketplace_name and "MX" in self.marketplace_name:
            self.currency = "MXN"

        insured_amount = 0.0
        if self.amount_paid_by_customer:
            insured_amount = float(self.amount_paid_by_customer)
        if self.marketplace_name and "JP" in self.marketplace_name:
            insured_amount = insured_amount * 0.0088
            print ("Insured amount pre-round = ", insured_amount)

        if self.marketplace_name and "CA" in self.marketplace_name:
            insured_amount = insured_amount * 0.75
        if self.marketplace_name and "MX" in self.marketplace_name:
            insured_amount = insured_amount * 0.049
        insured_amount = round(insured_amount, -2)
        self.insured_amount = insured_amount
        print ("insured_amount = ", insured_amount)


        super(ShipFIMS, self).save(*args, **kwargs)

    """
    def item_1(self):
        a = ''
        b = ''
        if self.custom_field_1:
            if '$' in self.custom_field_1:
                a, b = self.custom_field_1.split('$')
            else:
                a = self.custom_field_1
        return [a,b]

    def item_2(self):
        a = ''
        b = ''
        if self.custom_field_2:
            if '$' in self.custom_field_2:
                a, b = self.custom_field_2.split('$')
            else:
                a = self.custom_field_2
        return [a,b]

    def item_3(self):
        a = ''
        b = ''
        if self.custom_field_3:
            if '$' in self.custom_field_3:
                a, b = self.custom_field_3.split('$')
            else:
                a = self.custom_field_3
        return [a,b]

    def item_4(self):
        a = ''
        b = ''
        if self.notes_from_buyer:
            if '$' in self.notes_from_buyer:
                a, b = self.notes_from_buyer.split('$')
            else:
                a = self.notes_from_buyer
        return [a,b]

    def item_5(self):
        a = ''
        b = ''
        if self.notes_internal:
            if '$' in self.notes_internal:
                a, b = self.notes_internal.split('$')
            else:
                a = self.notes_internal
        return [a,b]

    def item_6(self):
        a = ''
        b = ''
        if self.notes_to_buyer:
            if '$' in self.notes_to_buyer:
                a, b = self.notes_to_buyer.split('$')
            else:
                a = self.notes_to_buyer
        return [a,b]


    def save(self, *args, **kwargs):
        print ("self.item_1 = ", self.item_1())
        total_amount = 0
        try:
            total_amount = total_amount + float(self.item_1()[1])
        except:
            pass
        try:
            total_amount = total_amount + float(self.item_2()[1])
        except:
            pass
        try:
            total_amount = total_amount + float(self.item_3()[1])
        except:
            pass
        try:
            total_amount = total_amount + float(self.item_4()[1])
        except:
            pass
        try:
            total_amount = total_amount + float(self.item_5()[1])
        except:
            pass
        try:
            total_amount = total_amount + float(self.item_6()[1])
        except:
            pass

        self.total_amount = total_amount
        print ("Total_amount = ", total_amount)

        super(ShipFIMS, self).save(*args, **kwargs)

    def items(self):
        s = ''
        if len(self.item_1()[0]) > 1:
            s = s + self.item_1()[0]
        if len(self.item_2()[0]) > 1:
            s = s + ', ' + self.item_2()[0]
        if len(self.item_3()[0]) > 1:
            s = s + ', ' + self.item_3()[0]
        if len(self.item_4()[0]) > 1:
            s = s + ', ' + self.item_4()[0]
        if len(self.item_5()[0]) > 1:
            s = s + ', ' + self.item_5()[0]
        if len(self.item_6()[0]) > 1:
            s = s + ', ' + self.item_6()[0]

        print ("Total items = ", s)
        return s

    def average_weight(self):
        s = 0
        if len(self.item_1()[0]) > 1:
            s = s + 1
        if len(self.item_2()[0]) > 1:
            s = s + 1
        if len(self.item_3()[0])>1:
            s = s + 1
        if len(self.item_4()[0])>1:
            s = s + 1
        if len(self.item_5()[0])>1:
            s = s + 1
        if len(self.item_6()[0])>1:
            s = s + 1

        a = float(self.total_weight) / s
        return a

    """

    def shippinglabel(self):
        folder = "FIMSLabels"

        url = "/static/" + folder + "/"+ self.order_number + '.pdf'
        if self.has_shipped:
            status_text = 'View'
        else:
            status_text = "Pending"
        return mark_safe(u'<a href="%s" target="blank">%s</a>' % (url, status_text))
    shippinglabel.allow_tags = True

    def mailviewtracking(self):
        if self.parcelId:
            status_text = self.parcelId
        else:
            status_text = "Pending"
        url = "http://mailviewrecipient.fedex.com/recip_package_summary.aspx?PostalID=" + status_text

        return mark_safe(u'<a href="%s" target="blank">%s</a>' % (url, status_text))
    mailviewtracking.allow_tags = True

    def fedextracking(self):
        if self.parcelId:
            status_text = self.trackingNo
        else:
            status_text = "Pending"
        url = "https://www.fedex.com/apps/fedextrack/?action=track&tracknumbers={}&locale=en_US&cntry_code=us".format(status_text)
        return mark_safe(u'<a href="%s" target="blank">%s</a>' % (url, status_text))
    fedextracking.allow_tags = True


    def fedextracking(self):
        if self.trackingNo:
            status_text = self.trackingNo
        else:
            status_text = "Pending"
        url = "https://www.fedex.com/apps/fedextrack/?action=track&tracknumbers=" + status_text + "&locale=en_US&cntry_code=US"

        return mark_safe(u'<a href="%s" target="blank">%s</a>' % (url, status_text))
    fedextracking.allow_tags = True

FBASHIPMENT_STATUS = (
                  ('proposed' , 'Proposed To List'),
                  ('approved' , 'Approved To List'),
                  ('pendingamazon' , 'Pending Amazon Approval'),
                  ('readytoship' , 'Read To Ship'),
                  ('readytopack' , 'Ready to Pack'),
                  ('holdshipping' , 'Hold Shipping'),
                  ('shipped' , 'Shipped'),
                  ('received' , 'Received'),
                  ('inconsistent' , 'Inconsistent'),
                  ('staleinconsistency', 'Stale Inconsistency'),
                  ('complete', 'Complete'),
                  ('casesubmitted', 'Case Submitted'),
                  ('caseapproved', 'Case Approved'),
                  ('caserejected', 'Case Rejected'),
                  ('inactive', 'Inactive'),
                 )

import re

def is_ups_tracking_number(tracking_number):
    # UPS tracking numbers are typically 18 characters starting with '1Z'
    # This regex will check for that pattern
    pattern = r'^1Z[0-9A-Z]{16}$'

    # Other UPS tracking number formats can also be included here
    # For example: 9-digit, 15-digit, 25-digit formats

    # Using the search function to match the pattern with the tracking number
    if re.search(pattern, tracking_number):
        return True
    else:
        return False



class FBAShipment(models.Model):
    status = models.CharField(max_length=20, default='proposed', choices=FBASHIPMENT_STATUS)
    products = models.CharField(max_length=200)
    asin = models.CharField(max_length=10, null=True, blank=True)
    ean = models.CharField(max_length=13, null=True, blank=True)
    sku = models.CharField(max_length=50, null=True, blank=True)
    quantity_shipped = models.IntegerField(null=True,blank=True)
    weight = models.IntegerField(null=True,blank=True)
    quantity_received = models.IntegerField(null=True,blank=True)
    in_stock_quantity = models.IntegerField(null=True,blank=True)
    total_quantity = models.IntegerField(null=True,blank=True)
    amazon_address = models.CharField(max_length=200, default='CLT2 10240 Old Dowd Rd,Charlotte, NC 28214')
    shipmentid = models.CharField(max_length=20, default='Not yet shipped')
    tracking_number = models.CharField(max_length=50, null=True, blank=True)
    ship_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    ship_date.editable = True
    received_date = models.DateTimeField(null=True, blank=True)
    reconcile_date = models.DateTimeField(null=True, blank=True)
    shipping_label= models.FileField(upload_to='fba/',blank=True)
    fba_label = models.FileField(upload_to='fba/',blank=True)
    barcode = models.FileField(upload_to='fba/',blank=True)

    class Meta:
        db_table = 'fbashipments'

    def tracking(self):
        if self.tracking_number:
            status_text = self.tracking_number
        else:
            status_text = "Pending"
        if is_ups_tracking_number(status_text):
            url = "https://www.ups.com/track?loc=en_US&tracknum=" + status_text
        else:
            url = "https://www.fedex.com/apps/fedextrack/?action=track&tracknumbers=" + status_text + "&locale=en_US&cntry_code=US"

        return mark_safe(u'<a href="%s" target="blank">%s</a>' % (url, status_text))
    tracking.allow_tags = True

    def amazonasin(self):
        if self.asin:
            status_text = self.asin
        else:
            status_text = "Pending"
        url = "https://www.amazon.com/dp/{}?ref=myi_title_dp".format(status_text)

        return mark_safe(u'<a href="%s" target="blank">%s</a>' % (url, status_text))
    amazonasin.allow_tags = True
