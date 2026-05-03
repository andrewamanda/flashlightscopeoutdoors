from django.shortcuts import get_object_or_404, render
from ecomstore.catalog.models import Department, Category, Product, ProductReview, Brand, Series, SubCategory, DealOfTheDay, accessory_product, PriceRange, BrightnessRange
from ecomstore.catalog.forms import ProductAddToCartForm, ProductReviewForm, ProductQuestionForm
from django.template import RequestContext

from django.urls import reverse
from ecomstore.cart import cart
from django.http import HttpResponseRedirect, HttpResponse

from ecomstore.stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW, NUM_OF_NEW_ARRIVALS, SITE_VERSION

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
#from django.utils import simplejson
import json as simplejson
from ecomstore.settings import UPCOMING_DEAL_ANNOUNCEMENT

import tagging
from tagging.models import Tag, TaggedItem

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME
import datetime
from ecomstore.catalog import deal_processor
from django.db.models import Avg

from ecomstore.utils.captcha import createCaptcha, verifyCaptcha
import string
from django.http import HttpResponsePermanentRedirect

from django.shortcuts import render
from .forms import TestImageForm
def test_widget_view(request):
    form = TestImageForm()
    return render(request, 'catalog/test_widget.html', {'form': form})
def test_template_view(request):
    return render(request, 'catalog/bulk_image_upload.html')
from .forms import AdditionalImagesForm


from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

def safe_cache_set(key, value, timeout=CACHE_TIMEOUT, request=None):
    """
    Safely set cache values.

    Memcached pickles values before storing them. Some Django model/queryset objects
    containing StdImageFieldFile can fail during pickling with errors like:
    "'StdImageFieldFile' object has no attribute 'super'" or "'large'".

    This helper prevents safe_cache_set() failures from causing 500 errors.
    """
    try:
        cache.set(key, value, timeout)
    except Exception as e:
        print(
            f"\n[CACHE SKIPPED - views]\n"
            f"Key: {key}\n"
            f"Path: {getattr(request, 'path', 'N/A')}\n"
            f"Value Type: {type(value).__name__ if value is not None else 'None'}\n"
            f"Value Repr: {repr(value)[:200] if value is not None else 'None'}\n"
            f"Error: {e}\n"
        )

from django.shortcuts import redirect

def test_image_upload(request):
    if request.method == 'POST':
        form = AdditionalImagesForm(request.POST, request.FILES)
        print(f"Files received: {request.FILES}")
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            print(form.errors)
    else:
        form = AdditionalImagesForm()

    return render(request, 'catalog/test_image_upload.html', {'form': form})

def index(request, template_name="catalog/index.html"):
    """ site home page , temporarily fix a problem with RMA overflow"""

    url = "/"
    return HttpResponseRedirect(url)

    search_recs = stats.recommended_from_search(request)

    featured_cache_key = 'featured_products_'
    try:
        featured = cache.get(featured_cache_key)
    except:
        featured = None
    if not featured:
        featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
        try:
            safe_cache_set(featured_cache_key, featured, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    recently_viewed = stats.get_recently_viewed(request)
    view_recs = stats.recommended_from_views(request)

    new_arrivals_cache_key = 'new_arrivals_products_'
    try:
        new_arrivals = cache.get(new_arrivals_cache_key)
    except:
        new_arrivals = None
    if not new_arrivals:
        new_arrivals = Product.new_arrivals.all()[0:NUM_OF_NEW_ARRIVALS]
        try:
            safe_cache_set(new_arrivals_cache_key, new_arrivals, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    clearance_products_cache_key = 'clearance_products_'
    try:
        clearance_products = cache.get(clearance_products_cache_key)
    except:
        clearance_products = None
    if not clearance_products:
        clearance_products = Product.clearance_products.all()[0:NUM_OF_NEW_ARRIVALS]
        try:
            safe_cache_set(clearance_products_cache_key, clearance_products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    page_title = SITE_NAME + ' | Hunting supplies for hunting enthusiasts'
    return render(request, template_name, locals())

def normalize_sortby(sortby):
    if 'Des' in sortby:
        reverse = True
    if 'title' in sortby:
        sortby = 'name'
    else:
        if 'price' in sortby:
            sortby = 'price'
        else:
            if 'lumen' in sortby:
                sortby = 'max_lumens'
            else:
                sortby = 'ranking'
    return sortby

def show_alldepartments(request, template_name="catalog/all_departments.html"):
    """ view for each individual category page """

    fullurl = request.build_absolute_uri()
    if "catalog/all_" in fullurl:
        newurl = fullurl.replace("catalog/all_", "catalog-all_")
        return HttpResponsePermanentRedirect(newurl)


    departments_cache_key = 'all_departments_'

    try:
        departments = cache.get(departments_cache_key)
    except:
        departments = None
    if not departments:
        departments = Department.active.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(departments_cache_key, departments, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    page_title = "All Stores"

    method = 'show_alldepartments'

    if request.flavour == 'mobile':
         template_name = 'mobile/home/subcategories.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

    from django.db import connection
    queries = connection.queries

    return render(request, template_name, locals())

def show_allbundles(request, template_name="catalog/category.html"):
    """ view for each individual category page """
    fullurl = request.build_absolute_uri()
    if "catalog/all_bundles/" in fullurl:
        newurl = fullurl.replace("catalog/all_bundles/", "catalog-all_bundles/")
        return HttpResponsePermanentRedirect(newurl)


    bundle_categories = Category.active.filter(slug__contains = 'bundle')
    bundles_cache_key = 'all_bundles_'
    products = cache.get(bundles_cache_key)
    if not products:
        products = Product.active.filter(categories__in=bundle_categories)
        try:
            safe_cache_set(bundles_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    page_title = "All bundles"

    method = 'show_allbundles'

    if request.flavour == 'mobile':
         template_name = 'mobile/home/subcategories.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

    from django.db import connection
    queries = connection.queries

    return render(request, template_name, locals())

def show_category(request, category_slug, template_name="catalog/category.html"):
    """ view for each individual category page """

    if SITE_VERSION == "NEW_SKIN":
        template_name = "2023/catalog/category.html"

    fullurl = request.build_absolute_uri()
    if "catalog/category/" in fullurl:
        newurl = fullurl.replace("catalog/category/", "catalog-category-")
        return HttpResponsePermanentRedirect(newurl)


    request.session['last_path'] = request.path

    category_cache_key = request.path
    try:
        page_subjects = cache.get(category_cache_key)
    except:
        page_subjects = None
    if not page_subjects:
        page_subjects = get_object_or_404(Category.active, slug=category_slug)
        try:
            safe_cache_set(category_cache_key, page_subjects, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    sortby = request.GET.get('sortby','titleAsc')

    request.session['sortby'] = sortby


    list_cache_key = 'products_in_category_' + sortby + '_' + page_subjects.slug

    reverse = False
    if 'Des' in sortby:
        reverse = True
    sortby = normalize_sortby(sortby)

    try:
        products = cache.get(list_cache_key)
    except:
        products = None
    if not products:
        if reverse:
            products = page_subjects.product_set.filter(is_active=True).order_by(sortby).reverse()
        else:
            products = page_subjects.product_set.filter(is_active=True).order_by(sortby)
        try:
            safe_cache_set(list_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    page_title = page_subjects.name
    meta_keywords = page_subjects.meta_keywords
    meta_description = page_subjects.meta_description

    method = 'show_category'

    subcategory_cache_key = 'active_subcategory_link_list_' + category_slug
    try:
        active_submenu = cache.get(subcategory_cache_key)
    except:
        active_submenu = None
    if not active_submenu:
        active_submenu = page_subjects.subcategory_set.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(subcategory_cache_key, active_submenu, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    url = request.path
    if request.method == 'POST':
        #print request.POST.get('sortby')
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")

        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/subcategories.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

    from django.db import connection
    queries = connection.queries

    return render(request, template_name, locals())

def show_subcategory(request, category_slug, subcategory_slug, template_name="catalog/category.html"):
    """ view for each individual category page """
    subcategory_cache_key = request.path

    fullurl = request.build_absolute_uri()
    if "catalog/category/" in fullurl:
        newurl = fullurl.replace("catalog/category/", "catalog-category-")
        return HttpResponsePermanentRedirect(newurl)

    method = 'show_subcategory'

    try:
        page_subjects = cache.get(subcategory_cache_key)
    except:
        page_subjects = None
    if not page_subjects:
        page_subjects = get_object_or_404(SubCategory.active, slug=subcategory_slug)
        try:
            safe_cache_set(subcategory_cache_key, page_subjects, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    #products = page_subjects.product_set.filter(is_active=True).order_by('ranking')
    page_title = page_subjects.name
    meta_keywords = page_subjects.meta_keywords
    meta_description = page_subjects.meta_description

    category_cache_key,sep,garbage = request.path.rpartition('/')
    try:
        c = cache.get(category_cache_key)
    except:
        c = None
    if not c:
        c = get_object_or_404(Category.active, slug=category_slug)
        try:
            safe_cache_set(category_cache_key, c, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    subcategory_cache_key = 'active_subcategory_link_list_' + category_slug
    try:
        active_submenu = cache.get(subcategory_cache_key)
    except:
        active_submenu = None
    if not active_submenu:
        active_submenu = c.subcategory_set.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(subcategory_cache_key, active_submenu, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    sortby = request.GET.get('sortby','titleAsc')
    request.session['sortby'] = sortby


    list_cache_key = 'products_in_subcategory_' + sortby + '_' + subcategory_slug

    reverse = False
    if 'Des' in sortby:
        reverse = True
    sortby = normalize_sortby(sortby)

    try:
        products = cache.get(list_cache_key)
    except:
        products = None
    if not products:
        if reverse:
            products = c.product_set.filter(is_active=True).filter(subcategory__slug=subcategory_slug).order_by(sortby).reverse()
        else:
            products = c.product_set.filter(is_active=True).filter(subcategory__slug=subcategory_slug).order_by(sortby)
        try:
            safe_cache_set(list_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

    from django.db import connection
    queries = connection.queries

    return render(request, template_name, locals())

def show_brand(request, brand_slug, template_name="catalog/category.html"):
    """ view for each individual brand page """

    fullurl = request.build_absolute_uri()
    if "catalog/brand/" in fullurl:
        newurl = fullurl.replace("catalog/brand/", "catalog-brand-")
        return HttpResponsePermanentRedirect(newurl)


    request.session['last_path'] = request.path

    brand_cache_key = request.path
    try:
        page_subjects = cache.get(brand_cache_key)
    except:
        page_subjects = None
    if not page_subjects:
        page_subjects = get_object_or_404(Brand.active, slug=brand_slug)
        try:
            safe_cache_set(brand_cache_key, page_subjects, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    sortby = request.GET.get('sortby','titleAsc')
    request.session['sortby'] = sortby


    list_cache_key = 'products_in_brand_' + sortby + '_' + page_subjects.slug

    reverse = False
    if 'Des' in sortby:
        reverse = True
    sortby = normalize_sortby(sortby)

    try:
        products = cache.get(list_cache_key)
    except:
        products = None
    if not products:
        if reverse:
            products = page_subjects.product_set.filter(is_active=True).order_by(sortby).reverse()
        else:
            products = page_subjects.product_set.filter(is_active=True).order_by(sortby)
        try:
            safe_cache_set(list_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache key: {e}")

    page_title = page_subjects.name
    meta_keywords = page_subjects.meta_keywords
    meta_description = page_subjects.meta_description

    method = 'show_brand'
    series_cache_key = 'active_series_link_list_' + brand_slug
    try:
        active_submenu = cache.get(series_cache_key)
    except:
        active_submenu = None
    if not active_submenu:
        active_submenu = page_subjects.series_set.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(series_cache_key, active_submenu, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/brandseries.html'

         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

    from django.db import connection
    queries = connection.queries

    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)
    return render(request, template_name, locals())

def show_series(request, brand_slug, series_slug, template_name="catalog/category.html"):
    """ view for each individual brand page """
    """ this method is currently not used """

    fullurl = request.build_absolute_uri()
    if "catalog/brand/" in fullurl:
        newurl = fullurl.replace("catalog/brand/", "catalog-brand-")
        return HttpResponsePermanentRedirect(newurl)

    series_cache_key = request.path
    try:
        page_subjects = cache.get(series_cache_key)
    except:
        page_subjects = None
    if not page_subjects:
        page_subjects = get_object_or_404(Series.active, slug=series_slug)
        try:
            safe_cache_set(series_cache_key, page_subjects, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    #products = page_subjects.product_set.filter(is_active=True).order_by('ranking')
    page_title = page_subjects.name
    meta_keywords = page_subjects.meta_keywords
    meta_description = page_subjects.meta_description

    method = 'show_brandseries'

    brand_cache_key,sep,garbage = request.path.rpartition('/')
    try:
        b = cache.get(brand_cache_key)
    except:
        b = None
    if not b:
        b = get_object_or_404(Brand.active, slug=brand_slug)
        try:
            safe_cache_set(brand_cache_key, b, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    series_cache_key = 'active_series_link_list_' + brand_slug
    try:
        active_submenu = cache.get(series_cache_key)
    except:
        active_submenu = None
    if not active_submenu:
        active_submenu = b.series_set.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(series_cache_key, active_submenu, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    sortby = request.GET.get('sortby','titleAsc')
    request.session['sortby'] = sortby

    list_cache_key = 'products_in_brand_' + sortby + '_' + page_subjects.slug

    reverse = False
    if 'Des' in sortby:
        reverse = True
    sortby = normalize_sortby(sortby)

    try:
        products = cache.get(list_cache_key)
    except:
        products = None
    if not products:
        if reverse:
            products = page_subjects.product_set.filter(is_active=True).order_by(sortby).reverse()
        else:
            products = page_subjects.product_set.filter(is_active=True).order_by(sortby)
        try:
            safe_cache_set(list_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")


    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)


    #from django.db import connection
    #queries = connection.queries

    return render(request, template_name, locals())

def show_pricerange(request, priceranges_slug, template_name="catalog/category.html"):
    """ view for each individual brand page """

    request.session['last_path'] = request.path

    current_depart = get_object_or_404(Department.active, slug__contains='flashlight')
    price_cache_key = request.path
    try:
        page_subjects = cache.get(price_cache_key)
    except:
        active_brands = None
    if not page_subjects:
        page_subjects = get_object_or_404(PriceRange.active, slug=priceranges_slug)
        try:
            safe_cache_set(price_cache_key, page_subjects, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    sortby = request.GET.get('sortby','titleAsc')
    request.session['sortby'] = sortby


    list_cache_key = 'products_in_pricerange_' + sortby + '_' + page_subjects.slug

    reverse = False
    if 'Des' in sortby:
        reverse = True
    sortby = normalize_sortby(sortby)
    try:
        products = cache.get(list_cache_key)
    except:
        products = None
    if not products:
        if not page_subjects.max_price:
            page_subjects.max_price = page_subjects.min_price * 100
        if reverse:
            products = Product.active.filter(brand__department__slug__contains='flashlight',price__gte=page_subjects.min_price).exclude(price__gte=page_subjects.max_price).order_by(sortby).reverse()
        else:
            products = Product.active.filter(brand__department__slug__contains='flashlight',price__gte=page_subjects.min_price).exclude(price__gte=page_subjects.max_price).order_by(sortby)
        try:
            safe_cache_set(list_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    page_title = page_subjects.description
    meta_keywords = 'LED Flashlights'
    meta_description = 'Andrew & Amanda LED Flashlights'

    method = 'show_pricerange'

    active_flashlight_brands_cache_key = 'active_flashlight_brands_link_list_'
    try:
        active_flashlight_brands = cache.get(active_flashlight_brands_cache_key)
    except:
        active_flashlight_brands = None
    if not active_flashlight_brands:
        active_flashlight_brands = Brand.active.filter(department__slug__contains='flashlight').order_by('ranking')
        try:
            safe_cache_set(active_flashlight_brands_cache_key, active_flashlight_brands, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)


    from django.db import connection
    queries = connection.queries

    return render(request, template_name, locals())

def show_brightnessrange(request, brightnessranges_slug, template_name="catalog/category.html"):
    """ view for each individual brand page """

    request.session['last_path'] = request.path

    current_depart = get_object_or_404(Department.active, slug__contains='flashlight')
    brightness_cache_key = request.path
    try:
        page_subjects = cache.get(brightness_cache_key)
    except:
        page_subjects = None
    if not page_subjects:
        page_subjects = get_object_or_404(BrightnessRange.active, slug=brightnessranges_slug)
        try:
            safe_cache_set(brightness_cache_key, page_subjects, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    sortby = request.GET.get('sortby','titleAsc')
    request.session['sortby'] = sortby


    list_cache_key = 'products_in_brightnessrange_' + sortby + '_' + page_subjects.slug

    reverse = False
    if 'Des' in sortby:
        reverse = True
    sortby = normalize_sortby(sortby)

    try:
        products = cache.get(list_cache_key)
    except:
        products = None
    if not products:
        if not page_subjects.max_lumens:
            page_subjects.max_lumens = page_subjects.min_lumens * 100
        if reverse:
            products = Product.active.filter(brand__department__slug__contains='flashlight',max_lumens__gte=page_subjects.min_lumens).exclude(max_lumens__gte=page_subjects.max_lumens).order_by(sortby).reverse()
        else:
            products = Product.active.filter(brand__department__slug__contains='flashlight',max_lumens__gte=page_subjects.min_lumens).exclude(max_lumens__gte=page_subjects.max_lumens).order_by(sortby)
        try:
            safe_cache_set(list_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    page_title = page_subjects.description
    meta_keywords = 'LED Flashlights'
    meta_description = 'Andrew & Amanda LED Flashlights'

    method = 'show_brightnessrange'

    active_flashlight_brands_cache_key = 'active_flashlight_brands_link_list_'
    try:
        active_flashlight_brands = cache.get(active_flashlight_brands_cache_key)
    except:
        active_flashlight_brands = None
    if not active_flashlight_brands:
        active_flashlight_brands = Brand.active.filter(department__slug__contains='flashlight').order_by('ranking')
        try:
            safe_cache_set(active_flashlight_brands_cache_key, active_flashlight_brands, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    brands_cache_key = 'active_brands_link_list_' + brightnessranges_slug
    try:
        active_submenu = cache.get(brands_cache_key)
    except:
        active_submenu = None
    if not active_submenu:
        active_submenu = Brand.active.filter(department__slug__contains='flashlight').order_by('ranking')

        excludes = []
        for brand in active_submenu.all():
            no_product = True
            for p in products:
                if p.brand.slug == brand.slug:
                    no_product = False
                    break
            if no_product == True:
                excludes.append(brand.slug)

        active_submenu = active_submenu.exclude(slug__in=excludes)

        try:
            safe_cache_set(brands_cache_key, active_submenu, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)


    from django.db import connection
    queries = connection.queries

    return render(request, template_name, locals())



def show_store(request, department_slug, template_name="catalog/store.html"):
    """ view for each individual brand page """
    fullurl = request.build_absolute_uri()
    if "catalog/store/" in fullurl:
        newurl = fullurl.replace("catalog/store/", "catalog-store/")
        return HttpResponsePermanentRedirect(newurl)


    request.session['last_path'] = request.path
    request.session['current_store'] = department_slug

    department_cache_key = request.path
    try:
        d = cache.get(department_cache_key)
    except:
        d = None
    if not d:
        d = get_object_or_404(Department.active, slug=department_slug)
        try:
            safe_cache_set(department_cache_key, d, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    list_cache_key = 'active_category_link_list_' + d.slug
    try:
        active_categories = cache.get(list_cache_key)
    except:
        active_categories = None
    if not active_categories:
        active_categories = d.category_set.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    brand_list_cache_key = 'active_brand_link_list_' + d.slug
    try:
        active_brands = cache.get(brand_list_cache_key)
    except:
        active_brands = None
    if not active_brands:
        active_brands = d.brand_set.filter(is_active=True).order_by('ranking')
        try:
            safe_cache_set(brand_list_cache_key, active_brands, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    page_title = d.name
    meta_keywords = 'LED Flashlights'
    meta_description = 'Andrew & Amanda LED Flashlights'

    method = 'show_store'

    return render(request, template_name, locals())

def show_related(request):
    import json

    if request.method != "POST":
        return HttpResponse(
            json.dumps({"data": [], "message": "This endpoint handles add-to-cart for manually curated related items."}),
            content_type='application/json'
        )

    try:
        slug = request.POST.get("slug")
        quantity = int(request.POST.get("quantity", 1) or 1)
        if quantity < 1:
            quantity = 1

        p = get_object_or_404(Product.active, slug=slug)
        cart.add_buyitnow_to_cart(request, p, quantity)
        total = cart.cart_distinct_item_count(request)
        messages.success(request, "Shopping cart updated.")
        payload = {"success": "True", "cart_count": str(total)}
    except Exception as e:
        logger.exception("Error processing related add_to_cart POST: %s", e)
        msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
        messages.error(request, f"Error: {msg}")
        payload = {"success": "False", "cart_count": str(cart.cart_distinct_item_count(request)), "message": msg}

    return HttpResponse(json.dumps(payload), content_type='application/json')



def show_product(request, product_slug, template_name="catalog/product.html"):
    """ view for each product page """

    if SITE_VERSION == "NEW_SKIN":
        template_name = "2023/catalog/product.html"

    fullurl = request.build_absolute_uri()
    if "catalog/product/" in fullurl:
        newurl = fullurl.replace("catalog/product/", "catalog-product-")
        return HttpResponsePermanentRedirect(newurl)


    """ this is a workaround if a product is not navigated  and clicked from the left nav section """
    last_path = request.session.get('last_path', '/catalog/category/led-flashlights/')
    request.session['last_path'] = last_path
    request.session['product_slug'] = product_slug


    product_cache_key = request.path
    # try to get product from cache
    try:
        p = cache.get(product_cache_key)
    except:
        p = None
    # if a cache miss, fall back on db query

    if not p:
        p = get_object_or_404(Product.active, slug=product_slug)
        # store item in cache for next time
        try:
            safe_cache_set(product_cache_key, p, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")
    product_category_cache_key = 'product_category_list_' + p.slug
    try:
        categories = cache.get(product_category_cache_key)
    except:
        categories = None
    if not categories:
        categories = p.categories.filter(is_active=True)
        try:
            safe_cache_set(product_category_cache_key, categories)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    # for backward compatibility, it accomodates the previous features with ; as the list delimiter;
    # now it uses the tinymce rich editor
    # if not p.features.startswith('<p>'):
    feature_cache_key = 'product_feature_list_' + p.slug
    try:
        features = cache.get(feature_cache_key)
    except:
        features = None
    if not features:
       features_str = p.features
       if not features_str:
            features_str = "Click to see the product details page"
       features = features_str.split(';')
       try:
           safe_cache_set(feature_cache_key, features)
       except Exception as e:
           print(f"Invalid Cache Key: {e}")

    new_arrivals_cache_key = 'new_arrivals_products_'
    try:
        new_arrivals = cache.get(new_arrivals_cache_key)
    except:
        new_arrivals = None
    if not new_arrivals:
        new_arrivals = Product.new_arrivals.all()[0:NUM_OF_NEW_ARRIVALS]
        try:
            safe_cache_set(new_arrivals_cache_key, new_arrivals, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    page_title = p.name
    meta_keywords = p.meta_keywords
    meta_description = p.meta_description
    # evaluate the HTTP method, change as needed
    if request.method == 'POST':
        url = request.path
        postdata = request.POST.copy()


        if product_slug == 'gift-certificate' and (verifyCaptcha(postdata.get('imghash'),postdata.get('imgtext')) == False):
           captcha_error = 'Error on captcha. Please type again.'
           #print captcha_error
           captcha = createCaptcha(request)
           imgpath = captcha['imgpath']
           imghash = captcha['imghash']
           return render(request, template_name, locals())

        #create the bound form
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            try:
                cart.add_to_cart(request)
                messages.success(request, "Shopping cart added.")
            except Exception as e:
                logger.exception("Error processing add_to_cart POST: %s", e)
                msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
                messages.error(request, f"Error: {msg}")
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            # url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
            #return redirect(url)
    else:
        #create the unbound form. Notice the request as a keyword argument

        form = ProductAddToCartForm(request=request, label_suffix=':')

    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set test cookie to make sure cookies are enabled
    request.session.set_test_cookie()
    # temporarily disable because it causes exception after migrating to python 3
    #stats.log_product_view(request, p)
    #return HttpResponse("sfsdkfs")
    # product review additions, CH 10

    product_reviews = ProductReview.approved.filter(product=p).order_by('-date')

    if len(product_reviews) > 0:
       rating__avg = product_reviews.aggregate(Avg('rating'))
       actual_rating = rating__avg['rating__avg']
       normalized_rating = float(int(actual_rating) + 0.5)
       if actual_rating > normalized_rating:
           starRating = int(actual_rating) + 1
       else:
           starRating = str(int(actual_rating)) + '12'
       if actual_rating == int(actual_rating):
           starRating = str(int(actual_rating))

    review_form = ProductReviewForm()

    question_form = ProductQuestionForm()

    is_deal = False
    deal_price = deal_processor.get_effective_price(p)
    if deal_price < p.price:
         is_deal = True
         #p.old_price = p.price
         #p.price = deal_price

    more_choices_cache_key = 'product_more_choices_' + p.slug
    try:
        more_choices = cache.get(more_choices_cache_key)
    except:
        more_choices = None
    if not more_choices:
        more_choices = p.optionalchoices_set.all()
        try:
            safe_cache_set(more_choices_cache_key, more_choices)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    more_images_cache_key = 'product_more_images_' + p.slug
    try:
        more_images = cache.get(more_images_cache_key)
    except:
        more_images = None
    if not more_images:
        more_images = p.additionalimages_set.all()
        try:
            safe_cache_set(more_images_cache_key, more_images)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    accessory_groups_cache_key = 'product_accessory_groups_' + p.slug
    try:
        accessory_groups = cache.get(accessory_groups_cache_key)
    except:
        accessory_groups = None
    if accessory_groups is None:
        accessory_groups = []
        accessory_group_qs = accessory_product.objects.filter(products=p).prefetch_related('accessories')
        for accessory_group in accessory_group_qs:
            items = []
            seen_ids = set()
            for accessory_item in accessory_group.accessories.all():
                if accessory_item.id == p.id or accessory_item.id in seen_ids or not accessory_item.is_active:
                    continue
                seen_ids.add(accessory_item.id)
                items.append(accessory_item)
            if items:
                accessory_groups.append({
                    'title': accessory_group.name,
                    'items': items,
                })
        try:
            safe_cache_set(accessory_groups_cache_key, accessory_groups)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    related_products_to_add = []
    related_seen_ids = set()
    for group in accessory_groups:
        for item in group['items']:
            if item.id in related_seen_ids:
                continue
            related_seen_ids.add(item.id)
            related_products_to_add.append(item)

    has_manual_related_content = bool(related_products_to_add)

    if product_slug == 'gift-certificate':
        captcha = createCaptcha(request)
        imgpath = captcha['imgpath']
        imghash = captcha['imghash']


    if request.flavour == 'mobile':
         template_name = 'mobile/home/product.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
    return render(request, template_name, locals())

def show_deal(request, template_name="catalog/category.html"):
    """ view for each individual category page """

    fullurl = request.build_absolute_uri()
    if "catalog/dealoftheday/" in fullurl:
        newurl = fullurl.replace("catalog/dealoftheday/", "catalog-dealoftheday/")
        return HttpResponsePermanentRedirect(newurl)



    page_title = 'Deal Of the Day ' + UPCOMING_DEAL_ANNOUNCEMENT

    method = 'dealoftheday'
    active_submenu = []

    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

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
        #if not product.sale_price:
        #    product.old_price = product.price
        #product.price = d.deal_price
        #product.quantity = d.quantity
        products.append(product)

        meta_keywords = product.meta_keywords
        meta_description = product.meta_description

    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

    return render(request, template_name, locals())


def show_clearance(request, template_name="catalog/category.html"):
    """ view for each individual category page """
    page_title = 'Clearance Corner ' + UPCOMING_DEAL_ANNOUNCEMENT

    fullurl = request.build_absolute_uri()
    if "catalog/clearance/" in fullurl:
        newurl = fullurl.replace("catalog/clearance/", "catalog-clearance/")
        return HttpResponsePermanentRedirect(newurl)


    method = 'clearance'
    active_submenu = []


    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    clearance_products_cache_key = 'clearance_products_'
    try:
        products = cache.get(clearance_products_cache_key)
    except:
        products = None
    if not products:
        products = Product.clearance_products.all()
        try:
            safe_cache_set(clearance_products_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")


    brands_cache_key = 'active_brands_link_list_clearance'
    try:
        active_submenu = cache.get(brands_cache_key)
    except:
        active_submenu = None
    if not active_submenu:
        active_submenu = Brand.active.all().order_by('ranking')

        excludes = []
        for brand in active_submenu.all():
            no_product = True
            for p in products:
                if p.brand.slug == brand.slug:
                    no_product = False
                    break
            if no_product == True:
                excludes.append(brand.slug)

        active_submenu = active_submenu.exclude(slug__in=excludes)

        try:
            safe_cache_set(brands_cache_key, active_submenu, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
    return render(request, template_name, locals())

def show_promotion(request, template_name="catalog/category.html"):
    """ view for each individual category page """
    page_title = 'Current Promotion '

    fullurl = request.build_absolute_uri()
    if "catalog/promotion/" in fullurl:
        newurl = fullurl.replace("catalog/promotion/", "catalog-promotion/")
        return HttpResponsePermanentRedirect(newurl)


    method = 'promotion'
    active_submenu = []


    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    from ecomstore.catalog.templatetags.catalog_tags import active_promotion, promotion_products
    try:
    	promos = active_promotion()
    	promo = promos[0]
    	products = promotion_products(promo)
    except:
        products = []
    #print "active promotions = ", products

    #promotion_products_cache_key = 'promotion_products_'
    #products = cache.get(promotion_products_cache_key)
    #if not products:
    #    products = Product.clearance_products.all()
    #    safe_cache_set(promotion_products_cache_key, products, CACHE_TIMEOUT)



    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
    return render(request, template_name, locals())


def show_newarrival(request, template_name="catalog/category.html"):
    """ view for each individual category page """

    fullurl = request.build_absolute_uri()
    if "catalog/newarrival/" in fullurl:
        newurl = fullurl.replace("catalog/newarrival/", "catalog-newarrival/")
        return HttpResponsePermanentRedirect(newurl)


    page_title = 'New Arrivals '

    method = 'newarrivals'
    active_submenu = []


    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    newarrivals_products_cache_key = 'newarrival_products_'
    try:
        products = cache.get(newarrivals_products_cache_key)
    except:
        products = None
    if not products:
        products = Product.new_arrivals.all()
        try:
            safe_cache_set(newarrivals_products_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
    return render(request, template_name, locals())


def show_open_box(request, template_name="catalog/category.html"):
    """ view for each individual category page """

    fullurl = request.build_absolute_uri()
    if "catalog/open_box/" in fullurl:
        newurl = fullurl.replace("catalog/open_box/", "catalog-open_box/")
        return HttpResponsePermanentRedirect(newurl)


    page_title = 'Open Box Items '

    method = 'open_box'
    active_submenu = []


    url = request.path
    if request.method == 'POST':
        #add to cart and redirect to cart page
        try:
           cart.add_to_cart(request)
           messages.success(request, "Shopping cart added.")
        except Exception as e:
            logger.exception("Error processing add_to_cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")
        # if test cookie worked, get rid of it
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        return HttpResponseRedirect(url)

    openbox_products_cache_key = 'openbox_products_'
    try:
        products = cache.get(openbox_products_cache_key)
    except:
        products = None
    if not products:
        products = Product.openbox.all()
        try:
            safe_cache_set(openbox_products_cache_key, products, CACHE_TIMEOUT)
        except Exception as e:
            print(f"Invalid Cache Key: {e}")

    if request.flavour == 'mobile':
         template_name = 'mobile/home/products.html'

         list_cache_key = 'active_category_link_list'
         try:
             active_categories = cache.get(list_cache_key)
         except:
             active_categories = None
         if not active_categories:
             active_categories = Category.active.all().order_by('ranking')
             try:
                 safe_cache_set(list_cache_key, active_categories, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")

         brand_cache_key = 'active_brand_link_list'
         try:
             active_brands = cache.get(brand_cache_key)
         except:
             active_brands = None
         if not active_brands:
             active_brands = Brand.active.all().order_by('ranking')
             try:
                 safe_cache_set(brand_cache_key, active_brands, CACHE_TIMEOUT)
             except Exception as e:
                 print(f"Invalid Cache Key: {e}")
    return render(request, template_name, locals())



from tagging.models import Tag
from tagging.utils import calculate_cloud, LOGARITHMIC
from django.utils.encoding import force_str
from django.shortcuts import render

def tag_cloud(request, template_name="catalog/tag_cloud.html"):
    # Filter your products first (replaces the broken filters=...)
    qs = Product.objects.filter(is_active=True)

    # Get tags + counts, then compute cloud
    tags = Tag.objects.usage_for_queryset(qs, counts=True)
    cloud = calculate_cloud(tags, steps=9, distribution=LOGARITHMIC)

    # Normalize to simple dicts, force names to str (not bytes)
    product_tags = []
    for t in cloud:
        name = force_str(getattr(t, "name", ""))   # ← force bytes → str safely
        count = int(getattr(t, "count", 0) or 0)
        size = getattr(t, "font_size", None)
        product_tags.append({"name": name, "count": count, "font_size": size})

    # Only pass what this template needs
    return render(request, template_name, {
        "product_tags": product_tags,
        "page_title": "Product Tag Cloud",
    })

def tag(request, tag, template_name="catalog/tag.html"):
    """ view listing products that have been tagged with a given tag """
    products = TaggedItem.objects.get_by_model(Product.active, tag)
    page_title = 'Products tagged with ' + tag
    return render(request, template_name, locals())


@login_required
def add_review(request):
    """ AJAX view that takes a form POST from a user submitting a new product review;
    requires a valid product slug and args from an instance of ProductReviewForm;
    return a JSON response containing two variables: 'review', which contains
    the rendered template of the product review to update the product page,
    and 'success', a True/False value indicating if the save was successful.
    """
    form = ProductReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        slug = request.POST.get('slug')
        product = Product.active.get(slug=slug)
        review.user = request.user
        review.product = product
        review.save()

        template = "catalog/product_review.html"
        html = render_to_string(template, {'review': review })
        response = simplejson.dumps({'success':'True', 'html': html})

    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def add_question(request):
    """ AJAX view that takes a form POST from a user submitting a new product review;
    requires a valid product slug and args from an instance of ProductReviewForm;
    return a JSON response containing two variables: 'review', which contains
    the rendered template of the product review to update the product page,
    and 'success', a True/False value indicating if the save was successful.
    """
    form = ProductQuestionForm(request.POST)
    if form.is_valid():
        question = form.save(commit=False)
        slug = request.POST.get('slug')
        product = Product.active.get(slug=slug)
        question.user = request.user
        question.product = product
        question.save()

        from django.core.mail import EmailMessage
        to_email = request.user.email
        from_email = "sales@andrew-amanda.com"
        subject = "Your question about " + product.name + " has been received"
        message = product.meta_description + "($" + str(product.price) + "):\n\n\t\t" + question.question
        message += "\n\nThank you for your question. We will respond within 1 business day."
        message += "\n\nThe Entire Sales Team\nAndrew & Amanda Store"
        EmailMsg = EmailMessage(subject,message,from_email,[to_email],[from_email],headers={'Reply-To':from_email})
        EmailMsg.send()

        template = "catalog/question_success.html"
        html = render_to_string(template, {'request': request, 'question': question })
        response = simplejson.dumps({'success':'True', 'html': html})

    else:
        html = form.errors.as_ul()
        response = simplejson.dumps({'success':'False', 'html': html})
    return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def add_tag(request):
    """ AJAX view that takes a form POST containing variables for a new product tag;
    requires a valid product slug and comma-delimited tag list; returns a JSON response
    containing two variables: 'success', indicating the status of save operation, and 'tag',
    which contains rendered HTML of all product pages for updating the product page.
    """
    tags = request.POST.get('tag','')
    slug = request.POST.get('slug','')
    if len(tags) > 2:
        p = Product.active.get(slug=slug)
        html = u''
        template = "catalog/tag_link.html"
        for tag in tags.split():
            tag.strip(',')
            Tag.objects.add_tag(p,tag)
        for tag in p.tags:
            html += render_to_string(template, {'tag': tag })
        response = simplejson.dumps({'success':'True', 'html': html })
    else:
        response = simplejson.dumps({'success':'False'})
    return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')
