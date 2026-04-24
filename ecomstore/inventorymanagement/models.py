from django.db import models
from stdimage.models import StdImageField
import datetime
from django.db.models import Sum, F, FloatField
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

# Create your models here.

def thumbnail_image_url(a):
        pos = a.rfind('.')
        b = a[:pos] + '.thumbnail.' + a[pos+1:].lower()
        return b

def large_image_url(a):
        pos = a.rfind('.')
        b = a[:pos] + '.large.' + a[pos+1:].lower()
        return b

def super_image_url(a):
        pos = a.rfind('.')
        b = a[:pos] + '.super.' + a[pos+1:].lower()
        return b



class FinishingType(models.Model):
    # raw naterial, unfinished flooring, prefinished inventory, etc
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True,) 


    def __str__(self):
        return self.name
    class Meta:
        db_table = 'heartwoodflooring_finishingtype'
        ordering = ['-name']


class UsageType(models.Model):
    # Beam, Joist, Decking, etc
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True,)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'heartwoodflooring_usagetype'
        ordering = ['-name']


class FinishingGrade(models.Model):
    # Natural Grade, Gold TP Grade, Blue Stain Grad, etc
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True,)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'heartwoodflooring_finishinggrade'
        ordering = ['-name']


GRAIN_ORIENTATION = (
                  ("VERTICAL" , 'VERTICAL GRAIN'),
                  ("HORIZONTAL" , 'HORIZONTAL GRAIN'),
                 )

UNIT_OF_MEASUREMENT = (
                  ("BF" , 'Board Foot'),
                  ("SF" , 'Square Foot'),
                 )

class FinishingPattern(models.Model):
    # Quartersawn, Select, Natural, Character, Antique Southern, etc 
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True,)
    heartwood_content = models.CharField(max_length=50)
    grain_pattern = models.CharField(max_length=50)
    grain_orientation = models.CharField(max_length=50, default="VERTICAL", choices=GRAIN_ORIENTATION)
    density = models.CharField(max_length=50)
    knots = models.CharField(max_length=50)
    nail_holes = models.CharField(max_length=50)
    widths = models.CharField(max_length=50)
    lengths = models.CharField(max_length=50)
    thicknesss = models.CharField(max_length=50)
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'heartwoodflooring_finishingpattern'
        ordering = ['-name']



class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True,) 
    finishing_type = models.ForeignKey(FinishingType, on_delete=models.CASCADE, help_text="raw material, prefinished, etc")
    usage_type = models.ForeignKey(UsageType, on_delete=models.CASCADE, help_text="Beam, decking, joist, etc")
    finishing_grade = models.ForeignKey(FinishingGrade, on_delete=models.CASCADE, help_text="Natural Grade, Blue Stainn Grade, etc")
    finishing_pattern = models.ForeignKey(FinishingPattern, on_delete=models.CASCADE, null=True, blank=True,help_text="Quartersawn, Select, Natural, etc")

    yield_estimate = models.DecimalField(max_digits=9,decimal_places=2, default=0.50,)
    total_quantity = models.CharField(max_length=50, default="0",)
    total_cost = models.CharField(max_length=50, default="USD $0.00",)


    purchase_date = models.DateField(null=True, blank=True, help_text='For an old asset, provide an estimate')
    purchase_price = models.DecimalField(max_digits=9,decimal_places=2, default=0.0,help_text='total')
    purchase_quantity = models.IntegerField(default=1)
    vendor = models.CharField(max_length=100, null=True, blank=True, help_text='This asset was initially purchased from')
    vendor_url = models.CharField(max_length=100, null=True, blank=True)
    vendor_phone_number = models.CharField(max_length=100, null=True, blank=True)
    vendor_email = models.CharField(max_length=100, null=True, blank=True)

    updated_at = models.DateField(default=datetime.date.today)

    class Meta:
        db_table = 'heartwoodflooring_products'
        ordering = ['-name']


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())

    def get_total_cost(self):
        return sum(item.total_value for item in self.items.all())

    def get_unit_of_measurement(self):
        unit = (self.items.all())[0].unit_of_measurement
        for item in self.items.all():
             if unit != item.unit_of_measurement:
                  unit += " OR " + item.unit_of_measurement
                  return unit
        return (self.items.all())[0].get_unit_of_measurement_display()


class product_item(models.Model):
    size = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    unit_of_measurement = models.CharField(max_length=50, default="SF", choices=UNIT_OF_MEASUREMENT)
    cost_per_unit = models.DecimalField(max_digits=9,decimal_places=2, default=0.0,)
    total_value = models.DecimalField(max_digits=9,decimal_places=2, default=0.0,)
    warehouse_location = models.CharField(max_length=100, null=True, blank=True,)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')

    def save(self, *args, **kwargs):
        self.total_value = self.quantity * self.cost_per_unit
        super(product_item, self).save(*args, **kwargs)


# see reference: https://www.py4u.net/discuss/182615
@receiver(pre_save, sender=Product)
def product_pre_save(sender, instance, **kwargs):
    instance.total_cost = str(instance.get_total_cost()) + " ( USD$ )"
    try:
        instance.total_quantity = str(instance.get_total_quantity()) + " ( " + instance.get_unit_of_measurement() + " )"
    except:
        instance.total_quantity = str(instance.get_total_quantity()) + " ( BF or SF )"



def product_item_post_save(sender, instance, **kwargs):
    try:
         instance.product.total_quantity = str(instance.product.get_total_quantity()) + " ( " + instance.product.get_unit_of_measurement() + " ) "
    except:
         instance.product.total_quantity = str(instance.product.get_total_quantity()) + " ( BF or SF ) "

    instance.product.save()

post_save.connect(product_item_post_save, sender=product_item)

class more_detail(models.Model):
    detail = models.TextField(null=True, blank=True,)
    image = StdImageField(upload_to='images/inventorymanagement/', blank=True,
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    document = models.FileField(upload_to='inventorymanagement/',blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def image_tag(self):
        from django.utils.html import escape, mark_safe
        return mark_safe('<a href="%s" target="_blank"><img src="%s" /></a>' % (escape(super_image_url(self.image.url)), escape(large_image_url(self.image.url))))
    image_tag.short_description = 'Image'

