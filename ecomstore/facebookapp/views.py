from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404

from ecomstore.catalog.models import Product, DealOfTheDay
from ecomstore.settings import PRODUCTS_PER_ROW, NUM_OF_NEW_ARRIVALS


from ecomstore.stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW, PRODUCTS_PER_PAGE, NUM_OF_NEW_ARRIVALS
import datetime

from ecomstore.settings import SITE_NAME
from ecomstore.cart import cart
from django.http import HttpResponseRedirect, HttpResponse
from ecomstore.misc.models import MessageOfTheDay
from ecomstore.catalog.models import Category, Brand


from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT
from django.shortcuts import render



from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def facebookapp(request, template_name="facebookapp/home.html"):

    featured = Product.featured.all()[0:PRODUCTS_PER_PAGE]
    new_arrivals = Product.new_arrivals.all()[0:NUM_OF_NEW_ARRIVALS]
    coming_soon = Product.coming_soon.all()[0:NUM_OF_NEW_ARRIVALS]

    messageoftheday = MessageOfTheDay.active.all()

    deals = DealOfTheDay.active.all()
    dealoftheday = []
    for d in deals:
        product = d.product
        if not product.sale_price:
            product.old_price = product.price
        product.price = d.deal_price
        #product.quantity = d.quantity
        dealoftheday.append(product)

        meta_keywords = product.meta_keywords
        meta_description = product.meta_description

    list_cache_key = 'active_category_link_list'
    active_categories = cache.get(list_cache_key)
    if not active_categories:
        active_categories = Category.active.all().order_by('ranking')
        cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

    list_cache_key = 'active_brand_link_list'
    active_brands = cache.get(list_cache_key)
    if not active_brands:
        active_brands = Brand.active.all().order_by('ranking')
        cache.set(list_cache_key, active_brands, CACHE_TIMEOUT)

    return render(request, template_name, locals())

@csrf_exempt
def MakeOffer(request, template_name="facebookapp/MakeOffer.html"):
    return render(request, template_name, locals())

@csrf_exempt
def DealOfDay(request, template_name="facebookapp/dealoftheday.html"):
    calendar_months = [ "jan", "feb", "mar", "apr", "may", "jun",
                    "jul", "aug", "sep", "oct", "nov", "dec" ]
    now = datetime.datetime.now( )
    month_name = calendar_months[ now.month-1 ]
    todays_file = month_name + "_" + ("%02d" % now.day)
    calendar_spec = "calendar_" + todays_file + ".jpg"

    deals = DealOfTheDay.active.all()
    products = []
    for d in deals:
        product = d.product
        if not product.sale_price:
            product.old_price = product.price
        product.price = d.deal_price
        #product.quantity = d.quantity
        products.append(product)

        meta_keywords = product.meta_keywords
        meta_description = product.meta_description

    return render(request, template_name, locals())

