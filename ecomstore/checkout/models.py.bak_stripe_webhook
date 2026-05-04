from django.db import models
from django import forms
from django.contrib.auth.models import User
from ecomstore.catalog.models import Product, Brand
import decimal
from django.urls import reverse
from django.utils.safestring import mark_safe
from ecomstore import settings

from ecomstore.utils import strops
from ecomstore.utils.models import base_country
import logging

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT
from datetime import datetime

COUNTRY_TUPLES = (
    ('US', 'United States of America'),
    ('CA', 'Canada'),
    ('AD', 'AD - Andorra'),
    ('AE', 'AE - United Arab Emirates'),
    ('AF', 'AF - Afghanistan'),
    ('AG', 'AG - Antigua & Barbuda'),
    ('AI', 'AI - Anguilla'),
    ('AL', 'AL - Albania'),
    ('AM', 'AM - Armenia'),
    ('AN', 'AN - Netherlands Antilles'),
    ('AO', 'AO - Angola'),
    ('AQ', 'AQ - Antarctica'),
    ('AR', 'AR - Argentina'),
    ('AS', 'AS - American Samoa'),
    ('AT', 'AT - Austria'),
    ('AU', 'AU - Australia'),
    ('AW', 'AW - Aruba'),
    ('AZ', 'AZ - Azerbaijan'),
    ('BA', 'BA - Bosnia and Herzegovina'),
    ('BB', 'BB - Barbados'),
    ('BD', 'BD - Bangladesh'),
    ('BE', 'BE - Belgium'),
    ('BF', 'BF - Burkina Faso'),
    ('BG', 'BG - Bulgaria'),
    ('BH', 'BH - Bahrain'),
    ('BI', 'BI - Burundi'),
    ('BJ', 'BJ - Benin'),
    ('BM', 'BM - Bermuda'),
    ('BN', 'BN - Brunei Darussalam'),
    ('BO', 'BO - Bolivia'),
    ('BR', 'BR - Brazil'),
    ('BS', 'BS - Bahama'),
    ('BT', 'BT - Bhutan'),
    ('BV', 'BV - Bouvet Island'),
    ('BW', 'BW - Botswana'),
    ('BY', 'BY - Belarus'),
    ('BZ', 'BZ - Belize'),
    ('CC', 'CC - Cocos (Keeling) Islands'),
    ('CF', 'CF - Central African Republic'),
    ('CG', 'CG - Congo'),
    ('CH', 'CH - Switzerland'),
    ('CI', 'CI - Ivory Coast'),
    ('CK', 'CK - Cook Iislands'),
    ('CL', 'CL - Chile'),
    ('CM', 'CM - Cameroon'),
    ('CN', 'CN - China'),
    ('CO', 'CO - Colombia'),
    ('CR', 'CR - Costa Rica'),
    ('CU', 'CU - Cuba'),
    ('CV', 'CV - Cape Verde'),
    ('CX', 'CX - Christmas Island'),
    ('CY', 'CY - Cyprus'),
    ('CZ', 'CZ - Czech Republic'),
    ('DE', 'DE - Germany'),
    ('DJ', 'DJ - Djibouti'),
    ('DK', 'DK - Denmark'),
    ('DM', 'DM - Dominica'),
    ('DO', 'DO - Dominican Republic'),
    ('DZ', 'DZ - Algeria'),
    ('EC', 'EC - Ecuador'),
    ('EE', 'EE - Estonia'),
    ('EG', 'EG - Egypt'),
    ('EH', 'EH - Western Sahara'),
    ('ER', 'ER - Eritrea'),
    ('ES', 'ES - Spain'),
    ('ET', 'ET - Ethiopia'),
    ('FI', 'FI - Finland'),
    ('FJ', 'FJ - Fiji'),
    ('FK', 'FK - Falkland Islands (Malvinas)'),
    ('FM', 'FM - Micronesia'),
    ('FO', 'FO - Faroe Islands'),
    ('FR', 'FR - France'),
    ('FX', 'FX - France, Metropolitan'),
    ('GA', 'GA - Gabon'),
    ('GB', 'GB - United Kingdom (Great Britain)'),
    ('GD', 'GD - Grenada'),
    ('GE', 'GE - Georgia'),
    ('GF', 'GF - French Guiana'),
    ('GH', 'GH - Ghana'),
    ('GI', 'GI - Gibraltar'),
    ('GL', 'GL - Greenland'),
    ('GM', 'GM - Gambia'),
    ('GN', 'GN - Guinea'),
    ('GP', 'GP - Guadeloupe'),
    ('GQ', 'GQ - Equatorial Guinea'),
    ('GR', 'GR - Greece'),
    ('GS', 'GS - South Georgia and the South Sandwich Islands'),
    ('GT', 'GT - Guatemala'),
    ('GU', 'GU - Guam'),
    ('GW', 'GW - Guinea-Bissau'),
    ('GY', 'GY - Guyana'),
    ('HK', 'HK - Hong Kong'),
    ('HM', 'HM - Heard & McDonald Islands'),
    ('HN', 'HN - Honduras'),
    ('HR', 'HR - Croatia'),
    ('HT', 'HT - Haiti'),
    ('HU', 'HU - Hungary'),
    ('ID', 'ID - Indonesia'),
    ('IE', 'IE - Ireland'),
    ('IL', 'IL - Israel'),
    ('IN', 'IN - India'),
    ('IO', 'IO - British Indian Ocean Territory'),
    ('IQ', 'IQ - Iraq'),
    ('IR', 'IR - Islamic Republic of Iran'),
    ('IS', 'IS - Iceland'),
    ('IT', 'IT - Italy'),
    ('JM', 'JM - Jamaica'),
    ('JO', 'JO - Jordan'),
    ('JP', 'JP - Japan'),
    ('KE', 'KE - Kenya'),
    ('KG', 'KG - Kyrgyzstan'),
    ('KH', 'KH - Cambodia'),
    ('KI', 'KI - Kiribati'),
    ('KM', 'KM - Comoros'),
    ('KN', 'KN - St. Kitts and Nevis'),
    ('KP', 'KP - Korea, Democratic People\'s Republic of'),
    ('KR', 'KR - Korea, Republic of'),
    ('KW', 'KW - Kuwait'),
    ('KY', 'KY - Cayman Islands'),
    ('KZ', 'KZ - Kazakhstan'),
    ('LA', 'LA - Lao People\'s Democratic Republic'),
    ('LB', 'LB - Lebanon'),
    ('LC', 'LC - Saint Lucia'),
    ('LI', 'LI - Liechtenstein'),
    ('LK', 'LK - Sri Lanka'),
    ('LR', 'LR - Liberia'),
    ('LS', 'LS - Lesotho'),
    ('LT', 'LT - Lithuania'),
    ('LU', 'LU - Luxembourg'),
    ('LV', 'LV - Latvia'),
    ('LY', 'LY - Libyan Arab Jamahiriya'),
    ('MA', 'MA - Morocco'),
    ('MC', 'MC - Monaco'),
    ('MD', 'MD - Moldova, Republic of'),
    ('MG', 'MG - Madagascar'),
    ('MH', 'MH - Marshall Islands'),
    ('ML', 'ML - Mali'),
    ('MN', 'MN - Mongolia'),
    ('MM', 'MM - Myanmar'),
    ('MO', 'MO - Macau'),
    ('MP', 'MP - Northern Mariana Islands'),
    ('MQ', 'MQ - Martinique'),
    ('MR', 'MR - Mauritania'),
    ('MS', 'MS - Monserrat'),
    ('MT', 'MT - Malta'),
    ('MU', 'MU - Mauritius'),
    ('MV', 'MV - Maldives'),
    ('MW', 'MW - Malawi'),
    ('MX', 'MX - Mexico'),
    ('MY', 'MY - Malaysia'),
    ('MZ', 'MZ - Mozambique'),
    ('NA', 'NA - Namibia'),
    ('NC', 'NC - New Caledonia'),
    ('NE', 'NE - Niger'),
    ('NF', 'NF - Norfolk Island'),
    ('NG', 'NG - Nigeria'),
    ('NI', 'NI - Nicaragua'),
    ('NL', 'NL - Netherlands'),
    ('NO', 'NO - Norway'),
    ('NP', 'NP - Nepal'),
    ('NR', 'NR - Nauru'),
    ('NU', 'NU - Niue'),
    ('NZ', 'NZ - New Zealand'),
    ('OM', 'OM - Oman'),
    ('PA', 'PA - Panama'),
    ('PE', 'PE - Peru'),
    ('PF', 'PF - French Polynesia'),
    ('PG', 'PG - Papua New Guinea'),
    ('PH', 'PH - Philippines'),
    ('PK', 'PK - Pakistan'),
    ('PL', 'PL - Poland'),
    ('PM', 'PM - St. Pierre & Miquelon'),
    ('PN', 'PN - Pitcairn'),
    ('PR', 'PR - Puerto Rico'),
    ('PT', 'PT - Portugal'),
    ('PW', 'PW - Palau'),
    ('PY', 'PY - Paraguay'),
    ('QA', 'QA - Qatar'),
    ('RE', 'RE - Reunion'),
    ('RO', 'RO - Romania'),
    ('RS', 'RS - Serbia'),
    ('RU', 'RU - Russian Federation'),
    ('RW', 'RW - Rwanda'),
    ('SA', 'SA - Saudi Arabia'),
    ('SB', 'SB - Solomon Islands'),
    ('SC', 'SC - Seychelles'),
    ('SD', 'SD - Sudan'),
    ('SE', 'SE - Sweden'),
    ('SG', 'SG - Singapore'),
    ('SH', 'SH - St. Helena'),
    ('SI', 'SI - Slovenia'),
    ('SJ', 'SJ - Svalbard & Jan Mayen Islands'),
    ('SK', 'SK - Slovakia'),
    ('SL', 'SL - Sierra Leone'),
    ('SM', 'SM - San Marino'),
    ('SN', 'SN - Senegal'),
    ('SO', 'SO - Somalia'),
    ('SR', 'SR - Suriname'),
    ('ST', 'ST - Sao Tome & Principe'),
    ('SV', 'SV - El Salvador'),
    ('SY', 'SY - Syrian Arab Republic'),
    ('SZ', 'SZ - Swaziland'),
    ('TC', 'TC - Turks & Caicos Islands'),
    ('TD', 'TD - Chad'),
    ('TF', 'TF - French Southern Territories'),
    ('TG', 'TG - Togo'),
    ('TH', 'TH - Thailand'),
    ('TJ', 'TJ - Tajikistan'),
    ('TK', 'TK - Tokelau'),
    ('TM', 'TM - Turkmenistan'),
    ('TN', 'TN - Tunisia'),
    ('TO', 'TO - Tonga'),
    ('TP', 'TP - East Timor'),
    ('TR', 'TR - Turkey'),
    ('TT', 'TT - Trinidad & Tobago'),
    ('TV', 'TV - Tuvalu'),
    ('TW', 'TW - Taiwan, Province of China'),
    ('TZ', 'TZ - Tanzania, United Republic of'),
    ('UA', 'UA - Ukraine'),
    ('UG', 'UG - Uganda'),
    ('UM', 'UM - United States Minor Outlying Islands'),
    ('UY', 'UY - Uruguay'),
    ('UZ', 'UZ - Uzbekistan'),
    ('VA', 'VA - Vatican City State (Holy See)'),
    ('VC', 'VC - St. Vincent & the Grenadines'),
    ('VE', 'VE - Venezuela'),
    ('VG', 'VG - British Virgin Islands'),
    ('VI', 'VI - United States Virgin Islands'),
    ('VN', 'VN - Viet Nam'),
    ('VU', 'VU - Vanuatu'),
    ('WF', 'WF - Wallis & Futuna Islands'),
    ('WS', 'WS - Samoa'),
    ('YE', 'YE - Yemen'),
    ('YT', 'YT - Mayotte'),
    ('YU', 'YU - Yugoslavia'),
    ('ZA', 'ZA - South Africa'),
    ('ZM', 'ZM - Zambia'),
    ('ZR', 'ZR - Zaire'),
    ('ZW', 'ZW - Zimbabwe'),
    ('ZZ', 'Unknown or unspecified country'),
)

"""""
class ActivePromotionManager(models.Manager):
    def all(self):
        curr = datetime.now()
        return super(ActivePromotionManager, self).all().filter(valid_until__gte=curr).exclude(valid_from__gte=curr)
"""""
class Promotion(models.Model):
    """ model class for storing the shipping methods """
    code = models.CharField(max_length=50, unique=True, help_text='Specify the alpha-numerical promotion or coupon code')
    title = models.CharField(max_length=20, null=True, blank=True,help_text='for the menu. Keep blank if it should not be shown on the menu')
    description = models.CharField(max_length=50, help_text='the description for the promotion')
    discount_amount = models.IntegerField(default=0,
                                    help_text='enter the $$ amount for the discount; discount_amount takes precedences over discount_percentage')
    discount_percentage = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00,
                                    help_text='enter the discount percentage, e.g. if 15%, enter 0.15')
    minimum_price = models.DecimalField(max_digits=9,decimal_places=2,default=0.00,
                                    help_text='enter the minimal price in order for the promotion to be valid')
    valid_from = models.DateTimeField(auto_now=False, help_text='Specify the start date')
    valid_until = models.DateTimeField(auto_now=False, help_text='Specify the end date')
    exclude = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)


    class Meta:
        db_table = 'promotion'
        ordering = ['-valid_until']


    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code



class ProductOnlyPromotion(Promotion):
    """ model class for storing the Product only promotion """

    products = models.ManyToManyField(Product, null=True, blank=True,
                                    help_text='Select all products this promotion applies to')

    class Meta:
        db_table = 'productonly_promotion'
        ordering = ['-valid_until']


    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code

    def all_products(self):
        return ', '.join([c.name for c in self.products.all()])
    all_products.short_description = "products"



class ShippingMethod(models.Model):
    """ model class for storing the shipping methods """
    name = models.CharField(max_length=50, help_text='Specify one of the following delivery methods: Standard, Expedited or Overnight Air Express')
    description = models.CharField(max_length=50, help_text='3-6 business day delivery, next business day delivery, etc')
    carrier = models.CharField(max_length=10, help_text='UPS, USPS, Fedex, etc')
    cutoff_time = models.CharField(max_length=10, help_text='To specify the cutoff time in the day for an order to be shipped on the same day. Example: 12pm')
    shipping_rate = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.15,
                                    help_text='enter the base cost rate for the shipping and handling')


    class Meta:
        db_table = 'shipping_method'
        ordering = ['-name']


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


#countries = base_country.objects.values_list('iso2', 'name_en')

class BaseOrderInfo(models.Model):
    """ base class for storing customer order information """
    class Meta:
        abstract = True

    #contact info
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)

    #shipping information
    shipping_name = models.CharField(max_length=50)
    shipping_address_1 = models.CharField(max_length=50)
    shipping_address_2 = models.CharField(max_length=50, blank=True)
    shipping_city = models.CharField(max_length=50)
    shipping_state = models.CharField(max_length=50, blank=True, null=True, help_text="Optional. For U.S. addresses, use two letter state abbreviations; leave blank if your address does not have a state")
    #shipping_country = models.ForeignKey(base_country, on_delete=models.CASCADE,default = base_country.objects.get(iso2='ZW'))
    shipping_country = models.CharField(max_length=2,choices=COUNTRY_TUPLES, default='US')
    shipping_zip = models.CharField(max_length=10)

    #billing information
    billing_name = models.CharField(max_length=50)
    billing_address_1 = models.CharField(max_length=50)
    billing_address_2 = models.CharField(max_length=50, blank=True)
    billing_city = models.CharField(max_length=50)
    billing_state = models.CharField(max_length=50, blank=True, null=True, help_text="Optional. For U.S. addresses, use two letter state abbreviations; leave blank if your address does not have a state")
    #billing_country = models.ForeignKey(base_country, on_delete=models.CASCADE,default = base_country.objects.get(iso2='ZW'))
    billing_country = models.CharField(max_length=2,choices=COUNTRY_TUPLES, default='US')
    billing_zip = models.CharField(max_length=10)




class Order(BaseOrderInfo):
    """ model class for storing a customer order instance """
    # each individual status
    SUBMITTED = 1
    PROCESSED = 2
    SHIPPED = 3
    CANCELLED = 4
    # set of possible order statuses
    ORDER_STATUSES = ((SUBMITTED,'Submitted'),
                      (PROCESSED,'Processed'),
                      (SHIPPED,'Shipped'),
                      (CANCELLED,'Cancelled'),)
    #order info
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=ORDER_STATUSES, default=SUBMITTED)
    ip_address = models.GenericIPAddressField(default='255.255.255.255')
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    shipping_method = models.ForeignKey(ShippingMethod, null=True, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, blank=True, null=True, on_delete=models.CASCADE)

    #gift information
    isItGift = models.CharField(max_length=5)
    pricePrinted = models.CharField(max_length=5)
    giftmessage = models.CharField(max_length=200)

    #Auction information
    #Now we are overloading the auction_price with the final sales price regardless
    #for the correct and accurate record
    isItAuction = models.BooleanField(default=False)
    auction_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00)

    note = models.CharField(max_length=200, blank=True, null=True)


    #tracking number after product shipment
    tracking = models.CharField(max_length=30, blank=True, null=True)
    ship_date = models.DateTimeField(blank=True, null=True)

    shipping_charged = models.DecimalField(max_digits=9,decimal_places=2,blank=True, null=True)
    invoice_number = models.CharField(max_length=50, blank=True, null=True)




    # MOVED INTO PARENT BaseOrderInfo CLASS IN Chapter 6
    #contact info
    #email = models.EmailField(max_length=50)
    #phone = models.CharField(max_length=20)

    #shipping information
    #shipping_name = models.CharField(max_length=50)
    #shipping_address_1 = models.CharField(max_length=50)
    #shipping_address_2 = models.CharField(max_length=50, blank=True)
    #shipping_city = models.CharField(max_length=50)
    #shipping_state = models.CharField(max_length=2)
    #shipping_country = models.CharField(max_length=50)
    #shipping_zip = models.CharField(max_length=10)

    #billing information
    #billing_name = models.CharField(max_length=50)
    #billing_address_1 = models.CharField(max_length=50)
    #billing_address_2 = models.CharField(max_length=50, blank=True)
    #billing_city = models.CharField(max_length=50)
    #billing_state = models.CharField(max_length=2)
    #billing_country = models.CharField(max_length=50)
    #billing_zip = models.CharField(max_length=10)


    def __str__(self):
        return u'Order #' + str(self.id)

    def __unicode__(self):
        return u'Order #' + str(self.id)

    @property
    def status_str(self):
        if self.status == Order.SUBMITTED:
            return "SUBMITTED"
        elif self.status == Order.CANCELLED:
            return "CANCELLED"
        elif self.status == Order.SHIPPED:
            return "SHIPPED"
        elif self.status == Order.PROCESSED:
            return "PROCESSING"

    @property
    def total(self):
        total = decimal.Decimal('0.00')
        order_items = OrderItem.objects.filter(order=self)
        for item in order_items:
            total += item.total

        return total

    @property
    def discount(self):
        discount = 0.0
        if self.promotion:
            if (self.promotion.minimum_price < self.total) and (self.promotion.discount_amount != 0):
                 discount = self.promotion.discount_amount
            else:
                 if (self.promotion.minimum_price < self.total) and (self.promotion.discount_percentage != 0.0):
                      discount = self.total * self.promotion.discount_percentage
        return discount

    @property
    def shipping_charge(self):
        shipping_rate = self.shipping_method.shipping_rate
        shipping_charge = decimal.Decimal('0.00')
        if self.total < settings.MINIMUM_FOR_FREE and decimal.Decimal(shipping_rate) == float(0.00):
            shipping_charge = float(settings.MINIMUM_POSTAGE)
        else:
            #if decimal.Decimal(shipping_rate) >= float(0.18):
            shipping_charge = self.total * shipping_rate


        return shipping_charge

    @property
    def actual_discount(self):
         if self.auction_price == None or decimal.Decimal('0.00') == self.auction_price:
              # for backward compatibility, prior to May 30, 2015 revision, we did not use the auction_price field to persist the effective sale price
              self.auction_price = self.total
         disc = decimal.Decimal(self.total) - decimal.Decimal(self.auction_price)
         return disc

    @property
    def final_total(self):
         #if self.isItAuction:
         #    f_total = decimal.Decimal(self.auction_price) + decimal.Decimal(self.shipping_charged)
         #    return f_total

         #f_total = decimal.Decimal('0.00')
         #f_total = decimal.Decimal(self.total) - decimal.Decimal(self.discount) + decimal.Decimal(self.shipping_charged)
         f_total = decimal.Decimal(self.total) - decimal.Decimal(self.actual_discount) + decimal.Decimal(self.shipping_charged)
         return f_total



    def get_absolute_url(self):
        return reverse('order_details', kwargs={ 'order_id': self.id })

    def get_absolute_url_invoice(self):
        return reverse('order_details', kwargs={ 'order_id': self.invoice_number })

    @property
    def effective_invoice_number(self):
        if self.invoice_number:
           l = self.invoice_number.find("-")
           return self.invoice_number[l+1:]
        else:
           return self.id

    def shippinglabel(self):
        # for backward compatibility, some orders do not have the random invoice_number
        if self.invoice_number:
            id = self.invoice_number
        else:
            id = self.id
        url = reverse('satchmo_print_shipping', None, None, {'doc' : 'shippinglabel', 'id' : id})
        return mark_safe(u'<a href="%s">%s</a>' % (url, 'View'))
    shippinglabel.allow_tags = True


    def packingslip(self):
        # for backward compatibility, some orders do not have the random invoice_number
        if self.invoice_number:
            id = self.invoice_number
        else:
            id = self.id

        url = reverse('satchmo_print_shipping', None, None, {'doc' : 'packingslip', 'id' : id})
        return mark_safe(u'<a href="%s">%s</a>' % (url, 'View'))
    packingslip.allow_tags = True

    def invoice(self):
        # for backward compatibility, some orders do not have the random invoice_number
        if self.invoice_number:
            id = self.invoice_number
        else:
            id = self.id

        url = reverse('satchmo_print_shipping', None, None, {'doc' : 'invoice', 'id' : id})
        return mark_safe(u'<a href="%s">%s</a>' % (url, 'View'))
    invoice.allow_tags = True

    def all_products(self):
        orderitems = OrderItem.objects.filter(order=self)
        return ', '.join([c.itemunit for c in orderitems])
    all_products.short_description = "products"




class OrderItem(models.Model):
    """ model class for storing each Product instance purchased in each order """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    options = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    @property
    def total(self):
        total = self.quantity * self.price
        try:
           if self.options:
               after = self.options
               while '$' in after:
                   before,op,after = strops.between('$',')',after)
                   total += decimal.Decimal(op) * self.quantity
        except Exception as e:
           logging.error('In calculation the price for optional accessories: %s', e)
        return total

    @property
    def name(self):
        return self.product.name

    @property
    def sku(self):
        return self.product.sku


    def __str__(self):
        return self.product.name + ' (' + self.product.sku + ')'

    def __unicode__(self):
        return self.product.name + ' (' + self.product.sku + ')'

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    @property
    def itemunit(self):
        return self.product.name + '(' + str(self.quantity) + ')'

    @property
    def options_in_array(self):
        return self.options.split(";")



class checkout_audit(models.Model):
    """ model class for storing the shipping methods """

    """ model class for storing each Product instance purchased in each order """
    email = models.CharField(max_length=50, null=True, blank=True)
    stage = models.CharField(max_length=50, null=True, blank=True)
    cart_id = models.CharField(max_length=50, null=True, blank=True)
    ipaddress = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=10, null=True, blank=True, default='Success')

    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email
    class Meta:
        db_table = 'checkout_audit'



class referral(models.Model):
    """ model class for storing the Product only promotion """
    referralCode = models.CharField(max_length=20)
    email = models.CharField(max_length=50, null=True, blank=True)

    orders = models.ManyToManyField(Order, null=True, blank=True,
                                    help_text='All orders referred')


    def __str__(self):
        return self.referralCode

    def __unicode__(self):
        return self.referralCode


class GiftCertificate(models.Model):
    """ model class for storing the shipping methods """
    code = models.CharField(max_length=50, help_text='Specify the alpha-numerical gift certificate code')
    face_value = models.IntegerField(default=0,
                                    help_text='enter the $$ amount for the discount; discount_amount takes precedences over discount_percentage')
    balance = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00,
                                    help_text='enter the discount percentage, e.g. if 15%, enter 0.15')
    value_in_cart = models.DecimalField(max_digits=9,decimal_places=2, blank=True,default=0.00)
    orders_redeemed = models.ManyToManyField(Order, null=True, blank=True)
    from_email = models.CharField(max_length=50, null=True, blank=True)
    to_email = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'giftcertificate'
        ordering = ['-code']


    def __str__(self):
        return self.code

    def __unicode__(self):
        return self.code
