from django.db import models
from stdimage.models import StdImageField
import datetime
from ecomstore.catalog.models import RichTextField

# Create your models here.

class AssetType(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(null=True, blank=True, verbose_name="Equipments, Maintenance, Parts, Services, packing materials, other consumables, etc",)


    created_at = models.DateField(null=True, blank=True)
    updated_at = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Type of Asset"

    def __str__(self):
        return self.name

class Stage(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True,) 

    class Meta:
        verbose_name = "Usage Stage"

    def __str__(self):
        return self.name


PURCHASE_STATUS = (
                  (1, 'NEED TO PURCHASE'),
                  (2, 'RECEIVED'),
                  (3, 'PURCHASED'),
                  (4, 'FOR FUTURE PURCHASE'),
                 )

PERSONNEL = (
                  (1, 'Coleen Conway'),
                  (2, 'Stephen Green'),
                  (3, 'Wangming Ye'),
                 )

CONDITION_TYPE = (
                  ("NEW" , 'NEW'),
                  ("USED" , 'USED'),
                  ("WORKING" , 'WORKING'),
                  ("IN MAINTENANCE" , 'IN MAINTENANCE'),
                 )

RANKING_CHOICES = (
                  (1 , '*****'),
                  (2 , '****'),
                  (3 , '***'),
                  (4 , '**'),
                  (5 , '*'),
                 )

class Procurement(models.Model):
    name = models.CharField(max_length=50, verbose_name="Product Name",)
    description = models.TextField(null=True, blank=True, help_text="Details about this purchase item", verbose_name="purchase description",)
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE, null=True, blank=True,)
    usage = models.CharField(max_length=200, null=True, blank=True,)
    purchase_date = models.DateField(null=True, blank=True, help_text='For an old asset, provide an estimate')
    purchase_price = models.DecimalField(max_digits=9,decimal_places=2, default=0.0,help_text='For an old asset, provide an estimate')
    purchase_quantity = models.IntegerField(default=1)
    condition = models.CharField(max_length=20, default='NEW', choices=CONDITION_TYPE)
    vendor = models.CharField(max_length=50, null=True, blank=True, help_text='This asset was initially purchased from')
    vendor_url = models.CharField(max_length=100, null=True, blank=True)
    vendor_phone_number = models.CharField(max_length=100, null=True, blank=True)
    vendor_email = models.CharField(max_length=100, null=True, blank=True)

    rating = models.PositiveSmallIntegerField(default=1, null=True, choices=RANKING_CHOICES)
    status = models.PositiveSmallIntegerField(default=1, null=True, choices=PURCHASE_STATUS)

    updated_at = models.DateField(default=datetime.date.today)
    requested_by = models.CharField(max_length=20, null=True, blank=True)
    approved_by = models.PositiveSmallIntegerField(null=True, blank=True, choices=PERSONNEL)
    purchased_by = models.PositiveSmallIntegerField(null=True, blank=True, choices=PERSONNEL)

    image1 = StdImageField(upload_to='images/procurement/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    image2 = StdImageField(upload_to='images/procurement/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    receipt1 = models.FileField(upload_to='procurement/',blank=True)
    receipt2 = models.FileField(upload_to='procurement/',blank=True)

    class Meta:
        db_table = 'procurement'
        ordering = ['-purchase_date']
        verbose_name = "Purchase & Procurement"


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def unit_price(self):
        return self.purchase_price/self.purchase_quantity


class Asset(models.Model):
    name = models.CharField(max_length=50)
    description = RichTextField(null=True, blank=True, help_text="Details about this asset item", verbose_name="Asset description",)
    type = models.ForeignKey(AssetType, on_delete=models.CASCADE, null=True, blank=True,)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE, null=True, blank=True,)
    usage = models.CharField(max_length=200, null=True, blank=True,)
    purchase_date = models.DateField(null=True, blank=True, help_text='For an old asset, provide an estimate')
    purchase_price = models.DecimalField(max_digits=9,decimal_places=2, default=0.0,help_text='For an old asset, provide an estimate')
    purchase_quantity = models.IntegerField(default=1)
    condition = models.CharField(max_length=20, default='NEW', choices=CONDITION_TYPE)
    vendor = models.CharField(max_length=50, null=True, blank=True, help_text='This asset was initially purchased from')
    vendor_url = models.CharField(max_length=100, null=True, blank=True)
    vendor_phone_number = models.CharField(max_length=100, null=True, blank=True)
    vendor_email = models.CharField(max_length=100, null=True, blank=True)

    rating = models.PositiveSmallIntegerField(default=1, null=True, choices=RANKING_CHOICES)

    updated_at = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'assets'
        ordering = ['-purchase_date']
        verbose_name = "Equipments & Maintenance"


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    @property
    def unit_price(self):
        return self.purchase_price/self.purchase_quantity


class asset_details(models.Model):
    detail = RichTextField(null=True, blank=True,)
    image = StdImageField(upload_to='images/assets/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    document = models.FileField(upload_to='assets/',blank=True)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)


class asset_service_history(models.Model):
    service_date = models.DateField(default=datetime.date.today)
    description = RichTextField(null=True, blank=True, help_text="Service Details", verbose_name="Service description",)
    image1 = StdImageField(upload_to='images/assets/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})
    image2 = StdImageField(upload_to='images/assets/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})
    image3 = StdImageField(upload_to='images/assets/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})
    image4 = StdImageField(upload_to='images/assets/main', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})
    document1 = models.FileField(upload_to='assets/documents/',blank=True)
    document2 = models.FileField(upload_to='assets/documents/',blank=True)
    document3 = models.FileField(upload_to='assets/documents/',blank=True)
    document4 = models.FileField(upload_to='assets/documents/',blank=True)
    services = models.ForeignKey(Asset, on_delete=models.CASCADE)

