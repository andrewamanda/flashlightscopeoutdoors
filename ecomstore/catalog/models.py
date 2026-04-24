from django.db import models
from django.http import Http404
from ecomstore import settings
from django.contrib.auth.models import User
from stdimage.models import StdImageField
import tagging

from django.db.models.signals import post_save, post_delete
from ecomstore.caching.caching import cache_update, cache_evict
import requests
import json
from django.template.loader import render_to_string
from django.urls import reverse

from ecomstore.utils import eBayTrade
from django.contrib.sites.models import Site

from ecomstore.utils.walmartapis import callwalmart
from django.contrib.sites.models import Site
from ecomstore.utils.MPItemFeed import *



from datetime import datetime

from ecomstore.facebooktwitter.views import *


JET_TOKEN_REQUEST = {"user": settings.JET_API_USER, "pass": settings.JET_SECRET}

AMAZON_RESTRICTED_KEYWORDS = {"™","FAST SHIPPING","assault", "»", "Best", "Top-rated", "Risk-free", "Free","guarantee","details","worry-free","TM","wireless","weapon","gun","knife","dizzy","baton","strike","defense","tactical","law", "enforement","18650","21700","20700","cr123","lithium","ion","14500","18350","16340","26650","battery", "batteries"}


"""The possible ratings for each blog entry"""
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

"""The top 6 important product attributes"""
TOP_ATTRIBUTE_CHOICES = (
                  ('LED Type' , 'LED Type'),
                  ('Max Output' , 'Max Output'),
                  ('Min Output' , 'Min Output'),
                  ('Throw Distance' , 'Throw Distance'),
                  ('Battery' , 'Battery'),
                  ('Max Runtime' , 'Max Runtime'),
                  ('Tactical Runtime' , 'Tactical Runtime'),
                  ('Magnification', 'Magnification'),
                  ('Reticle Type', 'Reticle Type'),
                  ('Object Diameter', 'Object Diameter'),
                  ('Tube Diameter', 'Tube Diameter'),
                  ('Eye Relief', 'Eye Relief'),
                  ('Field of View', 'Field of View'),
                  ('Exit Pupil', 'Exit Pupil'),
                  ('MOA', 'MOA'),
                  ('Lens Coating', 'Lens Coating'),
                  ('Lens Diameter', 'Lens Diameter'),
                  ('Length', 'Length'),
                  ('Capacity', 'Capacity'),
                  ('Weight', 'Weight'),
                  ('Input', 'Input'),
                  ('Output', 'Output'),
                  ('Dimension', 'Dimension'),
                 )

def super_image_url(a):
        pos = a.rfind('.')
        b = a[:pos] + '.super.' + a[pos+1:].lower()
        return b

def Webp2Jpeg(image):
        from PIL import Image
        from io import BytesIO
        from django.core.files.uploadedfile import InMemoryUploadedFile
        # Check if the uploaded image is in webp format
        if image and image.name.endswith('.webp'):
            # Open the image using Pillow
            img = Image.open(image)

            # Convert the image to RGB (necessary for JPEG)
            img = img.convert('RGB')

            # Save the image to an in-memory file as JPEG
            output = BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)

            # Create a new InMemoryUploadedFile for the JPEG version
            image = InMemoryUploadedFile(
                output, 'ImageField', f"{image.name.split('.')[0]}.jpg", 'image/jpeg',
                sys.getsizeof(output), None
            )

        return image


def remove_battery_fields(data, mid):
       battery_keys = [
          "battery",
          "number_of_lithium_ion_cells",
          "lithium_battery",
          "number_of_lithium_metal_cells",
          "num_batteries",
          "has_multiple_battery_powered_components",
          "battery_installation_device_type",
       ]

       for key in battery_keys:
         data.pop(key, None)

       data["batteries_required"] = [{"value": False, "marketplace_id": mid}]
       data["batteries_included"] = [{"value": False, "marketplace_id": mid}]

class ActiveDepartmentManager(models.Manager):
    """ Manager class to return only those categories where each instance is active """
    def get_queryset(self):
        return super(ActiveDepartmentManager, self).get_queryset().filter(is_active=True)

class Department(models.Model):
    """ model class containing information about a category in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for department page URL, created automatically from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("SEO Meta Keywords", max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField("SEO Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    image = StdImageField(upload_to='images/departments/main', null=True, blank=True,
                          variations={'large': (500, 500), 'thumbnail': (160, 160, True)})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)

    seo_title = models.CharField("SEO Title",max_length=255, null=True, blank=True)
    seo_og_title = models.CharField("SEO OG Title",max_length=255, null=True, blank=True)
    seo_og_description = models.CharField("SEO OG Description",max_length=300, null=True, blank=True)
    seo_h1_tag = models.CharField("SEO H1 Tag",max_length=255, null=True, blank=True)


    objects = models.Manager()
    active = ActiveDepartmentManager()

    class Meta:
        db_table = 'departments'
        ordering = ['name']
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store', kwargs={ 'department_slug': self.slug })
    @property
    def cache_key(self):
        return self.get_absolute_url()

class ActiveCategoryManager(models.Manager):
    """ Manager class to return only those categories where each instance is active """
    def get_queryset(self):
        return super(ActiveCategoryManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    """ model class containing information about a category in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created automatically from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag')
    ebay_categoryid = models.CharField(max_length=30, blank=True, null=True, help_text='eBay Category ID for API uploading')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)

    seo_title = models.CharField("SEO Title",max_length=255, null=True, blank=True)
    seo_og_title = models.CharField("SEO OG Title",max_length=255, null=True, blank=True)
    seo_og_description = models.CharField("SEO OG Description",max_length=300, null=True, blank=True)
    seo_h1_tag = models.CharField("SEO H1 Tag",max_length=255, null=True, blank=True)


    objects = models.Manager()
    active = ActiveCategoryManager()

    class Meta:
        db_table = 'categories'
        ordering = ['name']
        verbose_name_plural = 'Categories'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('catalog_category', (), { 'category_slug': self.slug })

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))


    @property
    def cache_key(self):
        return self.get_absolute_url()

class ActiveSubCategoryManager(models.Manager):
    """ Manager class to return only those SubCategories where each instance is active """
    def get_queryset(self):
        return super(ActiveSubCategoryManager, self).get_queryset().filter(is_active=True)


class SubCategory(models.Model):
    """ model class containing information about the subcategories in a Category in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for subcategory page URL, created automatically from name.')
    description = models.TextField()
    display_name = models.CharField(max_length=20, null=True, blank=True)
    image = StdImageField(upload_to='images/categories/subcategories', null=True, blank=True,
                          variations={'large': (500, 500), 'thumbnail': (160, 160, True)})
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)

    seo_title = models.CharField("SEO Title",max_length=255, null=True, blank=True)
    seo_og_title = models.CharField("SEO OG Title",max_length=255, null=True, blank=True)
    seo_og_description = models.CharField("SEO OG Description",max_length=300, null=True, blank=True)
    seo_h1_tag = models.CharField("SEO H1 Tag",max_length=255, null=True, blank=True)


    objects = models.Manager()
    active = ActiveSubCategoryManager()

    class Meta:
        db_table = 'category_subcategory'
        ordering = ['name']
        verbose_name_plural = 'Category_SubCategory'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


    #@models.permalink
    #def get_absolute_url(self):
    #    return ('category_subcategory', (), { 'category_slug': self.category.slug, 'subcategory_slug': self.slug })
        # return "/brand/%s/series/%s" % (self.brand.slug, self.slug)

    def get_absolute_url(self):
        return reverse('subcategory', args=(self.category.slug,self.slug,))


    @property
    def cache_key(self):
        return self.get_absolute_url()


class ActiveBrandManager(models.Manager):
    """ Manager class to return only those brands where each instance is active """
    def get_queryset(self):
        return super(ActiveBrandManager, self).get_queryset().filter(is_active=True)

class Brand(models.Model):
    """ model class containing information about a Brand in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for product page URL, created automatically from name.')
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    """ a brand can belong to 3 departments, the ideal way is to use ManyToMany relationship, for future  """
    department_2 = models.ForeignKey(Department, related_name="department_2", null=True, blank=True, on_delete=models.SET_NULL)
    department_3 = models.ForeignKey(Department, related_name="department_3",null=True, blank=True, on_delete=models.SET_NULL)
    department_4 = models.ForeignKey(Department, related_name="department_4",null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    image = StdImageField(upload_to='images/brands/main', null=True, blank=True,
                          variations={'large': (500, 500), 'thumbnail': (160, 160, True)})
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)


    seo_title = models.CharField("SEO Title",max_length=255, null=True, blank=True)
    seo_og_title = models.CharField("SEO OG Title",max_length=255, null=True, blank=True)
    seo_og_description = models.CharField("SEO OG Description",max_length=300, null=True, blank=True)
    seo_h1_tag = models.CharField("SEO H1 Tag",max_length=255, null=True, blank=True)



    objects = models.Manager()
    active = ActiveBrandManager()

    class Meta:
        db_table = 'brands'
        ordering = ['name']
        verbose_name_plural = 'Brands'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('brand_category', (), { 'brand_slug': self.slug })

    def get_absolute_url(self):
        return reverse('brand', args=(self.slug,))


    @property
    def cache_key(self):
        return self.get_absolute_url()

class ActiveBrandSeriesManager(models.Manager):
    """ Manager class to return only those brand series where each instance is active """
    def get_queryset(self):
        return super(ActiveBrandSeriesManager, self).get_queryset().filter(is_active=True)


class Series(models.Model):
    """ model class containing information about the series in a Brand in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for brand series page URL, created automatically from name.')
    display_name = models.CharField(max_length=30, null=True, blank=True,
                            help_text='A short display name for the brand series')
    image = StdImageField(upload_to='images/brands/series', null=True, blank=True,
                          variations={'large': (500, 500), 'thumbnail': (160, 160, True)})
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField(max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField(max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)

    seo_title = models.CharField("SEO Title",max_length=255, null=True, blank=True)
    seo_og_title = models.CharField("SEO OG Title",max_length=255, null=True, blank=True)
    seo_og_description = models.CharField("SEO OG Description",max_length=300, null=True, blank=True)
    seo_h1_tag = models.CharField("SEO H1 Tag",max_length=255, null=True, blank=True)


    objects = models.Manager()
    active = ActiveBrandSeriesManager()

    class Meta:
        db_table = 'brand_series'
        ordering = ['name']
        verbose_name_plural = 'Brand_series'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


    #@models.permalink
    #def get_absolute_url(self):
    #    return ('brand_series', (), { 'brand_slug': self.brand.slug, 'series_slug': self.slug })
        # return "/brand/%s/series/%s" % (self.brand.slug, self.slug)

    def get_absolute_url(self):
        return reverse('series', args=(self.brand.slug, self.slug,))


    @property
    def cache_key(self):
        return self.get_absolute_url()

class ActivePriceRangeManager(models.Manager):
    """ Manager class to return only those brands where each instance is active """
    def get_queryset(self):
        return super(ActivePriceRangeManager, self).get_queryset().filter(is_active=True)

class PriceRange(models.Model):
    """ model class containing information about a Shop By Price ranges in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for price range page URL, created automatically from name.')
    description = models.CharField(max_length=50,
                                     help_text='e.g, $50 - $100')
    is_active = models.BooleanField(default=True)
    min_price = models.DecimalField(max_digits=9,decimal_places=2)
    max_price = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)


    objects = models.Manager()
    active = ActivePriceRangeManager()

    class Meta:
        db_table = 'priceranges'
        ordering = ['name']
        verbose_name_plural = 'PriceRanges'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('price_ranges', kwargs={ 'priceranges_slug': self.slug })

    @property
    def cache_key(self):
        return self.get_absolute_url()


class ActiveBrightnessRangeManager(models.Manager):
    """ Manager class to return only those brands where each instance is active """
    def get_queryset(self):
        return super(ActiveBrightnessRangeManager, self).get_queryset().filter(is_active=True)

class BrightnessRange(models.Model):
    """ model class containing information about a Shop By Brightness ranges in the product catalog """
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
                            help_text='Unique value for Brightness range page URL, created automatically from name.')
    description = models.CharField(max_length=50,
                                     help_text='e.g, 100 - 300 Lumens')
    is_active = models.BooleanField(default=True)
    min_lumens = models.IntegerField()
    max_lumens = models.IntegerField(null=True,blank=True)


    objects = models.Manager()
    active = ActiveBrightnessRangeManager()

    class Meta:
        db_table = 'brightnessranges'
        ordering = ['name']
        verbose_name_plural = 'BrightnessRanges'


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brightness_ranges', kwargs={ 'brightnessranges_slug': self.slug })

    @property
    def cache_key(self):
        return self.get_absolute_url()


class ActiveProductManager(models.Manager):
    """ Manager class to return only those products where each instance is active """
    def get_queryset(self):
        return super(ActiveProductManager, self).get_queryset().filter(is_active=True)

class FeaturedProductManager(models.Manager):
    """ Manager class to return only those products where each instance is featured """
    def get_queryset(self):
        return super(FeaturedProductManager, self).get_queryset().filter(is_active=True).filter(is_featured=True)

class NewArrivalProductManager(models.Manager):
    """ Manager class to return only those products which arrived in the top 10 most recent days """
    def get_queryset(self):
        #return super(NewArrivalProductManager, self).get_queryset().filter(is_active=True).order_by('created_at').reverse()
        return super(NewArrivalProductManager, self).get_queryset().filter(is_new_arrival=True).filter(is_active=True)

class OpenBoxProductManager(models.Manager):
    """ Manager class to return only those products which arrived in the top 10 most recent days """
    def get_queryset(self):
        #return super(NewArrivalProductManager, self).get_queryset().filter(is_active=True).order_by('created_at').reverse()
        return super(OpenBoxProductManager, self).get_queryset().filter(is_openbox=True).filter(is_active=True)


class ClearanceProductManager(models.Manager):
    """ Manager class to return only those products which arrived in the top 10 most recent days """
    def get_queryset(self):
        return super(ClearanceProductManager, self).get_queryset().filter(clearance=True).filter(is_active=True)


class ComingSoonProductManager(models.Manager):
    """ Manager class to return only those products where each instance is featured """
    def get_queryset(self):
        return super(ComingSoonProductManager, self).get_queryset().filter(is_coming_soon=True)


class RichTextField(models.TextField):
    pass


class Product(models.Model):
    """ model class containing more information about a product; instances of this class are what the user
    adds to their shopping cart and can subsequently purchase

    """
    name = models.CharField(max_length=255, unique=True)
    modelNumber = models.CharField(max_length=20, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True,
                            help_text='Unique value for product page URL, created automatically from name.')
    brand = models.CharField(max_length=50)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    old_price = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    inventory_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00)
    weight = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=1.00, help_text='Enter the decimal value in ounces')

    is_active = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_coming_soon = models.BooleanField(default=False)
    is_new_arrival = models.BooleanField(default=False)
    clearance = models.BooleanField(default=False)
    clearance_price = models.DecimalField(max_digits=9,decimal_places=2,
                              blank=True)
    is_openbox = models.BooleanField(default=False)

    is_combo = models.BooleanField(default=False)


    use_18650 = models.BooleanField(default=False)
    use_cr123a = models.BooleanField(default=False)
    use_aa = models.BooleanField(default=False)


    quantity = models.IntegerField()

    full_description = RichTextField(null=True, blank=True,
                     help_text='Use this box to enter the product description and features in rich text format.  SVN revision 1105')

    description = models.TextField(null=True, blank=True, verbose_name="bullet points for Amazon", help_text='Bullet lists, one line per bullet')
    features = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description for Amazon", help_text='Features and descriptions separated by lines')

    max_lumens = models.IntegerField(null=True, blank=True,
                                      help_text='This is for LED Flashlights only, enter the integer number, e.g. 900')

    meta_keywords = models.CharField("Meta Keywords",max_length=255,
                                     help_text='Comma-delimited set of SEO keywords for keywords meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
                                        help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    categories = models.ManyToManyField(Category)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True,
                                        help_text='Some accessories do not have to associate with a brand')
    series = models.ForeignKey(Series, on_delete=models.CASCADE,null=True, blank=True)
    subcategory = models.ManyToManyField(SubCategory, null=True, blank=True)

    # image fields require a varchar(100) in db
    #image_zoom = StdImageField(upload_to='images/products/main', size=(1024,1024), null=True, blank=True)
    #image = StdImageField(upload_to='images/products/main', size=(300,500))
    #thumbnail = StdImageField(upload_to='images/products/thumbnails', size=(120,120))

    image = StdImageField(upload_to='images/products/main',
                          variations={'super': (2024,2048),'large': (439, 438), 'thumbnail': (139, 140, True)})
    #image_zoom = StdImageField(upload_to='images/products/main', size=(1024,1024), null=True, blank=True)
    #thumbnail = StdImageField(upload_to='images/products/thumbnails', size=(120,120), blank=True)

    image_caption = models.CharField(max_length=200, default="Submission ID", blank=True, verbose_name="SubmissionID")

    image_jetbeam = StdImageField(null=True, blank=True,upload_to='images/products/main',
                          variations={'super': (2024,2048),'large': (439, 438), 'thumbnail': (120, 120, True)})
    #bullets_jetbeam_amazon = models.TextField(null=True, blank=True, verbose_name="bullet points for Jetbeam Amazon", help_text='Bullet lists, one line per bullet')
    ranking = models.PositiveSmallIntegerField(default=10, null=True, choices=RANKING_CHOICES)

    seo_title = models.CharField("SEO Title",max_length=500, null=True, blank=True)
    seo_meta_description = models.CharField("SEO Meta Description",max_length=500, null=True, blank=True)
    seo_meta_keyword = models.CharField("SEO Meta Keywords",max_length=500, null=True, blank=True, help_text="Will be used as the 2nd bullet on Amazon")
    seo_og_title = models.CharField("SEO OG Title",max_length=500, null=True, blank=True, help_text="Will be used as the 3nd bullet on Amazon")
    seo_og_description = models.CharField("SEO OG Description",max_length=500, null=True, blank=True, help_text="Will be used as the 1st bullet on Amazon")
    seo_h1_tag = models.CharField("SEO H1 Tag",max_length=500, null=True, blank=True, help_text="Will be used as the 4th bullet on Amazon")





    objects = models.Manager()
    active = ActiveProductManager()
    featured = FeaturedProductManager()
    new_arrivals = NewArrivalProductManager()
    openbox = OpenBoxProductManager()
    coming_soon = ComingSoonProductManager()
    clearance_products = ClearanceProductManager()


    class Meta:
        db_table = 'products'
        ordering = ['-created_at']


    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def as_dict(self):
        return {
             "id": self.id,
             "slug": self.slug,
             "product": self.meta_description,
             "url": self.get_absolute_url(),
             "price": str(self.price),
             "image": super_image_url(self.image.url)
        }

    def save(self, *args, **kwargs):
        self.image = Webp2Jpeg(self.image)

        # Call the original save method
        super().save(*args, **kwargs)

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('catalog_product', (), { 'product_slug': self.slug })

    def get_absolute_url(self):
        return reverse('product', args=(self.slug,))


    @property
    def get_department(self):
        b = self.brand
        d = b.department
        if d:
            slug = str(d.slug)
            return slug
        else:
            return "None"

    @property
    def is_flashlight(self):
        if 'flashlight' in self.get_department.lower():
            return True
        else:
            return False

    @property
    def is_flashlight_by_maxlumen(self):
        if self.max_lumens == None:
            return False
        else:
            return True

    @property
    def demo_price(self):
        """ get the effective price """
        d_price = self.price
        if d_price < self.old_price:
            d_price = self.old_price
        return d_price

    @property
    def sale_price(self):
        """ get the effective price """
        effective_price = self.price
        if self.clearance and self.clearance_price:
            effective_price = self.clearance_price
        else:
            curr = datetime.now()
            deals = self.dealoftheday_set.filter(end_date__gte=curr).exclude(start_date__gte=curr)
            for d in deals:
               if d.quantity > 0:
                  effective_price = d.deal_price

        return effective_price



    def cross_sells(self):
        """ gets other Product instances that have been combined with the current instance in past orders. Includes the orders
        that have been placed by anonymous users that haven't registered
        """
        from ecomstore.checkout.models import Order, OrderItem
        orders = Order.objects.filter(orderitem__product=self)
        order_items = OrderItem.objects.filter(order__in=orders).exclude(product=self)
        products = Product.active.filter(orderitem__in=order_items).distinct()
        return products

    # users who purchased this product also bought....
    def cross_sells_user(self):
        """ gets other Product instances that have been ordered by other registered customers who also ordered the current
        instance. Uses all past orders of each registered customer and not just the order in which the current
        instance was purchased

        """
        from ecomstore.checkout.models import Order, OrderItem
        from django.contrib.auth.models import User
        users = User.objects.filter(order__orderitem__product=self)
        items = OrderItem.objects.filter(order__user__in=users).exclude(product=self)
        products = Product.active.filter(orderitem__in=items).distinct()
        return products

    def cross_sells_hybrid(self):
        """ gets other Product instances that have been both been combined with the current instance in orders placed by
        unregistered customers, and all products that have ever been ordered by registered customers

        """
        import datetime
        curr = datetime.datetime.now( )

        from ecomstore.checkout.models import Order, OrderItem
        from django.db.models import Q
        orders = Order.objects.filter(orderitem__product=self)
        curr = datetime.datetime.now( )

        users = User.objects.filter(order__orderitem__product=self)
        curr = datetime.datetime.now( )

        items = OrderItem.objects.filter( Q(order__in=orders) |
                      Q(order__user__in=users)
                      ).exclude(product=self)

        curr = datetime.datetime.now( )

        products = Product.active.filter(orderitem__in=items).distinct()

        curr = datetime.datetime.now( )

        return products

    def all_categories(self):
        return ', '.join([c.name for c in self.categories.all()])
    all_categories.short_description = "categories"

    def first_category(self):
        return self.categories.all()[0]
    first_category.short_description = "primecategory"

    @property
    def cache_key(self):
        return self.get_absolute_url()


    def additem_to_ebay(self, option):
        import ebaysdk
        from ebaysdk.utils import getNodeText
        from ebaysdk.exception import ConnectionError
        from ebaysdk.trading import Connection
        import traceback
        import os
        import json
        opts = {'debug': False, 'yaml': 'ebay.yaml', 'devid': None, 'certid': None, 'appid': None}
        print ("current dir = ", os.getcwd())
        retMsg = ""
        try:
                categories = self.categories.all()
                first_category = categories[0]

                a_images = []

                if option == "debug":
                    a_images.append("http://" + "www.andrew-amanda.com/" + super_image_url(self.image.url))
                else:
                    a_images.append("http://" + Site.objects.get_current().domain + super_image_url(self.image.url))
                    more_images = self.additionalimages_set.all()

                    for img in more_images[:11]:
                        imageUrl = "http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url)
                        a_images.append(imageUrl)

                if option == "aa":
                    ebay_template = "ebay/andrew-amanda_cleaned.html"
                else:
                    ebay_template = "ebay/flashlight_scope_outdoors_cleaned.html"




                # description = '<br><br>'.join([p.full_description for p in self.products.all()])
                description = '<br>'
                description += '<br><span style=\"margin-left:auto;margin-right:auto;font-size:30px;font-weight:bold\">' + self.name + '</span><br>'
                description += str(self.full_description)

                context_ebay = {'title': self.meta_description, 'description':description}
                ebay_content = render_to_string(ebay_template, context_ebay)
                content = ebay_content
                content = "<![CDATA[" + content + "]]>"

                import os
                dirspot = os.getcwd()
                print ("dirspot****** = ",dirspot)
                title = self.meta_description
                if option == "debug":
                    api = Connection(config_file="ebay.yaml", domain="api.sandbox.ebay.com", timeout=300, debug=True)
                if option == "aa":
                    aa_ebay = dirspot + "/ecomstore/aa_ebay.yaml"
                    api = Connection(config_file=aa_ebay, domain="api.ebay.com", timeout=300, debug=True)
                if option == "fso":
                    fso_ebay = dirspot + "/ecomstore/fso_ebay.yaml"
                    api = Connection(config_file=fso_ebay, domain="api.ebay.com", timeout=300, debug=True)
                    #title = "GlobalShipping-" + title

                nvl = []
                mpn = {"NameValueList": {
                            "Name": "MPN",
                            "Value": self.modelNumber
                        }}
                brand = {"NameValueList": {
                    "Name": "Brand",
                    "Value": self.brand.name
                }}
                nvl.append(mpn)
                nvl.append(brand)

                #https://developer.ebay.com/DevZone/XML/docs/Reference/eBay/AddItem.html#Request.Item.ProductListingDetails.UPC

                request = {
                    "Item": {
                        "Title": "<![CDATA[" + title[:80]  + "]]>",
                        "Country": "US",
                        "Location": "NC",
                        "Site": "US",
                        "ConditionID": "1000",
                        "SKU": self.sku,
                        "PaymentMethods": "PayPal",
                        "PayPalEmailAddress": "paypal@andrew-amanda.com",
                        "PrimaryCategory": {"CategoryID": first_category.ebay_categoryid},
                        "Description": content,
                        "PictureDetails": {"PictureURL": a_images},
                        "ProductListingDetails": {"IncludeeBayProductDetails": "false",
                                "UPC": "Does Not Apply"},
                        "ItemSpecifics": {
                            "NameValueList": [
                                {"Name": "Brand", "Value": self.brand.name},
                                {"Name": "Type", "Value": "Flashlight"},
                                {"Name": "SKU", "Value": self.sku},
                                {"Name": "MPN", "Value": self.modelNumber}
                            ]
                        },

                        "ListingDuration": "GTC",
                        "StartPrice": str(self.price),
                        "Currency": "USD",
                        #"BuyItNowPrice": str(self.price),
                        "BestOfferEnabled": "true",
                        "CategoryMappingAllowed": "true",
                        "ListingType": "FixedPriceItem",
                        "PaymentMethods": "PayPal",
                        "PayPalEmailAddress": "paypal@andrew-amanda.com",
                        "Quantity": "20",
                        "ShipToLocations": "Worldwide",
                        "ReturnPolicy": {
                            "ReturnsAcceptedOption": "ReturnsAccepted",
                            "RefundOption": "MoneyBack",
                            "ReturnsWithinOption": "Days_30",
                            "Description": "If you are not satisfied, return the product in original condition for refund.",
                            "ShippingCostPaidByOption": "Buyer"
                        },
                        "ShippingDetails": {
                            "PaymentInstructions": "1 business days of handling time, usually shipped next day. Make sure your address is correct, especially when shipping to foreign countries.",
                            "ShippingType": "Flat",
                            "ShippingServiceOptions": [{
                                "FreeShipping": "True",
                                "ShippingService": "USPSStandardPost"
                            },
                            {
                                "ShippingServiceCost": u'10.00',
                                "ShippingService": "FedEx2Day"
                            }],
                            "InternationalShippingServiceOption":
                            [{
                                "ShippingServiceCost": u'39.00',
                                "ShipToLocation": "Worldwide",
                                "ShippingServicePriority": 1,
                                "ShippingService": "USPSFirstClassMailInternational"
                            },
                            {
                                "ShippingServiceCost": u'45.00',
                                "ShipToLocation": "Worldwide",
                                "ShippingServicePriority": 2,
                                "ShippingService": "FedExInternationalEconomy"
                            },
                            {
                                "ShippingServiceCost": u'65.00',
                                "ShipToLocation": "Worldwide",
                                "ShippingServicePriority": 3,
                                "ShippingService": "FedExInternationalPriority"
                            }],

                        },
                        "DispatchTimeMax": "1"
                    }
                }

                #IntShip = []
                #IntShip.append('USPSPriorityMailInternational')
                #IntShip.append('USPSPriorityMailInternationalLargeFlatRateBox')
                #request['Item']['ShippingDetails']['ShippingServiceOptions']['InternationalShippingServiceOption'] = IntShip
                #if option == "fso" or option == "debug":
                #    request['Item']['ShippingDetails']['GlobalShipping'] = "true"


                request['Item']['BestOfferDetails'] = {'BestOfferEnabled': 'false'}

                api.execute("AddItem", request)
                return "{} successfully listed on eBay".format(self.name)
        except Exception as ex:
            traceback.print_exc()
            return "Failed to list the item {} on eBay: {}".format(self.name, str(ex))





    def export2walmart(self, market):

        item_url = "https://marketplace.walmartapis.com/v2/feeds?feedType=item"
        action = "POST"

        #item_url = "https://marketplace.walmartapis.com/v2/feeds"
        #action = "GET"



        mpItemFeed = MPItemFeed()
        mpItemFeedHeader = MPItemFeedHeader()
        mpItemFeed.MPItemFeedHeader = mpItemFeedHeader
        mpItemFeed.MPItemFeedHeader.version = "2.1"
        mpItemFeed.MPItemFeedHeader.requestId = "MinSpecElectronics"
        mpItemFeed.MPItemFeedHeader.requestBatchId = "MinSpecElectronics38"

        mpItem = MPItem()

        pyxb.RequireValidWhenGenerating(False)

        mpItem.sku = self.sku

        product = MPProduct()
        #print(product.toxml("utf-8"))
        product.productName = self.name
        product.longDescription = "<![CDATA[" + self.features + "]]>"
        product.shelfDescription = self.meta_keywords
        product.shortDescription = self.meta_description
        product.mainImage = pyxb.BIND()
        product.mainImage.mainImageUrl = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)

        alt_images = []
        a_images = self.additionalimages_set.all()

        slot = 0
        for img in a_images:
            slot += 1
            if slot == 1:
                product.additionalAssets = AdditionalAssets()
                product.additionalAssets.append(pyxb.BIND())
                asset = product.additionalAssets.additionalAsset[-1]
                asset.altText = self.name
                asset.assetUrl = "http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url)
                continue
            itm2 = type(asset)(altText=self.name, assetUrl="http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url))
            product.additionalAssets.additionalAsset.append(itm2)

        product.productIdentifiers = ProductIdentifiers()
        product.productIdentifiers.append(pyxb.BIND())

        # Now pull it off the array and do stuff to it
        itm = product.productIdentifiers.productIdentifier[-1]
        itm.productIdType = 'UPC'

        from ecomstore.utils.barcode_check_digit import generate_upc
        itm.productId = generate_upc()

        #the above can be refered to https://sourceforge.net/p/pyxb/discussion/956708/thread/c3da791a/

        product.productTaxCode = "2038710"

        if 'flashlight' in self.get_department.lower():
            product.SportAndRecreation = SportAndRecreation()
            product.SportAndRecreation.brand = self.brand.name
            product.SportAndRecreation.condition = "Brand New"
            product.SportAndRecreation.manufacturer = self.brand.name
            product.SportAndRecreation.modelNumber = self.name

        mpItem.sku = self.sku
        mpItem.Product = product

        mpItem.price = pyxb.BIND()
        mpItem.price.currency = "USD"
        mpItem.price.amount = self.price


        mpItem.shippingWeight = WeightMeasure()
        mpItem.shippingWeight.value_ = self.weight
        mpItem.shippingWeight.unit = "OZ"




        mpItemFeed.MPItem.append(mpItem)
        print(mpItemFeed.toxml("utf-8"))

        #retMsg = callwalmart(action, item_url, mpItemFeed.toxml("utf-8"))


        testxml = '<MPItemFeed xmlns="http://walmart.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://walmart.com/ MPItem.xsd ">'
        testxml = '<?xml version="1.0" encoding="UTF-8"?><MPItemFeed xmlns="http://walmart.com/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://walmart.com/ MPItem.xsd ">'
        testxml += '<MPItemFeedHeader><version>2.1</version><requestId>29834729834</requestId><requestBatchId>MinSpecElectronics32323</requestBatchId></MPItemFeedHeader>'
        testxml += '<MPItem><sku>10972wsdd29343423</sku><Product>'
        testxml += ' <productName>QVS 1-Foot S-Video Male to 2 S-Video Female Y Cable (CSV2F)</productName><longDescription><![CDATA[<div class="productDescriptionWrapper"> QVS Premium S-Video Mini4 Male to Two Female Splitter Cable CSV2F A/V Device Cables <div class="emptyClear"></div></div>]]></longDescription><shelfDescription><![CDATA[QVS 1-Foot S-Video Male to 2 S-Video Female Y Cable (CSV2F)]]></shelfDescription> <shortDescription>QVS 1-Foot S-Video Male to 2 S-Video Female Y Cable (CSV2F)</shortDescription><mainImage><mainImageUrl>http://images.antonline.com/img-main/500/037229400328.jpg</mainImageUrl>'
        testxml += '</mainImage><productIdentifiers><productIdentifier><productIdType>UPC</productIdType><productId>210354110847</productId></productIdentifier></productIdentifiers><productTaxCode>2038710</productTaxCode><Electronics><brand>QVS</brand><ElectronicsCables></ElectronicsCables></Electronics></Product><price><currency>USD</currency><amount>16.29</amount></price><shippingWeight><value>0.120</value><unit>LB</unit></shippingWeight></MPItem></MPItemFeed>'

        #with open("/Users/wangmingye/Downloads/Test.xml") as myfile:
        #    testxml="".join(line.rstrip() for line in myfile)
        print ("testxml = ", testxml)
        #retMsg = callwalmart(action, item_url, testxml)

        open("walmart.xml", "w").write(mpItemFeed.toxml("utf-8"))
        retMsg = callwalmart(action, item_url, "walmart.xml")

        print (retMsg)
        return retMsg

    def export2walmart_from_template(self, market, token):
        from ecomstore.utils.walmartapis import callwalmart
        from django.contrib.sites.models import Site

        item_url = settings.WM_URL + "feeds?feedType=item"
        action = "POST"


        variables = {}
        template = ''
        if 'flashlight' in self.get_department.lower():
            template = "marketplaces/walmart/flashlight_template.xml"

            variables.update({'requestId':'MinSpecSports'})
            variables.update({'requestBatchId':'MinSpecSports21'})

        from ecomstore.utils.barcode_check_digit import generate_upc

        variables.update({'sku':self.sku})
        variables.update({'productName':self.name})
        #variables.update({'model':self.modelNumber.upper()})
        variables.update({'model':self.slug.upper()})
        variables.update({'productTitle':self.meta_description})

        variables.update({'brand':self.brand.name})

        """
        if self.features:
             desc = self.features
             desc = "<b>Brand new in the manufacturer box</b><br><br><b>" + all_attributes_w_break + "</b><br>" + desc.replace('\n', '<br>').replace('\r', '')
        else:
             description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
             from ecomstore.utils.strops import smart_truncate
             desc = smart_truncate(description, 3900) + " ..."
        """
        description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
        from ecomstore.utils.strops import smart_truncate
        desc = smart_truncate(description, 3900) + " ..."


        variables.update({'description':'<![CDATA[<div class="productDescriptionWrapper">' + desc + '<div class="emptyClear"></div></div>]]>'})
        #variables.update({'shortDescription':self.meta_description})
        #variables.update({'shelfDescription':'<![CDATA[' + self.meta_keywords + ']]>'})


        more_features = []
        bullet_set = False
        if self.description:
             bullets = self.description.splitlines()
             if len(bullets) > 0:
                 bullet_set = True
             if len(bullets) == 1:
                 more_features.append(bullets[0])
             if len(bullets) == 2:
                 more_features.append(bullets[0])
                 more_features.append(bullets[1])
             if len(bullets) == 3:
                 more_features.append(bullets[0])
                 more_features.append(bullets[1])
                 more_features.append(bullets[2])
             if len(bullets) == 4:
                 more_features.append(bullets[0])
                 more_features.append(bullets[1])
                 more_features.append(bullets[2])
                 more_features.append(bullets[3])
             if len(bullets) == 5:
                 more_features.append(bullets[0])
                 more_features.append(bullets[1])
                 more_features.append(bullets[2])
                 more_features.append(bullets[3])
                 more_features.append(bullets[4])

             if len(bullets) > 5:
                 more_features.append(bullets[0])
                 more_features.append(bullets[1])
                 more_features.append(bullets[2])
                 more_features.append(bullets[3])
                 more_features.append(bullets[4])
                 more_features.append(bullets[5])


        if not bullet_set:
                 more_features.append(self.meta_description)

        top_attributes = self.topattributes_set.all()
        for a in top_attributes:
            more_features.append(a.name + ": " + a.value)

        variables.update({'more_features':more_features})


        mainImageUrl = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        more_images = []
        a_images = self.additionalimages_set.all()
        for img in a_images:
            imageUrl = "http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url)
            more_images.append(imageUrl)

        variables.update({'mainImageUrl':mainImageUrl})
        variables.update({'more_images':more_images})

        variables.update({'productId':generate_upc()})
        variables.update({'amount':self.price})
        variables.update({'value':self.weight})

        entry = render_to_string(template, variables)
        entry = entry.replace("&lt;", "<")
        entry = entry.replace("&gt;", ">")
        entry = entry.replace("&quot;", '"')
        entry = entry.replace("nbsp;", '')
        entry = entry.replace("&amp;", ' and ')
        entry = entry.replace("amp;", '')

        entry = entry.replace("Battery:", 'Compatible battery:')

        entry = entry.encode('ascii',errors='ignore')



        retMsg = "Response: "
        open("walmart.xml", "w").write(entry.decode("utf-8"))
        #open("walmart_test.xml", "w").write(entry)

        retMsg = callwalmart(action, token, item_url, "walmart.xml")

        return retMsg


    def walmart_get_item(self, market):
        from ecomstore.utils.walmartapis import callwalmart
        from django.contrib.sites.models import Site

        item_url = "https://marketplace.walmartapis.com/v2/items/" + self.sku
        action = "GET"

        retMsg = callwalmart(action, item_url, "walmart.xml")

        return retMsg


    def export2jet(self, market):
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode

        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        print ("authHeader = " + authHeader)
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        jet_browse_node_id = 19000169
        attribute_id = 50
        if 'flashlight' in self.get_department.lower():
              jet_browse_node_id = 19000169
              attribute_id = 50
        if 'science' in self.get_department.lower():
              jet_browse_node_id = 7000129
              attribute_id = 119
        if 'battery' in self.get_department.lower():
              jet_browse_node_id = 10000002
              attribute_id = 50
        if 'scope' in self.get_department.lower():
              jet_browse_node_id = 17000030
              attribute_id = 119
        if 'strut' in self.get_department.lower():
              jet_browse_node_id = 4000565
              attribute_id = 50

        data = {}
        data['product_title'] = self.meta_description
        data['jet_browse_node_id'] = jet_browse_node_id
        data['multipack_quantity'] = 1

        barcodes = []
        ean = {}
        ean['standard_product_code_type'] = 'EAN'
        b = barcode()
        b.product = self
        b.save()
        ean['standard_product_code'] = b.EAN
        barcodes.append(ean)
        data['standard_product_codes'] = barcodes

        data['brand'] = self.brand.name
        data['manufacturer'] = self.brand.name
        data['mfr_part_number'] = self.sku
        data['product_description'] = self.features[:2000]

        bulletsJet = []
        bullet_set = False
        if self.description:
             bullets = self.description.splitlines()
             if len(bullets) > 0:
                 bullet_set = True
             if len(bullets) == 1:
                 bulletsJet.append(bullets[0][:500])
             if len(bullets) == 2:
                 bulletsJet.append(bullets[0][:500])
                 bulletsJet.append(bullets[1][:500])
             if len(bullets) == 3:
                 bulletsJet.append(bullets[0][:500])
                 bulletsJet.append(bullets[1][:500])
                 bulletsJet.append(bullets[2][:500])
             if len(bullets) == 4:
                 bulletsJet.append(bullets[0][:500])
                 bulletsJet.append(bullets[1][:500])
                 bulletsJet.append(bullets[2][:500])
                 bulletsJet.append(bullets[3][:500])
        if not bullet_set:
                 bulletsJet.append(self.meta_description)
                 bulletsJet.append("We ship all orders within one business day")
        data['bullets'] = bulletsJet

        data['number_units_for_price_per_unit'] = 1
        data['type_of_unit_for_price_per_unit'] = "each"
        data['package_length_inches'] = 8
        data['package_width_inches'] = 6
        data['package_height_inches'] = 4
        data['display_length_inches'] = 6
        data['display_width_inches'] = 5
        data['display_height_inches'] = 3
        data['cpsia_cautionary_statements'] = ["no warning applicable"]
        data['country_of_origin'] = "China"
        data['fulfillment_time'] = 1
        data['msrp'] = float(self.price) + float(self.price) * 0.15
        data['map_price'] = float(self.price) + float(self.price) * 0.15
        data['map_implementation'] = "102"
        data['product_tax_code'] = "Generic Taxable Product"
        data['no_return_fee_adjustment'] = 0.01
        data['exclude_from_fee_adjustments'] = False
        data['ships_alone'] = False

        attributes = []
        attr = {}
        attr['attribute_id'] = attribute_id
        attr['attribute_value'] = '95'
        attr['attribute_value_unit'] = 'Count'
        attributes.append(attr)
        data['attributes_node_specific'] = attributes

        data['main_image_url'] = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        data['swatch_image_url'] = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)

        alt_images = []
        a_images = self.additionalimages_set.all()
        slot = 0
        for img in a_images:
            slot += 1
            if slot == 9:
                break
            attr = {}
            attr['image_slot_id'] = slot
            attr['image_url'] = "http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url)
            alt_images.append(attr)
        data['alternate_images'] = alt_images

        print ("data=" + json.dumps(data))

        sku_url = "https://merchant-api.jet.com/api/merchant-skus/" + self.slug
        testJet = requests.put(sku_url, headers=headers, data=json.dumps(data))

        print ("status code = ", testJet.status_code)
        #print "content = ", testJet.content)
        print ("status = ", testJet.text)

        retMessage = "Load sku: {}, content: {}".format(testJet.status_code, testJet.text)

        price_url = "https://merchant-api.jet.com/api/merchant-skus/" + self.slug + "/price"
        data = {}
        data['price'] = float(self.price)
        testJet = requests.put(price_url, headers=headers, data=json.dumps(data))
        retMessage += "Load Price: {}, content: {}".format(testJet.status_code, testJet.text)

        inventory_url = "https://merchant-api.jet.com/api/merchant-skus/" + self.slug + "/Inventory"
        data = {}
        nodes = []
        node = {}
        node['fulfillment_node_id'] = 'd166608cab3d43b3bf2ce1de7c6860bd'
        node['quantity'] = 1000
        nodes.append(node)
        data['fulfillment_nodes'] = nodes
        testJet = requests.put(inventory_url, headers=headers, data=json.dumps(data))
        retMessage += "Inventory: {}, content: {}".format(testJet.status_code, testJet.text)

        return retMessage

    def updatejetprice(self, market):
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode

        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        print ("authHeader = " + authHeader)
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        price_url = "https://merchant-api.jet.com/api/merchant-skus/" + self.slug + "/price"
        data = {}
        data['price'] = float(self.clearance_price)
        testJet = requests.put(price_url, headers=headers, data=json.dumps(data))
        retMessage = "Load Price: {}, content: {}".format(testJet.status_code, testJet.text)

        return retMessage

    def uploadimages2jet(self, market):
        from django.template.loader import render_to_string
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode

        headers = {"Accept": "application/json"}
        testJet = requests.post("https://merchant-api.jet.com/api/token", data=json.dumps(JET_TOKEN_REQUEST))
        reqJson = json.loads(testJet.text)
        authHeader = "bearer " + reqJson['id_token']
        print ("authHeader = " + authHeader)
        headers = {"Content-Type":"application/json", "Authorization":authHeader}

        data = {}

        data['main_image_url'] = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        data['swatch_image_url'] = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)

        alt_images = []
        a_images = self.additionalimages_set.all()
        slot = 0
        for img in a_images:
            slot += 1
            if slot == 9:
                break
            attr = {}
            attr['image_slot_id'] = slot
            attr['image_url'] = "http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url)
            alt_images.append(attr)
        if len(alt_images) > 0:
            data['alternate_images'] = alt_images

        print ("data=" + json.dumps(data))

        sku_url = "https://merchant-api.jet.com/api/merchant-skus/" + self.slug + "/image"
        testJet = requests.put(sku_url, headers=headers, data=json.dumps(data))

        print ("status code = ", testJet.status_code)
        #print "content = ", testJet.content)
        print ("status = ", testJet.text)

        retMessage = "Load images: {}, content: {}".format(testJet.status_code, testJet.text)

        return retMessage


    def add2globalindustrial(self, market):
        from django.template.loader import render_to_string
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode
        variables = {}
        sku = self.sku
        if not sku.startswith('aa'):
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            sku_length = 7
            sku = 'AA-'
            for y in range(sku_length):
               sku += characters[random.randint(0, sku_length)]
            self.sku = sku
            self.save()

        keywords = ''
        template = ''
        if 'flashlight' in self.get_department.lower():
            template = "marketplaces/globalindustrial/Flashlight_Template_Entries.txt"
            keywords = "LED Flashlights" + ";" + "Headlamps" + ";" + self.meta_description
            variables.update({"brightness":self.max_lumens})
            model = self.name
            model = model.replace(' ', '-')

        if 'science' in self.get_department.lower():
            template = "marketplaces/globalindustrial/Lab_Template_Entries.txt"
            keywords = self.meta_keywords
            sku = self.meta_description
            sku = sku.rsplit(None,1)[1]
            if 'syringe' in self.meta_description.lower():
                 sku = self.name
            model = sku
        variables.update({'sku':sku})
        variables.update({'keywords':keywords})
        brand = self.brand.name
        variables.update({'brand':brand})
        variables.update({'model':model})
        variables.update({'name':self.meta_description})
        if self.features:
             desc = self.features
             desc = self.meta_description + ". " + desc.replace('\n', '. ').replace('\r', '')
        else:
             description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
             #description = remove_html_markup(description)
             soup = BeautifulSoup(description)
             desc = ''
             for str in soup.stripped_strings:
                 desc += str
             from ecomstore.utils.strops import smart_truncate
             desc = smart_truncate(desc, 999) + " ..."
        variables.update({'desc':desc})
        price = self.price
        price = round(price,2)
        variables.update({'price':price})
        last_bullet = "ships out within one business day by Andrew-Amanda"
        bullet_set = False
        if self.description:
             bullets = self.description.splitlines()
             if len(bullets) > 0:
                 bullet_set = True
             features = ""
             for i in range(len(bullets)):
                 features += bullets[i] + ";"
        if not bullet_set:
             features = self.meta_description + ";" + last_bullet
        variables.update({"features":features})
        image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        variables.update({'image_1':image_1})
        a_images = self.additionalimages_set.all()
        if len(a_images) > 0:
           image_2 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[0].a_image.url)
           variables.update({'image_2':image_2})
        if len(a_images) > 1:
           image_3 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[1].a_image.url)
           variables.update({'image_3':image_3})
        if len(a_images) > 2:
           image_4 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[2].a_image.url)
           variables.update({'image_4':image_4})
        if len(a_images) > 3:
           image_5 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[3].a_image.url)
           variables.update({'image_5':image_5})
        if len(a_images) > 4:
           image_6 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[4].a_image.url)
           variables.update({'image_6':image_6})
        if len(a_images) > 5:
           image_7 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[5].a_image.url)
           variables.update({'image_7':image_7})
        if len(a_images) > 6:
           image_8 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[6].a_image.url)
           variables.update({'image_8':image_8})
        if len(a_images) > 7:
           image_9 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[7].a_image.url)
           variables.update({'image_9':image_9})

        import decimal
        msrp = decimal.Decimal(self.price) * decimal.Decimal(1.4)
        variables.update({"msrp": msrp})
        variables.update({"weight": self.weight})

        entry = render_to_string(template, variables)
        entry = entry.replace("&lt;", "<")
        entry = entry.replace("&gt;", ">")
        entry = entry.encode('ascii',errors='ignore')
        return entry

    def amazon_ap_spi_product_data(self, market):

        # Prepare product details
        product_data = {
            "MarketplaceId": "ATVPDKIKX0DER",  # US Marketplace ID
            "ProductType": "ToysAndGames",      # Example product type
            "Brand": "Your Brand Name",
            "Title": "Sample Product Title",
            "Manufacturer": "Your Manufacturer",
            "BulletPoints": [
                "First bullet point",
                "Second bullet point",
                "Third bullet point"
            ],
            "Description": "This is a sample product description.",
            "ItemType": "toy",  # Example item type
            "Images": [
                {
                    "ImageLocation": "https://example.com/image1.jpg",
                    "ImageType": "MAIN"
                },
                {
                    "ImageLocation": "https://example.com/image2.jpg",
                    "ImageType": "PT"
                }
            ],
            "PackageDimensions": {
                "Height": 10.0,
                "Length": 15.0,
                "Width": 5.0,
                "Weight": 2.0
            },
            "Price": {
                "Currency": "USD",
                "Amount": 19.99
            },
            "SKU": "SAMPLE-SKU-123",
            "ASIN": "",  # Leave blank if it's a new product
        }
        return product_data



        from django.template.loader import render_to_string
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from ecomstore.utils.strops import replace_str
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode
        variables = {}
        sku = self.sku
        """
        if not sku.startswith('aa'):
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            sku_length = 7
            sku = 'AA-'
            for y in range(sku_length):
               sku += characters[random.randint(0, sku_length)]
            self.sku = sku
            self.save()
        """

        template = "marketplaces/Amazon_Other_Flashlights_Data.txt"
        if 'flashlight' in self.get_department.lower() or 'scope' in self.get_department.lower():
            template = "marketplaces/Amazon_Other_Flashlights_Data.txt"
            if market == 'ca':
                template = "marketplaces/Amazon_CA_Other_Flashlights_Data.txt"
            if market == 'mx':
                template = "marketplaces/amazon_mx_outdoors_template.txt"
            if market in ["eu", "uk", "de", "it", "es", "fr", "se", "tr"]:
                template = "marketplaces/amazon_uk_sports_flashlightlatern_20190328_data.txt"
            if market == 'jp':
                template = "marketplaces/amazon_uk_sports_flashlightlatern_20190328_data.txt"
            if market == 'au':
                template = "marketplaces/amazon_au_FlashlightLanterns_template.txt"
            if market == 'sg':
                template = "marketplaces/amazon_sg_flashlight_data.txt"

            if market == 'ae':
                template = "marketplaces/amazon_ae_other_flashlight_data.txt"
            if market == 'sa':
                template = "marketplaces/amazon_ae_other_flashlight_data.txt"



            barcode_set = self.barcode_set.all()
            for b in barcode_set:
               ean = b.EAN
               if market == 'ca':
                  b.is_used_by_amazon_ca = True
               else:
                  b.is_used_by_amazon_com = True
               b.save()
            barcode_set = None #this will void the above 7 lines to avoid amazon merge two SKUs based on the same EAN
            if not barcode_set:
               bar = barcode()
               bar.product = self
               if market == 'ca':
                  bar.is_used_by_amazon_ca = True
               else:
                  bar.is_used_by_amazon_com = True
               bar.save()
               ean = bar.EAN
            variables.update({'ean':ean})

        if 'science' in self.get_department.lower():
            template = "marketplaces/amazon_labsupplies_template.txt"
            if market == 'ca':
                template = "marketplaces/Flat.File.LabSupplies.ca.entries.txt"
            variables.update({'item_type_keyword':'science-lab-consumables'})
            sku = self.meta_description
            sku = sku.rsplit(None,1)[1]
        brand = self.brand.name
        if brand.lower() == "nest":
             brand = "Eco-Sensa"
        #if brand.lower() == "nitecore":
        #    brand = "Andrew & Amanda"
        variables.update({'brand':brand})
        model = self.modelNumber
        model = model.replace(' ', '-')
        variables.update({'model':model})

        meta_description = self.meta_description

        meta_description = replace_str(meta_description, "bank", "Charger")
        meta_description = replace_str(meta_description, "cree", "C-ree")
        meta_description = replace_str(meta_description, "osram", "O-sram")
        if market == 'ca':
            meta_description = replace_str(meta_description, "eco-sensa", "")
            meta_description = replace_str(meta_description, "eco-", "")
            meta_description = replace_str(meta_description, "EcoSensa", "")

        for kword in AMAZON_RESTRICTED_KEYWORDS:
            meta_description = replace_str(meta_description, kword, " ")

        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
             sku += "jn"
             variables.update({'name':meta_description + " w/ Exclusive Jetbeam Keychain Light"})
             variables.update({'manufacturer': "Ecosphere"})
        else:
             variables.update({'name':meta_description})
             variables.update({'manufacturer': brand})
        if "nitecore" in brand.lower():
             variables.update({'manufacturer': "SYSMAX Innovations Co., Ltd"})

        # Below two lines will override the above condition for now until we figure out what to do with the Jetbeam store on Amazon
        variables.update({'name':meta_description})
        variables.update({'manufacturer': brand})
        if "nitecore" in brand.lower():
             variables.update({'manufacturer': "SYSMAX Innovations Co., Ltd"})


        variables.update({'sku':sku})
        if self.features:
             desc = self.features
             desc = "<b>" + self.meta_description + "</b><br><br>" + desc.replace('\n', '<br>').replace('\r', '')
        else:
             description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
             #description = remove_html_markup(description)
             soup = BeautifulSoup(description)
             desc = ''
             for str in soup.stripped_strings:
                 desc += str + '<br>'

        desc = replace_str(desc, "bank", "Charger")
        desc = replace_str(desc, "cree", "C-ree")
        desc = replace_str(desc, "osram", "O-sram")

        for kword in AMAZON_RESTRICTED_KEYWORDS:
            desc = replace_str(desc, kword, " ")

        from ecomstore.utils.strops import smart_truncate
        desc = smart_truncate(desc, 1960) + " ..."
        variables.update({'description':desc})
        price = self.price
        import decimal
        if market == 'ca':
             price = decimal.Decimal(price) * decimal.Decimal(1.4)
        if market == 'mx':
             price = decimal.Decimal(price) * decimal.Decimal(20.0)
        if market == 'jp':
             price = decimal.Decimal(price) * decimal.Decimal(130.0)
        if market == 'au':
             price = decimal.Decimal(price) * decimal.Decimal(1.6)
        if market == 'ae':
             price = decimal.Decimal(price + 15) * decimal.Decimal(3.67)
        if market == 'sa':
             price = decimal.Decimal(price + 35) * decimal.Decimal(3.75)
        if market == 'tr':
             price = decimal.Decimal(price + 35) * decimal.Decimal(8.00)
        if market == 'sg':
             price = decimal.Decimal(price) * decimal.Decimal(1.50)
        if market in ["eu", "uk", "de", "it", "es", "fr", "se", "tr"]:
             price = decimal.Decimal(price) * decimal.Decimal(1.25)


        #the above 15 accommodates the max fedex shipping cost we are able to set


        price = round(price,2)
        variables.update({'price':price})
        list_price = decimal.Decimal(price) * decimal.Decimal(1.3)
        variables.update({'list_price':list_price})

        last_bullet = "ships out within one business day"
        if market in ["eu", "uk", "de", "it", "es", "fr", "se", "tr", "jp", "au", "ae", "sa"]:
            last_bullet = "ships out within one business day from United States"

        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
             last_bullet = "Include a free Jetbeam 25 Lumen Keychain Light, exclusively distributed by Jetbeam Store only"
        bullet_set = False
        if self.description:
             description = self.description
             description = replace_str(description, "bank", "Charger")
             description = replace_str(description, "cree", "C-ree")
             description = replace_str(description, "osram", "O-sram")


             for kword in AMAZON_RESTRICTED_KEYWORDS:
                description = replace_str(description, kword, " ")
             bullets = description.splitlines()
             if len(bullets) > 0:
                 bullet_set = True
             if len(bullets) == 1:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':last_bullet})
             if len(bullets) == 2:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':last_bullet})
             if len(bullets) == 3:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':last_bullet})
             if len(bullets) == 4:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':bullets[3]})
             if len(bullets) == 5:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':bullets[3]})
                 variables.update({'bullet_point_5':bullets[4]})
             if len(bullets) > 5:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':bullets[3]})
                 variables.update({'bullet_point_5':bullets[4]})
                 variables.update({'bullet_point_5':bullets[5]})




                 variables.update({'bullet_point_5':last_bullet})
        if not bullet_set:
             variables.update({'bullet_point_1':meta_description})
             variables.update({'bullet_point_2':last_bullet})
        variables.update({'key_1':self.all_categories})
        key_2 = self.meta_description
        key_2 = key_2[:100]
        variables.update({'key_2':key_2})
        a_images = self.additionalimages_set.all()
        if len(a_images) > 0:
           image_2 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[0].a_image.url)
           variables.update({'image_2':image_2})
        if len(a_images) > 1:
           image_3 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[1].a_image.url)
           variables.update({'image_3':image_3})
        if len(a_images) > 2:
           image_4 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[2].a_image.url)
           variables.update({'image_4':image_4})
        if len(a_images) > 3:
           image_5 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[3].a_image.url)
           variables.update({'image_5':image_5})
        if len(a_images) > 4:
           image_6 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[4].a_image.url)
           variables.update({'image_6':image_6})
        if len(a_images) > 5:
           image_7 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[5].a_image.url)
           variables.update({'image_7':image_7})
        if len(a_images) > 6:
           image_8 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[6].a_image.url)
           variables.update({'image_8':image_8})
        if len(a_images) > 7:
           image_9 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[7].a_image.url)
           variables.update({'image_9':image_9})
        amazon_image = None
        for a in a_images:
            try:
                if a.image_caption.lower().find('amazon') != -1:
                    amazon_image = a
            except Exception:
                continue
        if amazon_image:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(amazon_image.a_image.url)
        else:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
            try:
                image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image_jetbeam.url)
            except:
                pass
        variables.update({'image_1':image_1})

        entry = render_to_string(template, variables)
        entry = entry.replace("&lt;", "<")
        entry = entry.replace("&gt;", ">")
        entry = entry.encode('ascii',errors='ignore')
        return entry


    def productdata4spapi(self, market):
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from ecomstore.utils.strops import replace_str
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode
        from decimal import Decimal

        if market == ".com":
            mid = "ATVPDKIKX0DER"

        meta_description = self.meta_description

        meta_description = replace_str(meta_description, "bank", "Charger")
        meta_description = replace_str(meta_description, "cree", "C-ree")
        meta_description = replace_str(meta_description, "osram", "O-sram")
        meta_description = replace_str(meta_description, "wireless", "WL")

        for kword in AMAZON_RESTRICTED_KEYWORDS:
            meta_description = replace_str(meta_description, kword, " ")

        bar = barcode()
        bar.product = self
        if market == 'ca':
            bar.is_used_by_amazon_ca = True
        else:
            bar.is_used_by_amazon_com = True
        bar.save()
        ean = bar.EAN

        manufacturer = self.brand.name
        if "nitecore" in manufacturer.lower():
            manufacturer = "SYSMAX Innovations Co., Ltd"

        if self.features:
             desc = self.features
             desc = "<b>" + self.meta_description + "</b><br><br>" + desc.replace('\n', '<br>').replace('\r', '')
        else:
             description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
             #description = remove_html_markup(description)
             soup = BeautifulSoup(description)
             desc = ''
             for str in soup.stripped_strings:
                 desc += str + '<br>'

        desc = replace_str(desc, "bank", "Charger")
        desc = replace_str(desc, "cree", "C-ree")
        desc = replace_str(desc, "osram", "O-sram")
        desc = replace_str(desc, "wireless", "WL")

        for kword in AMAZON_RESTRICTED_KEYWORDS:
            desc = replace_str(desc, kword, " ")

        from ecomstore.utils.strops import smart_truncate
        desc = smart_truncate(desc, 10000) + " ..."

        title = self.name.upper() + " - " + meta_description
        if len(title) > 200:
            title = title[:200]


        # Define the product data as a JSON object
        product_data = {
            "productType": "FLASHLIGHT",  # Replace with the actual product type
            "requirements": "LISTING",
            "attributes": {
                "item_name": [
                    {
                        "value": title,
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "special_feature": [
                    {
                        "value": "Durable",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Adjustable Light Modes",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "High Power",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Impact Resistant",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Lightweight",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Long Range",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Mountable",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Non Slip Grip",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Portable",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Rechargeable",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Shock Resistant",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Weatherproof",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Dustproof",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "color": [
                    {
                        "value": "Black",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "country_of_origin": [
                    {
                        "value": "US",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "model_name": [
                    {
                        "value": self.modelNumber,
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "list_price": [
                    {
                        "value": self.price * Decimal("1.2"),
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],

                "fulfillment_availability": [
                    {
                        "fulfillment_channel_code": "DEFAULT",
                        "quantity": self.quantity,
                        "marketplace_id": mid
                    }
                ],
                "purchasable_offer": [
                    {
                        "audience": "ALL",
                        "currency": "USD",
                        "start_at": {
                            "value": "2021-07-14T19:56:57.717Z"
                        },
                        "our_price": [
                            {
                                "schedule": [
                                    {
                                        "value_with_tax": self.price,
                                    }
                                ]
                            }
                        ],
                        "marketplace_id": "ATVPDKIKX0DER"
                    },
                ],
                "light_source": [
                   {
                        "marketplace_id": mid,
                        "type": [
                            {
                                "value": "LED",
                                "language_tag": "en_US"
                            }
                        ]
                    }
                ],
                "number_of_items": [
                    {
                        "value": "1",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "item_length_width_height": [
                    {
                        "length": {
                            "unit": "inches",
                            "value": "2"
                        },
                        "width": {
                            "unit": "inches",
                            "value": "1"
                        },
                        "height": {
                            "unit": "inches",
                            "value": "2"
                        }

                    }
                ],
                "item_depth_width_height": [
                    {
                        "depth": {
                            "unit": "inches",
                            "value": "2"
                        },
                        "width": {
                            "unit": "inches",
                            "value": "1"
                        },
                        "height": {
                            "unit": "inches",
                            "value": "2"
                        }

                    }
                ],

                "model_number": [
                    {
                        "value": self.modelNumber,
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "supplier_declared_dg_hz_regulation": [
                    {
                        "value": "not_applicable",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "material": [
                    {
                        "value": "Aluminum",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "externally_assigned_product_identifier": [
                    {
                        "value": ean,
                        "type": "ean",
                        "marketplace_id": mid
                    }
                ],
                "part_number": [
                    {
                        "value": self.modelNumber,
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                #"merchant_suggested_asin": [
                #    {
                #        "value": "B007KQBXN0",
                #        "language_tag": "en_US",
                #        "marketplace_id": mid
                #    }
                #],
                "batteries_required": [
                    {
                        "value": "true",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "battery_installation_device_type": [
                    {
                        "value": "Installed in the device",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],

                "batteries_included": [
                    {
                        "value": "true",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],

                "battery": [
                    {
                        "average_life": [
                            {
                                "unit": "minutes",
                                "value": 60
                            }
                        ],
                        "cell_composition": [
                            {
                                "value": "lithium"
                            }
                        ],
                        "description": [
                            {
                                "language_tag": "en_US",
                                "value": "Lithium"
                            }
                        ],
                        "marketplace_id": mid,
                        "weight": [
                            {
                                "unit": "grams",
                                "value": 2.5
                            }
                        ],

                    }
                ],
                "number_of_lithium_ion_cells": [
                    {
                        "value": 1,
                        "marketplace_id": mid
                    }
                ],
                "lithium_battery": [
                    {
                        "energy_content": [
                            {
                                "value": 2.6,
                                "unit": "watt_hours"
                            }
                        ],
                        "marketplace_id": mid,
                        "packaging": [
                            {
                                "value": "batteries_contained_in_equipment"
                            }
                        ],
                        "weight": [
                            {
                                "value": 0.5,
                                "unit": "grams"
                            }
                        ]
                    }
                ],
                "number_of_lithium_metal_cells": [
                    {
                        "value": 0,
                        "marketplace_id": mid
                    }
                ],
                "number_of_lithium_metal_cells": [
                    {
                        "value": 0,
                        "marketplace_id": mid
                    }
                ],
                "num_batteries": [
                    {
                        "quantity": 1,
                        "type": "lithium_ion",
                        "marketplace_id": mid
                    },
                ],
                "has_multiple_battery_powered_components": [
                    {
                        "value": "No",
                        "marketplace_id": mid
                    },
                ],
                "warranty_description": [
                    {
                        "value": "Manufacturer warranty for 2 years from date of purchase.",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "power_source_type": [
                    {
                        "value": "Battery Powered",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "included_components": [
                    {
                        "value": "The Flashlight",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "Everything included in the original factory box",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "item_package_dimensions": [
                    {
                        "length": {
                            "unit": "inches",
                            "value": "2"
                        },
                        "width": {
                            "unit": "inches",
                            "value": "2"
                        },
                        "height": {
                            "unit": "inches",
                            "value": "3"
                        }

                    }
                ],
                "item_package_weight": [
                    {
                        "marketplace_id": mid,
                        "unit": "pounds",
                        "value": self.weight
                    }
                ],
                #"package_contains_sku": [
                #    {
                #        "marketplace_id": mid,
                #        "quantity": 1,
                #        "sku": self.sku
                #    }
                #],

                "brand": [
                    {
                        "value": self.brand.name,
                        "marketplace_id": mid
                    }
                ],
                "product_description": [
                    {
                        "value": desc,
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                #"bullet_point": [
                #    "Output 2000 Lumen",
                #    "Throw Distance 340 yeard"
                #],
                "manufacturer": [
                    {
                        "value": manufacturer,
                        "marketplace_id": mid
                    }
                ],
                "item_type_keyword": [
                    {
                        "value": "LED Flashlight",
                        "marketplace_id": mid
                    }
                ],
                "generic_keyword": [
                    {
                        "value": "handheld torch; portable flashlight; LED flashlight; outdoor lighting; emergency light; camping gear; rechargeable flashlight",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    },
                    {
                        "value": "tactical torch; high lumens; waterproof flashlight;  portable flashlight; outdoor lighting; survival gear; camping equipment",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],

                "condition_type": [
                    {
                        "value": "new_new",
                        "marketplace_id": mid
                    }
                ],
                "condition_note": [
                    {
                        "value": "This is a brand new product, unopened in the original factory box",
                        "language_tag": "en_US",
                        "marketplace_id": mid
                    }
                ],
                "unit_count": [
                    {
                        "marketplace_id": mid,
                        "value": 1,
                        "type": {
                            "language_tag": "en_US",
                            "value": "Count"
                        }
                    }
                ],


            }
        }

        remove_battery_fields(product_data["attributes"], mid)

        a_images = self.additionalimages_set.all()
        for i, a in enumerate(a_images, start=1):
            if i == 9:
                break
            key = f"other_product_image_locator_{i}"  # Dynamically create the key name
            a_url = "http://" + Site.objects.get_current().domain + super_image_url(a.a_image.url)
            product_data['attributes'][key] = [
                {
                    "media_location": a_url,
                    "marketplace_id": mid
                }
            ]

        amazon_image = None
        for a in a_images:
            try:
                if a.image_caption.lower().find('amazon') != -1:
                    amazon_image = a
            except Exception:
                continue
        if amazon_image:
            main_image_url = "http://" + Site.objects.get_current().domain + super_image_url(amazon_image.a_image.url)
        else:
            main_image_url = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)

        product_data['attributes']["main_product_image_locator"] = [
            {
                "media_location": main_image_url,
                "marketplace_id": mid
            }
        ]



        if 'bullet_point' not in product_data:
            product_data['attributes']['bullet_point'] = []

        last_bullet = "Ships out within one business day from North Carolina"
        bullets = [self.seo_og_description, self.seo_meta_keyword, self.seo_og_title, self.seo_h1_tag, last_bullet]
        for bullet in bullets:
             bullet = replace_str(bullet, "bank", "Charger")
             bullet = replace_str(bullet, "cree", "C-ree")
             bullet = replace_str(bullet, "osram", "O-sram")
             for kword in AMAZON_RESTRICTED_KEYWORDS:
                bullet = replace_str(bullet, kword, " ")
             product_data['attributes']['bullet_point'].append({
                "value": bullet,
                "language_tag": "en_US",  # Assuming language tag is always en_US
                "marketplace_id": mid
             })


        return product_data

    def add2amazonfeed(self, market):
        from django.template.loader import render_to_string
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from ecomstore.utils.strops import replace_str
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode
        variables = {}
        sku = self.sku
        """
        if not sku.startswith('aa'):
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            sku_length = 7
            sku = 'AA-'
            for y in range(sku_length):
               sku += characters[random.randint(0, sku_length)]
            self.sku = sku
            self.save()
        """

        template = "marketplaces/Amazon_Other_Flashlights_Data.txt"
        if 'flashlight' in self.get_department.lower() or 'scope' in self.get_department.lower():
            template = "marketplaces/Amazon_Other_Flashlights_Data.txt"
            if market == 'ca':
                template = "marketplaces/Amazon_CA_Other_Flashlights_Data.txt"
            if market == 'mx':
                template = "marketplaces/amazon_mx_outdoors_template.txt"
            if market in ["eu", "uk", "de", "it", "es", "fr", "se", "tr"]:
                template = "marketplaces/amazon_uk_sports_flashlightlatern_20190328_data.txt"
            if market == 'jp':
                template = "marketplaces/amazon_uk_sports_flashlightlatern_20190328_data.txt"
            if market == 'au':
                template = "marketplaces/amazon_au_FlashlightLanterns_template.txt"
            if market == 'sg':
                template = "marketplaces/amazon_sg_flashlight_data.txt"

            if market == 'ae':
                template = "marketplaces/amazon_ae_other_flashlight_data.txt"
            if market == 'sa':
                template = "marketplaces/amazon_ae_other_flashlight_data.txt"



            barcode_set = self.barcode_set.all()
            for b in barcode_set:
               ean = b.EAN
               if market == 'ca':
                  b.is_used_by_amazon_ca = True
               else:
                  b.is_used_by_amazon_com = True
               b.save()
            barcode_set = None #this will void the above 7 lines to avoid amazon merge two SKUs based on the same EAN
            if not barcode_set:
               bar = barcode()
               bar.product = self
               if market == 'ca':
                  bar.is_used_by_amazon_ca = True
               else:
                  bar.is_used_by_amazon_com = True
               bar.save()
               ean = bar.EAN
            variables.update({'ean':ean})

        if 'science' in self.get_department.lower():
            template = "marketplaces/amazon_labsupplies_template.txt"
            if market == 'ca':
                template = "marketplaces/Flat.File.LabSupplies.ca.entries.txt"
            variables.update({'item_type_keyword':'science-lab-consumables'})
            sku = self.meta_description
            sku = sku.rsplit(None,1)[1]
        brand = self.brand.name
        if brand.lower() == "nest":
             brand = "Eco-Sensa"
        #if brand.lower() == "nitecore":
        #    brand = "Andrew & Amanda"
        variables.update({'brand':brand})
        model = self.modelNumber
        model = model.replace(' ', '-')
        variables.update({'model':model})

        meta_description = self.meta_description

        meta_description = replace_str(meta_description, "bank", "Charger")
        meta_description = replace_str(meta_description, "cree", "C-ree")
        meta_description = replace_str(meta_description, "osram", "O-sram")
        if market == 'ca':
            meta_description = replace_str(meta_description, "eco-sensa", "")
            meta_description = replace_str(meta_description, "eco-", "")
            meta_description = replace_str(meta_description, "EcoSensa", "")

        for kword in AMAZON_RESTRICTED_KEYWORDS:
            meta_description = replace_str(meta_description, kword, " ")

        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
             sku += "jn"
             variables.update({'name':meta_description + " w/ Exclusive Jetbeam Keychain Light"})
             variables.update({'manufacturer': "Ecosphere"})
        else:
             variables.update({'name':meta_description})
             variables.update({'manufacturer': brand})
        if "nitecore" in brand.lower():
             variables.update({'manufacturer': "SYSMAX Innovations Co., Ltd"})

        # Below two lines will override the above condition for now until we figure out what to do with the Jetbeam store on Amazon
        variables.update({'name':meta_description})
        variables.update({'manufacturer': brand})
        if "nitecore" in brand.lower():
             variables.update({'manufacturer': "SYSMAX Innovations Co., Ltd"})


        variables.update({'sku':sku})
        if self.features:
             desc = self.features
             desc = "<b>" + self.meta_description + "</b><br><br>" + desc.replace('\n', '<br>').replace('\r', '')
        else:
             description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
             #description = remove_html_markup(description)
             soup = BeautifulSoup(description)
             desc = ''
             for str in soup.stripped_strings:
                 desc += str + '<br>'

        desc = replace_str(desc, "bank", "Charger")
        desc = replace_str(desc, "cree", "C-ree")
        desc = replace_str(desc, "osram", "O-sram")

        for kword in AMAZON_RESTRICTED_KEYWORDS:
            desc = replace_str(desc, kword, " ")

        from ecomstore.utils.strops import smart_truncate
        desc = smart_truncate(desc, 1960) + " ..."
        variables.update({'description':desc})
        price = self.price
        import decimal
        if market == 'ca':
             price = decimal.Decimal(price) * decimal.Decimal(1.4)
        if market == 'mx':
             price = decimal.Decimal(price) * decimal.Decimal(20.0)
        if market == 'jp':
             price = decimal.Decimal(price) * decimal.Decimal(130.0)
        if market == 'au':
             price = decimal.Decimal(price) * decimal.Decimal(1.6)
        if market == 'ae':
             price = decimal.Decimal(price + 15) * decimal.Decimal(3.67)
        if market == 'sa':
             price = decimal.Decimal(price + 35) * decimal.Decimal(3.75)
        if market == 'tr':
             price = decimal.Decimal(price + 35) * decimal.Decimal(8.00)
        if market == 'sg':
             price = decimal.Decimal(price) * decimal.Decimal(1.50)
        if market in ["eu", "uk", "de", "it", "es", "fr", "se", "tr"]:
             price = decimal.Decimal(price) * decimal.Decimal(1.25)


        #the above 15 accommodates the max fedex shipping cost we are able to set


        price = round(price,2)
        variables.update({'price':price})
        list_price = decimal.Decimal(price) * decimal.Decimal(1.3)
        variables.update({'list_price':list_price})

        last_bullet = "ships out within one business day"
        if market in ["eu", "uk", "de", "it", "es", "fr", "se", "tr", "jp", "au", "ae", "sa"]:
            last_bullet = "ships out within one business day from United States"

        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
             last_bullet = "Include a free Jetbeam 25 Lumen Keychain Light, exclusively distributed by Jetbeam Store only"
        bullet_set = False
        if self.description:
             description = self.description
             description = replace_str(description, "bank", "Charger")
             description = replace_str(description, "cree", "C-ree")
             description = replace_str(description, "osram", "O-sram")


             for kword in AMAZON_RESTRICTED_KEYWORDS:
                description = replace_str(description, kword, " ")
             bullets = description.splitlines()
             if len(bullets) > 0:
                 bullet_set = True
             if len(bullets) == 1:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':last_bullet})
             if len(bullets) == 2:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':last_bullet})
             if len(bullets) == 3:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':last_bullet})
             if len(bullets) == 4:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':bullets[3]})
             if len(bullets) == 5:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':bullets[3]})
                 variables.update({'bullet_point_5':bullets[4]})
             if len(bullets) > 5:
                 variables.update({'bullet_point_1':bullets[0]})
                 variables.update({'bullet_point_2':bullets[1]})
                 variables.update({'bullet_point_3':bullets[2]})
                 variables.update({'bullet_point_4':bullets[3]})
                 variables.update({'bullet_point_5':bullets[4]})
                 variables.update({'bullet_point_5':bullets[5]})




                 variables.update({'bullet_point_5':last_bullet})
        if not bullet_set:
             variables.update({'bullet_point_1':meta_description})
             variables.update({'bullet_point_2':last_bullet})
        variables.update({'key_1':self.all_categories})
        key_2 = self.meta_description
        key_2 = key_2[:100]
        variables.update({'key_2':key_2})
        a_images = self.additionalimages_set.all()
        if len(a_images) > 0:
           image_2 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[0].a_image.url)
           variables.update({'image_2':image_2})
        if len(a_images) > 1:
           image_3 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[1].a_image.url)
           variables.update({'image_3':image_3})
        if len(a_images) > 2:
           image_4 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[2].a_image.url)
           variables.update({'image_4':image_4})
        if len(a_images) > 3:
           image_5 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[3].a_image.url)
           variables.update({'image_5':image_5})
        if len(a_images) > 4:
           image_6 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[4].a_image.url)
           variables.update({'image_6':image_6})
        if len(a_images) > 5:
           image_7 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[5].a_image.url)
           variables.update({'image_7':image_7})
        if len(a_images) > 6:
           image_8 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[6].a_image.url)
           variables.update({'image_8':image_8})
        if len(a_images) > 7:
           image_9 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[7].a_image.url)
           variables.update({'image_9':image_9})
        amazon_image = None
        for a in a_images:
            try:
                if a.image_caption.lower().find('amazon') != -1:
                    amazon_image = a
            except Exception:
                continue
        if amazon_image:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(amazon_image.a_image.url)
        else:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
            try:
                image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image_jetbeam.url)
            except:
                pass
        variables.update({'image_1':image_1})

        entry = render_to_string(template, variables)
        entry = entry.replace("&lt;", "<")
        entry = entry.replace("&gt;", ">")
        entry = entry.encode('ascii',errors='ignore')
        return entry


    def add2skuvaultfeed(self):
        from django.template.loader import render_to_string
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode
        variables = {}
        sku = self.sku
        if not sku.startswith('aa'):
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            sku_length = 7
            sku = 'AA-'
            for y in range(sku_length):
               sku += characters[random.randint(0, sku_length)]
            self.sku = sku
            self.save()

        template = "marketplaces/skuvault_dataentry.csv"

        ean = sku
        variables.update({'ean':ean})

        brand = self.brand.name
        if brand.lower() == "nest":
             brand = "Eco-Sensa"
        #if brand.lower() == "nitecore":
        #    brand = "Andrew & Amanda"
        variables.update({'brand':brand})
        model = self.modelNumber
        model = model.replace(' ', '-')
        variables.update({'model':model})

        variables.update({'manufacturer': brand})


        # Below two lines will override the above condition for now until we figure out what to do with the Jetbeam store on Amazon
        title = self.meta_description.replace(",","").replace("("," ").replace(")"," ")

        variables.update({'name':title})


        variables.update({'sku':sku})

        variables.update({'description':title})


        price = self.price
        variables.update({'price':price})

        amazon_image = None
        a_images = self.additionalimages_set.all()
        for a in a_images:
            try:
                if a.image_caption.lower().find('amazon') != -1:
                    amazon_image = a
            except Exception:
                continue
        if amazon_image:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(amazon_image.a_image.url)
        else:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)

        variables.update({'image_1':image_1})

        variables.update({'classification':self.first_category})

        entry = render_to_string(template, variables)
        entry = entry.replace("&lt;", "<")
        entry = entry.replace("&gt;", ">")
        entry = entry.encode('ascii',errors='ignore')
        return entry


    def add2neweggfeed(self, market):
        from django.template.loader import render_to_string
        from django.contrib.sites.models import Site
        from ecomstore.utils.strip_html import remove_html_markup
        from bs4 import BeautifulSoup
        import random
        from ecomstore.misc.models import barcode
        variables = {}
        sku = self.sku
        if not sku.startswith('aa'):
            characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            sku_length = 7
            sku = 'AA-'
            for y in range(sku_length):
               sku += characters[random.randint(0, sku_length)]
            self.sku = sku
            self.save()

        if 'flashlight' in self.get_department.lower():
            template = "marketplaces/newegg/HomeImprovement_BatchItemCreation_Flashlights_tab_entry.txt"
            if market == 'ca':
                template = "marketplaces/amazon_ca_Sports.template.txt"
            barcode_set = self.barcode_set.all()
            for b in barcode_set:
               ean = b.EAN
               if market == 'ca':
                  b.is_used_by_amazon_ca = True
               else:
                  b.is_used_by_amazon_com = True
               b.save()
            barcode_set = None #this will void the above 7 lines to avoid amazon merge two SKUs based on the same EAN
            if not barcode_set:
               bar = barcode()
               bar.product = self
               if market == 'ca':
                  bar.is_used_by_amazon_ca = True
               else:
                  bar.is_used_by_amazon_com = True
               bar.save()
               ean = bar.EAN
            variables.update({'ean':ean})

        if 'science' in self.get_department.lower():
            template = "marketplaces/amazon_labsupplies_template.txt"
            if market == 'ca':
                template = "marketplaces/Flat.File.LabSupplies.ca.entries.txt"
            variables.update({'item_type_keyword':'science-lab-consumables'})
            sku = self.meta_description
            sku = sku.rsplit(None,1)[1]
        brand = self.brand.name
        if brand.lower() == "nest":
             brand = "Eco-Sensa"
        variables.update({'brand':brand})
        model = self.modelNumber
        model = model.replace(' ', '-')
        model = model[-20:]
        variables.update({'model':model})
        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
             sku += "jn"
             variables.update({'name':self.meta_description})
             variables.update({'manufacturer': brand})
        else:
             variables.update({'name':self.meta_description})
             variables.update({'manufacturer': brand})
        variables.update({'sku':sku})
        if self.features:
             desc = self.features
             desc = "<b>" + self.meta_description + "</b><br><br>" + desc.replace('\n', '<br>').replace('\r', '')
        else:
             description = self.full_description.replace('\t','').replace('\n','').replace('\r','')
             #description = remove_html_markup(description)
             soup = BeautifulSoup(description)
             desc = ''
             for str in soup.stripped_strings:
                 desc += str + '<br>'
             from ecomstore.utils.strops import smart_truncate
             desc = smart_truncate(desc, 1980) + " ..."
        variables.update({'description':desc})
        price = self.price
        import decimal
        if market == 'ca':
             price = decimal.Decimal(price) * decimal.Decimal(1.4)
        price = round(price,2)
        variables.update({'price':price})
        last_bullet = "ships out within one business day by Andrew-Amanda"
        bullet_set = False
        newegg_bullets = ''
        prev_len = 0
        if self.description:
             bullets = self.description.splitlines()
             if len(bullets) > 0:
                 bullet_set = True
                 for b in bullets:
                     newegg_bullets = newegg_bullets + b + "^^"
                 newegg_bullets = newegg_bullets[:-2]
                 newegg_bullets = newegg_bullets[:200]
        if not bullet_set:
             variables.update({'bullet_point_1':self.meta_description})
             variables.update({'bullet_point_2':last_bullet})
             newegg_bullets = self.meta_description
        newegg_bullets = newegg_bullets[:190]
        variables.update({"newegg_bullets":newegg_bullets})
        variables.update({'key_1':self.all_categories})
        key_2 = self.meta_description
        key_2 = key_2[:100]
        variables.update({'key_2':key_2})
        a_images = self.additionalimages_set.all()
        if len(a_images) > 0:
           image_2 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[0].a_image.url)
           variables.update({'image_2':image_2})
        if len(a_images) > 1:
           image_3 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[1].a_image.url)
           variables.update({'image_3':image_3})
        if len(a_images) > 2:
           image_4 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[2].a_image.url)
           variables.update({'image_4':image_4})
        if len(a_images) > 3:
           image_5 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[3].a_image.url)
           variables.update({'image_5':image_5})
        if len(a_images) > 4:
           image_6 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[4].a_image.url)
           variables.update({'image_6':image_6})
        if len(a_images) > 5:
           image_7 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[5].a_image.url)
           variables.update({'image_7':image_7})
        if len(a_images) > 6:
           image_8 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[6].a_image.url)
           variables.update({'image_8':image_8})
        if len(a_images) > 7:
           image_9 = "http://" + Site.objects.get_current().domain + super_image_url(a_images[7].a_image.url)
           variables.update({'image_9':image_9})
        amazon_image = None
        for a in a_images:
            try:
                if a.image_caption.lower().find('amazon') != -1:
                    amazon_image = a
            except Exception:
                continue
        if amazon_image:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(amazon_image.a_image.url)
        else:
            image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image.url)
        if brand.lower() == "jetbeam" or brand.lower() == "niteye":
            try:
                image_1 = "http://" + Site.objects.get_current().domain + super_image_url(self.image_jetbeam.url)
            except:
                pass
        variables.update({'image_1':image_1})

        entry = render_to_string(template, variables)
        entry = entry.replace("&lt;", "<")
        entry = entry.replace("&gt;", ">")
        entry = entry.encode('ascii',errors='ignore')
        return entry

    """
    @property
    def max_lumens(self):
        max_lumens = 0
        attribute_cache_key = 'product_top_attribute_list_' + self.slug
        top_attributes = cache.get(attribute_cache_key)
        if not top_attributes:
            top_attributes = self.topattributes_set.all()
            cache.set(attribute_cache_key, top_attributes, CACHE_TIMEOUT)
        for attr in top_attributes:
            if attr.name == 'Max Output':
               max_lumens = attr.value
        return max_lumens

    @property
    def min_lumens(self):
        min_lumens = 0
        attribute_cache_key = 'product_top_attribute_list_' + self.slug
        top_attributes = cache.get(attribute_cache_key)
        if not top_attributes:
            top_attributes = self.topattributes_set.all()
            cache.set(attribute_cache_key, top_attributes, CACHE_TIMEOUT)
        for attr in top_attributes:
            if attr.name == 'Min Output':
               min_lumens = attr.value
        return min_lumens
    """


try:
    tagging.register(Product)
except:
    pass

class OptionalChoices(models.Model):
    title = models.CharField(max_length=200,
                           help_text='e.g, body color; then add the individual choice details')
    #choice_1 = models.CharField(max_length=200,
    #                       help_text='If for an additional charge, - Add $amount as the postfix, e.g, Brown Color - Add $12')
    #choice_2 = models.CharField(max_length=200, null=True, blank=True)
    #choice_3 = models.CharField(max_length=200, null=True, blank=True)
    #choice_4 = models.CharField(max_length=200, null=True, blank=True)
    #choice_5 = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,)

    @property
    def title_normalize(self):
        return self.title.replace(' ', '_')

    @property
    def product_name(self):
        return self.product.name


class IndividualChoice(models.Model):
    description = models.CharField(max_length=200, help_text='Dark Brown, Smooth Reflector, etc')
    additional_price = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    quantity = models.IntegerField()
    optionalchoices = models.ForeignKey(OptionalChoices, on_delete=models.CASCADE)

class TopAttributes(models.Model):
    #name = models.PositiveSmallIntegerField(default=1, null=True, choices=TOP_ATTRIBUTE_CHOICES)
    name = models.CharField(max_length=20, default='LED Type', null=True, choices=TOP_ATTRIBUTE_CHOICES)
    value = models.CharField(max_length=30)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class AdditionalImages(models.Model):
    #a_image = StdImageField(upload_to='images/products/main', size=(300,500))
    #a_image_zoom = StdImageField(upload_to='images/products/main', size=(1024,1024))
    #a_thumbnail = StdImageField(upload_to='images/products/thumbnails', size=(50,50))
    a_image = StdImageField(upload_to='images/products/main',
                    variations={'super': (2024,2048), 'large': (439, 438), 'thumbnail': (139, 140, True)})

    image_caption = models.CharField(max_length=200, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    #def save(self, *args, **kwargs):
        #self.a_image = Webp2Jpeg(self.a_image)

        # Call the original save method
        #super().save(*args, **kwargs)

class accessory_product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    accessories = models.ManyToManyField(Product, related_name='accessories')
    products = models.ManyToManyField(Product, related_name='products')

    class Meta:
        verbose_name = 'Accessory Group'
        verbose_name_plural = 'Accessory Groups'

    def __str__(self):
        return self.name

    def all_accessories(self):
        return ', '.join([c.name for c in self.accessories.all()])
    all_accessories.short_description = "accessories"

    def all_products(self):
        return ', '.join([c.name for c in self.products.all()])
    all_products.short_description = "products"





class ActiveProductReviewManager(models.Manager):
    """ Manager class to return only those product reviews where each instance is approved """
    def all(self):
        return super(ActiveProductReviewManager, self).all().filter(is_approved=True)

class ProductReview(models.Model):
    """ model class containing product review data associated with a product instance """
    RATINGS = ((5,5),(4,4),(3,3),(2,2),(1,1),)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(default=5, choices=RATINGS)
    is_approved = models.BooleanField(default=True)
    content = models.TextField()

    objects = models.Manager()
    approved = ActiveProductReviewManager()

class ActiveProductQuestionManager(models.Manager):
    """ Manager class to return only those product reviews where each instance is approved """
    def all(self):
        return super(ActiveProductQuestionManager, self).all().filter(is_answered=True)

class ProductQuestion(models.Model):
    """ model class containing product question associated with a product instance """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    is_answered = models.BooleanField(default=True)
    question = models.TextField()

    answered = ActiveProductQuestionManager()

    class Meta:
        db_table = 'questions'


class FutureDealOfTheDayManager(models.Manager):
    """ Manager class to return only those product reviews where each instance is approved """
    def all(self):
        curr = datetime.now()
        return super(FutureDealOfTheDayManager, self).all().filter(end_date__gte=curr)

class ActiveDealOfTheDayManager(models.Manager):
    """ Manager class to return only those product reviews where each instance is approved """
    def all(self):
        curr = datetime.now()
        return super(ActiveDealOfTheDayManager, self).all().filter(end_date__gte=curr).exclude(start_date__gte=curr)

class DealOfTheDay(models.Model):
    """ model class containing Deals of the day """

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    deal_price = models.DecimalField(max_digits=9,decimal_places=2)

    sold_date = models.DateTimeField(blank=True, null=True)
    purchased_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)


    quantity = models.PositiveSmallIntegerField(default=5)

    objects = models.Manager()
    active = ActiveDealOfTheDayManager()
    future = FutureDealOfTheDayManager()

    def post2twitter(self):
        message = 'Deal Of The Day - ' + self.title + '-$' + str(self.deal_price) + '(orig.' + str(self.product.price) + ')'
        status = updateTwitter(message)
        return status



class ProductAssociation(models.Model):
    title = models.CharField(max_length=50)
    products = models.ManyToManyField(Product)

    class Meta:
        db_table = 'product_association'
        ordering = ['-title']
        verbose_name = 'Related Product Group'
        verbose_name_plural = 'Related Product Groups'

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
             "id": self.id,
             "user": self.user.username,
             "email": self.email,
             "name": self.name,
             "quantity": self.quantity,
             "reason": self.reason,
             "country": self.country,
             "state": self.state,
             "last_updated": str(self.last_updated)
        }


    def all_products(self):
        return ', '.join([c.name for c in self.products.all()])
    all_products.short_description = "products"



# attach signals to Product and Category model classes
# to update cache data on save and delete operations
post_save.connect(cache_update, sender=Department)
post_delete.connect(cache_evict, sender=Department)
post_save.connect(cache_update, sender=Product)
post_delete.connect(cache_evict, sender=Product)
post_save.connect(cache_update, sender=Category)
post_delete.connect(cache_evict, sender=Category)
post_save.connect(cache_update, sender=Brand)
post_delete.connect(cache_evict, sender=Brand)
post_save.connect(cache_update, sender=Series)
post_delete.connect(cache_evict, sender=Series)
post_save.connect(cache_update, sender=SubCategory)
post_delete.connect(cache_evict, sender=SubCategory)
