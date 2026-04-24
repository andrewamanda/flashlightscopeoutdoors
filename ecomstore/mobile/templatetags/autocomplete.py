from django import template
from django.contrib.flatpages.models import FlatPage
from ecomstore.catalog.models import Product

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT

from django.shortcuts import get_object_or_404
import datetime

register = template.Library()

@register.inclusion_tag("mobile/home/searchpanel.html")
def autocomplete_searchlist():
   all_products_key = 'active_all_products_4autocomplete_'
   products = cache.get(all_products_key)
   if not products:
        start = datetime.datetime.now()

        products = Product.objects.filter(is_active=True).values('id','name','price').order_by('created_at').reverse()

        #for p in products:
        #    product = Product.objects.get(id=p["id"])
        #    p["sale_price"] = str(product.sale_price)
        cache.set(all_products_key, products, CACHE_TIMEOUT)
        end = datetime.datetime.now()
        elapsed = end - start
        #print "Generate AutoComplete Time elapsed {} seconds {} microseconds ".format(elapsed.seconds, elapsed.microseconds)

   return {'products': products}

@register.inclusion_tag("mobile/nameyourprice/searchpanel.html")
def autocomplete_offerlist():
   return {'products': getAllProducts()}

def getAllProducts():
   all_products_key = 'active_all_products_4autocomplete_'
   products = cache.get(all_products_key)
   if not products:
        start = datetime.datetime.now()

        products = Product.objects.filter(is_active=True).values('id','name','price').order_by('created_at').reverse()
        #for p in products:
        #    product = Product.objects.get(id=p["id"])
        #    p["sale_price"] = str(product.sale_price)
        cache.set(all_products_key, products, CACHE_TIMEOUT)

        end = datetime.datetime.now()
        elapsed = end - start
        #print "Get All Products Time elapsed {} seconds {} microseconds ".format(elapsed.seconds, elapsed.microseconds)

   return products
