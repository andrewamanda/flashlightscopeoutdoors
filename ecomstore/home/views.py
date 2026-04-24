from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404

from ecomstore.catalog.models import Department, Product, Category, Brand, DealOfTheDay
from ecomstore.settings import PRODUCTS_PER_ROW, NUM_OF_NEW_ARRIVALS


from ecomstore.stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW, PRODUCTS_PER_PAGE, NUM_OF_NEW_ARRIVALS
import datetime

from ecomstore.settings import SITE_NAME
from ecomstore.cart import cart
from django.http import HttpResponseRedirect, HttpResponse
from ecomstore.misc.models import MessageOfTheDay, MediaImage
from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT







# Create your views here.
def home(request, template_name="home/store_main.html"):
    """ page displaying the Aimkon Outdoors Home """

    calendar_months = [ "jan", "feb", "mar", "apr", "may", "jun",
                    "jul", "aug", "sep", "oct", "nov", "dec" ]

    page_title = 'Your premium source for outdoor gears'
    name = request.user.username

    now = datetime.datetime.now( )
    month_name = calendar_months[ now.month-1 ]
    todays_file = month_name + "_" + ("%02d" % now.day)
    calendar_spec = "calendar_" + todays_file + ".jpg"

    #featured = Product.featured.all()[0:PRODUCTS_PER_PAGE]
    #coming_soon = Product.coming_soon.all()[0:NUM_OF_NEW_ARRIVALS]

    messageoftheday = MessageOfTheDay.active.all()

    #banner_cache_key = "banner_"
    #banners = cache.get(banner_cache_key)
    #if not banners:
    #      banners = MediaImage.active.all()
    #      cache.set(banner_cache_key, banners, CACHE_TIMEOUT)
    #for b in banners:
    #     print "b = {}, {}".format(b.url_link, b.description)
    banners = MediaImage.active.all()

    newarrivals_cache_key = "newarrivals_"
    new_arrivals = cache.get(newarrivals_cache_key)
    if not new_arrivals:
          new_arrivals = Product.new_arrivals.all()
          cache.set(newarrivals_cache_key, new_arrivals, CACHE_TIMEOUT)

    deals_cache_key = 'active_deals_'
    dealoftheday = cache.get(deals_cache_key)
    if not dealoftheday or len(dealoftheday) == 0:
        dealoftheday = []
        deals = DealOfTheDay.active.all()
        for d in deals:
            product = d.product
            #if not product.sale_price:
            #    product.old_price = product.price
            #product.price = d.deal_price
            #product.quantity = d.quantity
            dealoftheday.append(product)
            cache.set(deals_cache_key, dealoftheday, CACHE_TIMEOUT)
            meta_keywords = product.meta_keywords
            meta_description = product.meta_description

    clearance = Product.objects.filter(clearance=True).filter(is_active=True)
    openbox = Product.objects.filter(is_openbox=True).filter(is_active=True)

    brand_cache_key = 'active_brand_link_list'
    active_brands = cache.get(brand_cache_key)
    if not active_brands:
        active_brands = Brand.active.all().order_by('ranking')
        cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)

    department_cache_key = 'active_department_link_list'
    active_departments = cache.get(department_cache_key)
    if not active_departments:
        active_departments = Department.active.all().order_by('ranking')
        cache.set(department_cache_key, active_departments, CACHE_TIMEOUT)

    if request.method == 'POST':
        url = request.path
        #create the bound form
        postdata = request.POST.copy()
        #add to cart and redirect to cart page
        cart.add_to_cart(request)
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
           request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/home.html'


         start = datetime.datetime.now()


         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         end = datetime.datetime.now()
         elapsed = end - start
         print(elapsed)
         # or
         print(elapsed.seconds,":",elapsed.microseconds)

    return render(request, template_name, locals())


# Create your views here.
def index(request, template_name="home/index.html"):
    """ page displaying the Aimkon Outdoors Home """

    calendar_months = [ "jan", "feb", "mar", "apr", "may", "jun",
                    "jul", "aug", "sep", "oct", "nov", "dec" ]

    page_title = 'Your premium source for outdoor gears'
    name = request.user.username

    now = datetime.datetime.now( )
    month_name = calendar_months[ now.month-1 ]
    todays_file = month_name + "_" + ("%02d" % now.day)
    calendar_spec = "calendar_" + todays_file + ".jpg"

    featured = Product.featured.all()[0:NUM_OF_NEW_ARRIVALS]
    new_arrivals = Product.new_arrivals.all()[0:NUM_OF_NEW_ARRIVALS]
    coming_soon = Product.coming_soon.all()[0:NUM_OF_NEW_ARRIVALS]

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

    messageoftheday = MessageOfTheDay.active.all()



    if request.method == 'POST':
        url = request.path
        #create the bound form
        postdata = request.POST.copy()
        #add to cart and redirect to cart page
        cart.add_to_cart(request)
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
           request.session.delete_test_cookie()
        return HttpResponseRedirect(url)



    return render(request, template_name, locals())
