from django.db import models
from ecomstore.catalog.models import Product

from django.shortcuts import render
from django.template.loader import render_to_string
from stdimage.models import StdImageField

# Create your models here.

class RichTextField(models.TextField):
    pass

class EBayListing(models.Model):
    name = models.CharField(max_length=20, unique=True,
                 help_text="for example, SRT7w2XNL189")
    front_image = StdImageField(upload_to='images/products/ebay', null=True, blank=True,
                          variations={'large': (500, 500), 'thumbnail': (160, 160, True)})
    comment_little_ebay = RichTextField(null=True, blank=True, verbose_name="Comment for flashlight_scope_outdoors eBay listing")
    comment_big_ebay = RichTextField(null=True, blank=True, verbose_name="Comment for andrew_amanda_outdoors eBay listing")

    products = models.ManyToManyField(Product, related_name="main_products")

    little_ebay_description = models.TextField(null=True, blank=True,
                     help_text='for Flashlight-Scope-Outdoors', verbose_name="flashlight_scope_outdoors eBay description")
    big_ebay_description = models.TextField(null=True, blank=True,
                     help_text='for Andrew-Amanda-Outdoors', verbose_name="andrew_amanda_outdoors eBay description")
    amazon_description = models.TextField(null=True, blank=True,
                     help_text='for Andrew-Amanda-Outdoors')

    posted = models.BooleanField(default = False)
    price = models.DecimalField(max_digits=9,decimal_places=2,null=True, blank=True)
    little_ebay_title = models.CharField(max_length=80,null=True, blank=True, verbose_name="flashlight_scope_outdoors eBay Title")
    big_ebay_title = models.CharField(max_length=80,null=True, blank=True, verbose_name="andrew_amanda_outdoors eBay Title")

    def all_included(self):
           packageincludes = ', '.join([p.name for p in self.products.all()])
           for bs in self.bonusaccessories_set.all():
               packageincludes += ', ' + str(bs.quantity) + 'x' + bs.name
           return packageincludes
    all_included.short_description = "included"


    def save(self):
        little_ebay_template = "ebay/flashlight_scope_outdoors.html"
        big_ebay_template = "ebay/andrew-amanda.com.html"

        if self.pk:

           packageincludes = ', '.join([p.name for p in self.products.all()]) + ' in the original factory box with all accessories'
           for bs in self.bonusaccessories_set.all():
               packageincludes += ', ' + str(bs.quantity) + 'x' + bs.name

           lIncludes = '<ul>'

           more_images = []
           for p in self.products.all():
               lIncludes += '<li>' + p.name + ' in the unopened factory box</li>'
               p1 = p
               images = p1.additionalimages_set.all()
               more_images.extend(images[:4])

           title = ''
           for bs in self.bonusaccessories_set.all():
               title = 'Combo Offer: '
               lIncludes += '<li>' + str(bs.quantity) + 'x' + bs.name + '</li>'
           lIncludes += '</ul>'

           title += ', '.join([p.meta_description for p in self.products.all()])
           title += self.all_included()

           # description = '<br><br>'.join([p.full_description for p in self.products.all()])
           description = '<br>'
           for p in self.products.all():
               description += '<br><span style=\"margin-left:auto;margin-right:auto;font-size:30px;font-weight:bold\">' + p.name + '</span><br>'
               description += unicode(p.full_description)

           context_little_ebay = {'title': title,'comments':self.comment_little_ebay,'description':description,'packageincludes':lIncludes, 'p':p1, 'more_images':more_images}
           little_ebay_content = render_to_string(little_ebay_template, context_little_ebay)
           self.little_ebay_description = little_ebay_content

           title = ', '.join([p.meta_description for p in self.products.all()])
           context_big_ebay = {'title': title,'comments':self.comment_big_ebay,'description':description,'packageincludes':lIncludes, 'p':p1, 'more_images':more_images}
           big_ebay_content = render_to_string(big_ebay_template, context_big_ebay)
           self.big_ebay_description = big_ebay_content


        super(EBayListing, self).save()



class BonusAccessories(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    ebaylisting = models.ForeignKey(EBayListing, on_delete=models.CASCADE)
