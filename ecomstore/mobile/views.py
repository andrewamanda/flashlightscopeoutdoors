from django.template import RequestContext

from ecomstore.catalog.models import Product
from ecomstore.cart import cart
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect, HttpResponse
#from django.utils import simplejson
import json as simplejson
import json

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME
from ecomstore.newsletter.models import EmailSubscription
from ecomstore.django_mobile import set_flavour, get_flavour

def getProductAutoComplete(request):
    all_products_cache_key = 'all_products_autocomplete_'
    rJson = cache.get(all_products_cache_key)

    if rJson:
         print ("get allproducts from cache")

    if not rJson :
        products = Product.objects.filter(is_active=True).values('id','name').order_by('created_at').reverse()
        for p in products:
            product = Product.objects.get(id=p["id"])
            p["sale_price"] = str(product.sale_price)
        #import sys
        #import cPickle
        #p_string = cPickle.dumps(products)
        #print "size of products", sys.getsizeof(p_string)
        rJson = simplejson.dumps(list(products))
        cache.set(all_products_cache_key, rJson, CACHE_TIMEOUT)

    return HttpResponse(rJson,
                content_type='application/javascript; charset=utf-8')


def add2Cart(request):
    cart.add_to_cart(request)
    prop = {}
    #prop[request.POST.get('product_slug')] = int(request.POST.get('quantity'))

    slug = request.POST.get('product_slug')
    qty_str = request.POST.get('quantity')

    try:
       qty = int(qty_str)
    except (TypeError, ValueError):
       # TypeError = None passed in, ValueError = bad string like "2dfs"
       #raise ValueError(f"Invalid quantity value: {qty_str!r}")
       qty = 0

    prop[slug] = qty



    data ={}
    data['itemAdded'] = prop
    data['cartSize'] = cart.cart_distinct_item_count(request)
    ret = simplejson.dumps(data)
    return HttpResponse(ret,
                content_type='application/javascript; charset=utf-8')


def getCartCount(request):
    data = {}
    data['cartSize'] = cart.cart_distinct_item_count(request)
    ret = simplejson.dumps(data)
    return HttpResponse(ret,
                content_type='application/javascript; charset=utf-8')


def email_signup(request):
    """ page displaying the Aimkon email signup """
    if request.method == 'POST':

        email_subscription = EmailSubscription();
        email_subscription.email = request.POST.get('email', '')
        #print email_subscription.email
        email_subscription.save()

    response = simplejson.dumps({'success':'True'})
    return HttpResponse(response,
             content_type='application/javascript; charset=utf-8')

from ecomstore.misc.models import MessageOfTheDay
from ecomstore.catalog.models import Product,DealOfTheDay
from django.shortcuts import render
def messageoftheday(request):
    """ page displaying the Aimkon email signup """

    page_title = "Message Of The Day"
    new_arrivals = Product.new_arrivals.all()

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

    from ecomstore.catalog.models import Brand, Category
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


    messageoftheday = MessageOfTheDay.active.all()

    template_name = "mobile/home/messageoftheday.html"

    return render(request, template_name, locals())


    response = simplejson.dumps({'success':'True'})
    return HttpResponse(response,
             content_type='application/javascript; charset=utf-8')

#def switch_flavour(request):
#    current_flavour = get_flavour(request)
#    print "******",request.flavour
#    print "+++++++",current_flavour
#    set_flavour("full", permanent=True)
#    current_flavour = get_flavour(request)
#    print "******",request.flavour
#    print "+++++++",current_flavour
#    request.flavour = "full"
#    from django.core import urlresolvers
#    url = urlresolvers.reverse('home')
#    print url
#    return HttpResponseRedirect(url)
