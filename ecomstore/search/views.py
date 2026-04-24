from django.shortcuts import render
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage

from ecomstore.search import search
from ecomstore import settings

#from django.utils import simplejson
import json as simplejson
from django.http import HttpResponse
from django.core import serializers
from ecomstore.catalog.models import Product
from ecomstore.stats import stats
from ecomstore.catalog.models import Product, Category, Brand
from ecomstore.settings import PRODUCTS_PER_ROW, CACHE_TIMEOUT
from django.core.cache import cache

def results(request, template_name="search/results.html"):
    """ template for displaying settings.PRODUCTS_PER_PAGE paginated product results """
    # get current search phrase
    q = request.GET.get('q', '')
    # get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    matching = search.products(q).get('products', [])
    # generate the pagintor object
    paginator = Paginator(matching,
                          settings.PRODUCTS_PER_PAGE)

    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect("/")

    #search.store(request, q)

    page_title = 'Search Results for: ' + q

    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/searchresults.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)



    return render(request, template_name, locals())
