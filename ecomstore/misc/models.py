from django.db import models
from datetime import datetime
from ecomstore.facebooktwitter.views import *

import random, string
from ecomstore.catalog.models import Product, Brand
from ecomstore.utils.barcode_check_digit import add_check_digit_ean
from django.db.models.signals import post_save, post_delete
from ecomstore.caching.caching import cache_update, cache_evict

RANKING_CHOICES = (
                  (1 , '**********'),
                  (2 , '*********'),
                  (3 , '********'),
                  (4 , '*******'),
                  (5 , '******'),
                  (6 , '*****'),
                  (7 , '****'),
                  (8 , '***'),
                  (9 , '**'),
                  (10, '*'),
                 )


class ActiveMessageOfTheDayManager(models.Manager):
    """ Manager class to return only those product reviews where each instance is approved """
    def all(self):
        curr = datetime.now()
        return super(ActiveMessageOfTheDayManager, self).all().filter(end_date__gte=curr).exclude(start_date__gte=curr).order_by('ranking')

class MessageOfTheDay(models.Model):
    title = models.CharField(max_length=200,
                           help_text='e.g, body color; then add the individual choice details')
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)


    active = ActiveMessageOfTheDayManager()


    class Meta:
        db_table = 'messageoftheday'
        ordering = ('description',)

    def __unicode__(self):
        return self.title

    def post2twitter(self):
        message = self.title + ': ' + self.description
        status = updateTwitter(message)
        return status


class Testimonial(models.Model):
    comment = models.TextField(max_length=500, null=True, blank=True)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'testimonial'
        ordering = ['created_at']

    def __unicode__(self):
        return self.name


class BannerControl(models.Model):
    name = models.CharField(max_length=30)
    banner = models.CharField(max_length=100)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    class Meta:
        db_table = 'banner_control'
        ordering = ['name']

    def __unicode__(self):
        return self.name

IN_TRANSIT = 1
DELIVERED = 2
DUTY_PAID = 3

DUTY_STATUSES = ((IN_TRANSIT,'SHIPMENT IN TRANSIT'),
                 (DELIVERED,'SHIPMENT DELIVERED'),
                 (DUTY_PAID,'CUSTOMS DUTY PAID'),)

class Customs_Duty_Tracking(models.Model):
    # each individual status
    # set of possible RMA statuses

    tracking_number = models.CharField(max_length=20)
    pi_number = models.CharField(max_length=20)
    carrier_invoice_number = models.CharField(max_length=20, null=True, blank=True)
    manufacturer = models.CharField(max_length=30, null=True, blank=True)
    carrier = models.CharField(max_length=20, null=True, blank=True)
    shipping_date = models.DateField()
    pi_value = models.CharField(max_length=10)
    declared_value = models.CharField(max_length=10, null=True, blank=True)
    duty_amount = models.CharField(max_length=10, null=True, blank=True)

    duty_status = models.IntegerField(choices=DUTY_STATUSES, default=IN_TRANSIT)
    details = models.TextField()
    closed_date = models.DateField(blank=True, null=True)


    created_at = models.DateField(auto_now=True)


    def __unicode__(self):
        return self.tracking_number
    class Meta:
        db_table = 'customs_duty'
        verbose_name = "Fulfillment Record"

    def order_number(self):
        return self.pi_number
    order_number.short_description = "Order Number"

    def customer_name(self):
        return self.manufacturer
    customer_name.short_description = "Customer Name"

    def product_name(self):
        return self.carrier_invoice_number
    product_name.short_description = "Product Name"

    def sku(self):
        return self.declared_value
    sku.short_description = "SKU"

    def serial_number(self):
        return self.carrier_invoice_number
    serial_number.short_description = "Serial Number"

    def order_amount(self):
        return self.duty_amount
    order_amount.short_description = "Order Amount"


class ean_prefix(models.Model):

    prefix = models.CharField(max_length=7)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.prefix
    class Meta:
        db_table = 'barcode_ean_prefix'

class barcode(models.Model):

    EAN = models.CharField(max_length=13, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_used_by_amazon_com = models.BooleanField(default=False)
    is_used_by_amazon_ca = models.BooleanField(default=False)
    created_at = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.EAN
    class Meta:
        db_table = 'barcode'

    def save(self):
        if not self.EAN:
            pre = ean_prefix.objects.get(brand = self.product.brand)
            ean_seed = pre.prefix
            characters = '0123456789'
            ean_length = 5
            for y in range(ean_length):
                 ean_seed += characters[random.randint(0, len(characters)-1)]
            self.EAN = add_check_digit_ean(ean_seed)
        super(barcode, self).save()


MEDIA_CHOICES = (
                  ('NEWSLETTER' , 'Newsletter'),
                  ('BANNER' , 'Banner'),)

MEDIA_ORDER = (
                  (1 , '1'),
                  (2 , '2'),
                  (3 , '3'),
                  (4 , '4'),
                  (5 , '5'),
                  (6 , '6'),
                  (7 , '7'),
                  (8 , '8'),
                  (9 , '9'),
                  (10 , '10'),)


from stdimage.models import StdImageField
class BannerManager(models.Manager):
    def get_queryset(self):
        return super(BannerManager, self).get_queryset().filter(is_active=True, type='BANNER').order_by('order')

class MediaImage(models.Model):
    type = models.CharField(max_length=20, choices=MEDIA_CHOICES, default='BANNER')
    description = models.CharField(max_length=100, null=True, blank=True)
    url_link = models.CharField(max_length=100, null=True, blank=True)
    order = models.IntegerField(choices=MEDIA_ORDER, default=1)
    is_active = models.BooleanField(default=True)
    image = StdImageField(upload_to='images/misc/',
                          variations={'banner': (1608, 494), 'newsletter': (600,1607, True)})
    created_at = models.DateField(auto_now=True)

    objects = models.Manager()
    active = BannerManager()

    class Meta:
        db_table = 'misc_mediaimage'

    def __unicode__(self):
        return str(self.id)

    @property
    def cache_key(self):
        return "banner_"



post_save.connect(cache_update, sender=MediaImage)
post_delete.connect(cache_evict, sender=MediaImage)

from ecomstore.catalog.models import RichTextField

class TodaysNews(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    url_link = models.CharField(max_length=100, null=True, blank=True)
    embed_video = RichTextField(null=True, blank=True)
    order = models.IntegerField(choices=MEDIA_ORDER, default=1)
    is_active = models.BooleanField(default=True)
    image = StdImageField(null=True, blank=True, upload_to='images/misc/',
                          variations={'banner': (1608, 494), 'newsletter': (600,1607, True)})
    valid_from = models.DateTimeField(auto_now=False, null=True, blank=True, help_text='Specify the start date')
    valid_until = models.DateTimeField(auto_now=False, null=True, blank=True,help_text='Specify the end date')

    created_at = models.DateField(auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = 'misc_todaysnews'

    def __unicode__(self):
        return str(self.id)

    @property
    def cache_key(self):
        return "todaysnews_"
