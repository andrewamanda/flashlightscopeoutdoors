from django import template
from django.contrib.flatpages.models import FlatPage
from ecomstore.utils.strops import *
from ecomstore.catalog.models import Department, Category, Brand, Product, SubCategory, Series, PriceRange, BrightnessRange, DealOfTheDay
from ecomstore.checkout.models import Promotion, ProductOnlyPromotion
from ecomstore.cart import cart
from ecomstore.cart.models import CartItem, CartItemOption
from ecomstore.misc.models import Testimonial, BannerControl, TodaysNews
from django.urls import reverse
from datetime import datetime
from django.contrib.sites.models import Site
from datetime import datetime
from ecomstore.heartwoodbeyond.models import Reclaimed_Blog



from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, NUM_OF_NEW_ARRIVALS, DISTRIBUTOR_BRAND_SLUG, SITE_SEO_H1_TAG, SITE_SEO_TITLE, SITE_SEO_OG_TITLE, SITE_SEO_OG_DESCRIPTION, SITE_SEO_META_KEYWORDS, SITE_SEO_META_DESCRIPTION, CACHE_PREFIX

from django.shortcuts import get_object_or_404

def safe_cache_set(key, value, timeout=CACHE_TIMEOUT):
    """
    Safely set cache values.

    Memcached pickles values before storing them. Some Django model/queryset objects
    containing StdImageFieldFile can fail during pickling with errors like:
    "'StdImageFieldFile' object has no attribute 'super'" or "'large'".

    This helper prevents template tags from causing 500 errors because of safe_cache_set().
    """
    try:
        cache.set(key, value, timeout)
    except Exception as e:
        print(
            f"\n[CACHE SKIPPED - catalog_tags]\n"
            f"Key: {key}\n"
            f"Value Type: {type(value).__name__ if value is not None else 'None'}\n"
            f"Value Repr: {repr(value)[:200] if value is not None else 'None'}\n"
            f"Error: {e}\n"
        )


def util_brands_in_department(d):
    list_cache_key = CACHE_PREFIX + 'active_brands_link_list_4_' + d.slug
    brands = cache.get(list_cache_key)
    if not brands:
        brands = Brand.active.filter(department__slug = d.slug) | Brand.active.filter(department_2__slug = d.slug) | Brand.active.filter(department_3__slug = d.slug) | Brand.active.filter(department_4__slug = d.slug)
        safe_cache_set(list_cache_key, brands, CACHE_TIMEOUT)
    return brands


register = template.Library()

@register.inclusion_tag("tags/cart_box.html")
def cart_box(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count}

@register.simple_tag
def cart_count(request):
    cart_item_count = cart.cart_distinct_item_count(request)
    return cart_item_count

@register.inclusion_tag("tags/nav_category_list.html")
def nav_category_list(request_path, department):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/category/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep

    list_cache_key = CACHE_PREFIX + 'active_category_link_list_' + department.slug
    active_categories = cache.get(list_cache_key)
    if not active_categories:
        #active_categories = Category.active.all().order_by('ranking')
        active_categories = department.category_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
    return {
        'active_categories': active_categories,
        'request_path': request_path
    }

@register.inclusion_tag("tags/g_nav_category_list.html")
def g_nav_category_list(request_path, department):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/category/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep

    list_cache_key = CACHE_PREFIX + 'active_category_link_list_' + department.slug
    active_categories = cache.get(list_cache_key)
    if not active_categories:
        #active_categories = Category.active.all().order_by('ranking')
        active_categories = department.category_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
    return {
        'active_categories': active_categories,
        'request_path': request_path
    }

@register.simple_tag
def brands_in_the_department(d):
    return util_brands_in_department(d)

@register.simple_tag
def active_departments():
    list_cache_key = CACHE_PREFIX + 'active_departments_link_list'
    departments = cache.get(list_cache_key)
    if not departments:
        departments = Department.active.all().order_by('ranking')
        safe_cache_set(list_cache_key, departments, CACHE_TIMEOUT)
    return departments

@register.simple_tag
def active_categories():
    list_cache_key = CACHE_PREFIX + 'active_categories_link_list'
    categories = cache.get(list_cache_key)

    if not categories:
        categories = Category.active.all().order_by('ranking')
        safe_cache_set(list_cache_key, categories, CACHE_TIMEOUT)
    return categories



@register.simple_tag
def active_categories_4d(department):
    list_cache_key = CACHE_PREFIX + 'active_category_link_list_' + department.slug
    active_categories_4d = cache.get(list_cache_key)
    if not active_categories_4d:
        active_categories_4d = department.category_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_categories_4d, CACHE_TIMEOUT)
    return active_categories_4d

@register.simple_tag
def active_subcategory_list(category):
    list_cache_key = CACHE_PREFIX + 'active_subcategories_link_list_' + category.slug
    active_subcategories = cache.get(list_cache_key)
    if not active_subcategories:
        active_subcategories = category.subcategory_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_subcategories, CACHE_TIMEOUT)
    return active_subcategories

@register.inclusion_tag("tags/category_list.html")
def category_list(request_path, department):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/category/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep

    list_cache_key = CACHE_PREFIX + 'active_category_link_list_' + department.slug
    active_categories = cache.get(list_cache_key)
    if not active_categories:
        #active_categories = Category.active.all().order_by('ranking')
        active_categories = department.category_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
    return {
        'active_categories': active_categories,
        'department': department,
        'request_path': request_path
    }

@register.inclusion_tag("tags/active_subcategories.html")
def subcategory_list(request_path, category):
    list_cache_key = CACHE_PREFIX + 'active_subcategories_link_list_' + category.slug
    active_subcategories = cache.get(list_cache_key)
    if not active_subcategories:
        active_subcategories = category.subcategory_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_subcategories, CACHE_TIMEOUT)
    return {
        'active_subcategories': active_subcategories,
        'request_path': request_path
    }

@register.inclusion_tag("tags/g_active_subcategories.html")
def g_subcategory_list(request_path, category):
    list_cache_key = CACHE_PREFIX + 'active_subcategories_link_list_' + category.slug
    active_subcategories = cache.get(list_cache_key)
    if not active_subcategories:
        active_subcategories = category.subcategory_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_subcategories, CACHE_TIMEOUT)
    return {
        'active_subcategories': active_subcategories,
        'request_path': request_path
    }

@register.inclusion_tag("tags/g_searchresult.html")
def g_searchresult(c):
    return {
        'products': c,
    }

@register.inclusion_tag("2023/catalog/category_mainpanel.html")
def g_searchresult_2023(c):
    return {
        'products': c,
    }


@register.inclusion_tag("tags/footer.html")
def footer_links():
    flatpage_list = FlatPage.objects.all()
    return {'flatpage_list': flatpage_list }

@register.inclusion_tag("tags/product_list.html")
def product_list(products, header_text):
    return { 'products': products,
            'header_text': header_text }

@register.inclusion_tag("tags/product_list_3col.html")
def product_list_3col(products, header_text):
    return { 'products': products,
            'header_text': header_text }

@register.inclusion_tag("tags/product_list_special.html")
def product_list_special(products, header_text):
    return { 'products': products,
            'header_text': header_text }



@register.inclusion_tag("tags/nav_brand_list.html")
def nav_brand_list(request_path, department):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    active_brands = util_brands_in_department(department)
    #list_cache_key = CACHE_PREFIX + 'active_brand_link_list_' + department.slug
    #active_brands = cache.get(list_cache_key)
    #if not active_brands:
    #    active_brands = department.brand_set.filter(is_active=True).order_by('ranking')
    #    safe_cache_set(list_cache_key, active_brands, CACHE_TIMEOUT)
    return {
        'active_brands': active_brands,
        'request_path': request_path
    }

@register.inclusion_tag("tags/g_nav_brand_list.html")
def g_nav_brand_list(request_path, department):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    active_brands = util_brands_in_department(department)
    #list_cache_key = CACHE_PREFIX + 'active_brand_link_list_' + department.slug
    #active_brands = cache.get(list_cache_key)
    #if not active_brands:
    #    active_brands = department.brand_set.filter(is_active=True).order_by('ranking')
    #    safe_cache_set(list_cache_key, active_brands, CACHE_TIMEOUT)
    return {
        'active_brands': active_brands,
        'request_path': request_path
    }


@register.inclusion_tag("tags/brand_list.html")
def brand_list(request_path, department):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    active_brands = util_brands_in_department(department)
    #list_cache_key = CACHE_PREFIX + 'active_brand_link_list_' + department.slug
    #active_brands = cache.get(list_cache_key)
    #if not active_brands:
    #    active_brands = department.brand_set.filter(is_active=True).order_by('ranking')
    #    safe_cache_set(list_cache_key, active_brands, CACHE_TIMEOUT)
    return {
        'active_brands': active_brands,
        'department': department,
        'request_path': request_path
    }

@register.inclusion_tag("tags/active_series.html")
def series_list(request_path, brand):
    list_cache_key = CACHE_PREFIX + 'active_series_link_list_' + brand.slug
    active_series = cache.get(list_cache_key)
    if not active_series:
        active_series = brand.series_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_series, CACHE_TIMEOUT)
    return {
        'active_series': active_series,
        'request_path': request_path
    }

@register.inclusion_tag("tags/price_range.html")
def price_range(request_path):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    list_cache_key = CACHE_PREFIX + 'active_prices_range_list'
    active_prices = cache.get(list_cache_key)
    if not active_prices:
        active_prices = PriceRange.active.all().order_by('min_price')
        safe_cache_set(list_cache_key, active_prices, CACHE_TIMEOUT)
    return {
        'active_prices': active_prices,
        'request_path': request_path
    }

@register.inclusion_tag("tags/featuredproducts_nav.html")
def featured_products_in_brand(request):

    c = get_object_or_404(Brand.active, slug=DISTRIBUTOR_BRAND_SLUG)
    featured = c.product_set.filter(is_featured=True)
    return {
        'products': featured
    }

@register.inclusion_tag("for_dealers/active_series.html")
def series_in_brand(request_path):
    brand = get_object_or_404(Brand.active, slug=DISTRIBUTOR_BRAND_SLUG)

    list_cache_key = CACHE_PREFIX + 'active_series_link_list_' + brand.slug
    active_series = cache.get(list_cache_key)
    if not active_series:
        active_series = brand.series_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_series, CACHE_TIMEOUT)
    return {
        'active_series': active_series,
        'request_path': request_path
    }

@register.inclusion_tag("for_dealers/slide_list_all.html")
def slide_list_all_in_brand(request):
    brand = get_object_or_404(Brand.active, slug=DISTRIBUTOR_BRAND_SLUG)

    list_cache_key = CACHE_PREFIX + 'active_series_link_list_' + brand.slug
    active_series = cache.get(list_cache_key)
    if not active_series:
        active_series = brand.series_set.filter(is_active=True).order_by('ranking')
        safe_cache_set(list_cache_key, active_series, CACHE_TIMEOUT)

    products = brand.product_set.all()

    return {
        'active_series': active_series,
        'products': products
    }

@register.inclusion_tag("tags/brightness_range.html")
def max_output_list(request_path):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep

    list_cache_key = CACHE_PREFIX + 'max_output_list'
    max_output_list = cache.get(list_cache_key)
    if not max_output_list:
        max_output_list = BrightnessRange.active.all().order_by('min_lumens')
        safe_cache_set(list_cache_key, max_output_list, CACHE_TIMEOUT)
    return {
        'max_outputs': max_output_list,
        'request_path': request_path
    }



@register.inclusion_tag("tags/nav_price_list.html")
def nav_price_list(request_path):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    list_cache_key = CACHE_PREFIX + 'active_prices_range_list'
    active_prices = cache.get(list_cache_key)
    if not active_prices:
        active_prices = PriceRange.active.all().order_by('min_price')
        safe_cache_set(list_cache_key, active_prices, CACHE_TIMEOUT)
    return {
        'active_prices': active_prices,
        'request_path': request_path
    }

@register.inclusion_tag("tags/g_nav_price_list.html")
def g_nav_price_list(request_path):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    list_cache_key = CACHE_PREFIX + 'active_prices_range_list'
    active_prices = cache.get(list_cache_key)
    if not active_prices:
        active_prices = PriceRange.active.all().order_by('min_price')
        safe_cache_set(list_cache_key, active_prices, CACHE_TIMEOUT)
    return {
        'active_prices': active_prices,
        'request_path': request_path
    }

@register.inclusion_tag("tags/nav_brightness_list.html")
def nav_brightness_list(request_path):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    list_cache_key = CACHE_PREFIX + 'max_output_list'
    active_brightnesses = cache.get(list_cache_key)
    if not active_brightnesses:
        active_brightnesses = BrightnessRange.active.all().order_by('min_lumens')
        safe_cache_set(list_cache_key, active_brightnesses, CACHE_TIMEOUT)
    return {
        'active_brightnesses': active_brightnesses,
        'request_path': request_path
    }

@register.inclusion_tag("tags/g_nav_brightness_list.html")
def g_nav_brightness_list(request_path):
    # the request_path might be the path for a series under a brand
    # request_path = /catalog/brand/itp/l-series/
    if request_path.count('/') == 5:
        request_path = request_path.rstrip('/')
        request_path, sep, garbage = request_path.rpartition('/')
        request_path = request_path + sep


    list_cache_key = CACHE_PREFIX + 'max_output_list'
    active_brightnesses = cache.get(list_cache_key)
    if not active_brightnesses:
        active_brightnesses = BrightnessRange.active.all().order_by('min_lumens')
        safe_cache_set(list_cache_key, active_brightnesses, CACHE_TIMEOUT)
    return {
        'active_brightnesses': active_brightnesses,
        'request_path': request_path
    }



@register.inclusion_tag("tags/feature_list.html")
def feature_list(product):
    attribute_cache_key = CACHE_PREFIX + 'product_top_attribute_list_' + product.slug
    top_attributes = cache.get(attribute_cache_key)
    if not top_attributes:
        top_attributes = product.topattributes_set.all()
        safe_cache_set(attribute_cache_key, top_attributes, CACHE_TIMEOUT)

    features_8th = []
    if not top_attributes:
        feature_cache_key = CACHE_PREFIX + 'product_feature_list_' + product.slug
        features = cache.get(feature_cache_key)
        if not features:
            features_str = product.features
            if not features_str:
                features_str = "Click to see the product details page"
            features = features_str.split(';')
            safe_cache_set(feature_cache_key, features)
        features_8th = features[0:5]

    return { 'features': features_8th,
             'top_attributes': top_attributes
    }

@register.inclusion_tag("tags/product_individual_choices.html")
def individual_choices(optionalchoices):
    list_cache_key = CACHE_PREFIX + 'individual_choices_list_' + optionalchoices.product.slug + optionalchoices.title_normalize
    ic = cache.get(list_cache_key)
    if not ic:
        ic = optionalchoices.individualchoice_set.all()
        safe_cache_set(list_cache_key, ic, CACHE_TIMEOUT)

    return { 'individual_choices': ic }

@register.inclusion_tag("tags/cart_item_options.html")
def cart_options_list(cartitem):
    cio = cartitem.cartitemoption_set.all()
    return { 'cio': cio }

@register.inclusion_tag("tags/testimonial_nav.html")
def testimonial_tag():
    testimonials = Testimonial.objects.all()[0:4]
    return { 'testimonials': testimonials }

@register.inclusion_tag("tags/brands_nav.html")
def all_brands_tag():
    brand_cache_key = CACHE_PREFIX + 'active_brand_link_list'
    active_brands = cache.get(brand_cache_key)
    if not active_brands:
        active_brands = Brand.active.all().order_by('ranking')
        safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
    return { 'active_brands': active_brands }

@register.inclusion_tag("tags/newarrivals_nav.html")
def newarrivals_tag():
    newarrivals_cache_key = CACHE_PREFIX + "newarrivals_"
    new_arrivals = cache.get(newarrivals_cache_key)
    if not new_arrivals:
          new_arrivals = Product.new_arrivals.all()
          safe_cache_set(newarrivals_cache_key, new_arrivals, CACHE_TIMEOUT)
    return { 'active_newarrivals': new_arrivals }

@register.inclusion_tag("tags/dealoftheday_nav.html")
def dealoftheday_tag():
    deals_cache_key = CACHE_PREFIX + 'active_deals_'
    dealoftheday = cache.get(deals_cache_key)
    if not dealoftheday or len(dealoftheday) == 0:
        dealoftheday = []
        deals = DealOfTheDay.active.all()
        for d in deals:
            product = d.product
            dealoftheday.append(product)
            safe_cache_set(deals_cache_key, dealoftheday, CACHE_TIMEOUT)

    return { 'active_deals': dealoftheday }

@register.simple_tag
def all_active_brands():
    brand_cache_key = CACHE_PREFIX + 'active_brand_link_list'
    active_brands = cache.get(brand_cache_key)
    if not active_brands:
        active_brands = Brand.active.all().order_by('ranking')
        safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
    return active_brands


@register.simple_tag
def dealoftheday_all():
    deals_cache_key = CACHE_PREFIX + 'active_deals_'
    dealoftheday = cache.get(deals_cache_key)
    if not dealoftheday or len(dealoftheday) == 0:
        dealoftheday = []
        deals = DealOfTheDay.active.all()
        for d in deals:
            product = d.product
            dealoftheday.append(product)
            safe_cache_set(deals_cache_key, dealoftheday, CACHE_TIMEOUT)

    return dealoftheday

@register.simple_tag
def active_promotion():
    promotion_cache_key = CACHE_PREFIX + 'active_promotion_'
    promos = cache.get(promotion_cache_key)
    if not promos or len(promos) == 0:
        curr = datetime.now()
        promos = Promotion.objects.filter(valid_until__gte=curr).exclude(valid_from__gte=curr).exclude(title__isnull=True).exclude(title__exact='')
        safe_cache_set(promotion_cache_key, promos, CACHE_TIMEOUT)

    return promos

@register.simple_tag
def active_todaysnews():
    todaysnews_cache_key = CACHE_PREFIX + 'todaysnews_'
    todaysnews = cache.get(todaysnews_cache_key)
    if not todaysnews or len(todaysnews) == 0:
        curr = datetime.now()
        news = TodaysNews.objects.filter(valid_until__gte=curr).exclude(valid_from__gte=curr).exclude(title__isnull=True).exclude(title__exact='').order_by('order')
        safe_cache_set(todaysnews_cache_key, news, CACHE_TIMEOUT)

    return news


@register.simple_tag
def promotion_products(promo):
   p = []
   try:
        pop = promo.productonlypromotion
        p = pop.products.all().order_by('name')
   except ProductOnlyPromotion.DoesNotExist:
        pass

   return p

@register.inclusion_tag("tags/rebate.html")
def rebate_tag():
    curr = datetime.now()
    banners = BannerControl.objects.filter(valid_to__gte=curr).exclude(valid_from__gte=curr)
    return { 'banners': banners}


@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""

@register.simple_tag
def navselected(request, cur_submenu):
    if cur_submenu == 'show_category' or cur_submenu == 'show_brand' or cur_submenu == 'show_pricerange' or cur_submenu == 'show_brightnessrange' or cur_submenu in request.path:
        return "selected"
    return ""

@register.simple_tag
def sortdropdownselected(request, val):
    if request.session.get('sortby') == val:
        return "SELECTED"
    return ""

@register.simple_tag
def departmentselected(request, d):
    if request.session.get('current_store') == d.slug:
        return "SELECTED"
    return ""

@register.simple_tag
def belong2department(request, d):
    path = request.path

    if "price" in path or "brightness" in path or "bundle" in path:
       if "flashlight" in d.slug:
            return "SELECTED"
       else:
            return ""

    s = find_between(path, "-product-", "/")
    try:
         product = Product.active.get(slug=s)
         if product:
              dep = product.brand.department.slug
    except:
        s = find_between(path, "-category-", "/")
        try:
            cat = Category.active.get(slug=s)
            if cat:
                dep = cat.department.slug
        except:
            s = find_between(path, "/category/", "/")
            try:
                cat = Category.active.get(slug=s)
                if cat:
                    dep = cat.department.slug
            except:
                s = find_between(path, "/brand/", "/")
                try:
                    b = Brand.active.get(slug=s)
                    if b:
                        dep = b.department.slug
                except:
                    s = find_between(path, "-brand-", "/")
                    try:
                        b = Brand.active.get(slug=s)
                        if b:
                            dep = b.department.slug

                    except:
                        dep = "not found"

    if dep == d.slug:
        return "SELECTED"
    return ""

@register.simple_tag
def half(val):
    return round(val/2)

@register.simple_tag
def banner_image_url(a):
    pos = a.rfind('.')
    b = a[:pos] + '.banner.' + a[pos+1:]
    return b

@register.simple_tag
def large_image_url(a):
    pos = a.rfind('.')
    b = a[:pos] + '.large.' + a[pos+1:].lower()
    return b

@register.simple_tag
def thumbnail_image_url(a):
    pos = a.rfind('.')
    b = a[:pos] + '.thumbnail.' + a[pos+1:].lower()
    return b

@register.simple_tag
def super_image_url(a):
    pos = a.rfind('.')
    b = a[:pos] + '.super.' + a[pos+1:].lower()
    return b

@register.simple_tag
def enclose_description_with_div(a):
    b = '<div id="richtext" style="width:95%;">' + a + '</div>'
    from django.utils.safestring import mark_safe
    return mark_safe(b)


@register.simple_tag
def is_flashlight_department(d):
    if 'flashlight'.lower() in d.name.lower():
         return True
    else:
         return False

@register.simple_tag
def current_domain():
    return Site.objects.get_current().domain

@register.simple_tag
def secure_domain():
    return 'https://{}'.format(Site.objects.get_current().domain)

@register.simple_tag(takes_context=True)
def get_seo_tags(context):
    request = context["request"]
    url = request.path
    if "catalog-product-" in url:
        try:
            s = find_between(url, "catalog-product-", "/")
            tag_cache_key = CACHE_PREFIX + 'tag_product_' + s
            tags = cache.get(tag_cache_key)
            if not tags:
                p = get_object_or_404(Product, slug=s)
                tags = {"meta_keywords": not_null(p.seo_meta_keyword, p.meta_keywords),
                        "meta_description": not_null(p.seo_meta_description, p.meta_description),
                        "title": not_null(p.seo_title, p.meta_description),
                        "og_title": not_null(p.seo_og_title, p.meta_description),
                        "og_description": not_null(p.seo_og_description, p.meta_description),
                        "h1_tag": not_null(p.seo_h1_tag, p.meta_description)}
                safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
            return tags
        except Exception:
            pass
    if "catalog-category-" in url and url.count("/") == 2:
        try:
            s = find_between(url, "catalog-category-", "/")
            tag_cache_key = CACHE_PREFIX + 'tag_category_' + s
            tags = cache.get(tag_cache_key)
            if not tags:
                p = get_object_or_404(Category, slug=s)
                tags = {"meta_keywords": p.meta_keywords,
                        "meta_description": p.meta_description,
                        "title": not_null(p.seo_title, p.meta_description),
                        "og_title": not_null(p.seo_og_title, p.meta_description),
                        "og_description": not_null(p.seo_og_description, p.meta_description),
                        "h1_tag": not_null(p.seo_h1_tag, p.meta_description)}
                safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
            return tags
        except Exception:
            pass
    if "catalog-category-" in url and url.count("/") == 3:
        try:
            url_path = url.rstrip('/')
            a,b,s = url_path.rpartition('/')
            tag_cache_key = CACHE_PREFIX + 'tag_subcategory_' + s
            tags = cache.get(tag_cache_key)
            if not tags:
                p = get_object_or_404(SubCategory, slug=s)
                tags = {"meta_keywords": p.meta_keywords,
                        "meta_description": p.meta_description,
                        "title": not_null(p.seo_title, p.meta_description),
                        "og_title": not_null(p.seo_og_title, p.meta_description),
                        "og_description": not_null(p.seo_og_description, p.meta_description),
                        "h1_tag": not_null(p.seo_h1_tag, p.meta_description)}
                safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
            return tags
        except Exception:
            pass
    if "catalog-brand-" in url and url.count("/") == 2:
        try:
            s = find_between(url, "catalog-brand-", "/")
            tag_cache_key = CACHE_PREFIX + 'tag_brand_' + s
            tags = cache.get(tag_cache_key)
            if not tags:
                p = get_object_or_404(Brand, slug=s)
                tags = {"meta_keywords": p.meta_keywords,
                        "meta_description": p.meta_description,
                        "title": not_null(p.seo_title, p.meta_description),
                        "og_title": not_null(p.seo_og_title, p.meta_description),
                        "og_description": not_null(p.seo_og_description, p.meta_description),
                        "h1_tag": not_null(p.seo_h1_tag, p.meta_description)}
                safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
            return tags
        except Exception:
            pass
    if "catalog-brand-" in url and url.count("/") == 3:
        try:
            url_path = url.rstrip('/')
            a,b,s = url_path.rpartition('/')
            tag_cache_key = CACHE_PREFIX + 'tag_series_' + s
            tags = cache.get(tag_cache_key)
            if not tags:
                p = get_object_or_404(Series, slug=s)
                tags = {"meta_keywords": p.meta_keywords,
                        "meta_description": p.meta_description,
                        "title": not_null(p.seo_title, p.meta_description),
                        "og_title": not_null(p.seo_og_title, p.meta_description),
                        "og_description": not_null(p.seo_og_description, p.meta_description),
                        "h1_tag": not_null(p.seo_h1_tag, p.meta_description)}
                safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
            return tags
        except Exception:
            pass
    if "catalog-store" in url and url.count("/") == 3:
        try:
            url_path = url.rstrip('/')
            a,b,s = url_path.rpartition('/')
            tag_cache_key = CACHE_PREFIX + 'tag_store_' + s
            tags = cache.get(tag_cache_key)
            if not tags:
                p = get_object_or_404(Department, slug=s)
                tags = {"meta_keywords": p.meta_keywords,
                        "meta_description": p.meta_description,
                        "title": not_null(p.seo_title, p.meta_description),
                        "og_title": not_null(p.seo_og_title, p.meta_description),
                        "og_description": not_null(p.seo_og_description, p.meta_description),
                        "h1_tag": not_null(p.seo_h1_tag, p.meta_description)}
                safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
            return tags
        except Exception:
            pass

    tag_cache_key = CACHE_PREFIX + 'tag_others_'
    tags = cache.get(tag_cache_key)
    if not tags:
        tags = {"meta_keywords": SITE_SEO_META_KEYWORDS,
                "meta_description": SITE_SEO_META_DESCRIPTION,
                "title": SITE_SEO_TITLE,
                "og_title": SITE_SEO_OG_TITLE,
                "og_description": SITE_SEO_OG_DESCRIPTION,
                "h1_tag": SITE_SEO_H1_TAG}
        safe_cache_set(tag_cache_key, tags, CACHE_TIMEOUT)
    return tags

@register.inclusion_tag("tags/testimonials.html")
def testimonials_tag():
    testimonials_cache_key = CACHE_PREFIX + "testimonials_"
    testimonials = cache.get(testimonials_cache_key)
    if not testimonials:
          testimonials = Testimonial.objects.all()
          safe_cache_set(testimonials_cache_key, testimonials, CACHE_TIMEOUT)
    return { 'active_testimonials': testimonials }


@register.simple_tag
def active_blogs():
    list_cache_key = CACHE_PREFIX + 'active_blogs_link_list'
    blogs = cache.get(list_cache_key)
    print (blogs)
    if not blogs:
        blogs = Reclaimed_Blog.active.all().order_by('ranking')
        safe_cache_set(list_cache_key, blogs, CACHE_TIMEOUT)
    return blogs
