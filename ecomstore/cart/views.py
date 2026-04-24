from django.shortcuts import render, get_object_or_404
from ecomstore.cart import cart
from django.template import RequestContext

from django.http import HttpResponseRedirect
from ecomstore.checkout import checkout
from ecomstore import settings
from ecomstore.stats import stats
from ecomstore.catalog.models import Product, Category, Brand
from ecomstore.settings import PRODUCTS_PER_ROW, CACHE_TIMEOUT, SITE_VERSION

from django.contrib.auth.decorators import login_required
from ecomstore.cart.models import WishList

from ecomstore.cart import cart
from django.core.cache import cache
from ecomstore.cart.models import CartItem

from django.contrib import messages
import logging
logger = logging.getLogger(__name__)

def show_cart(request, template_name="cart/cart.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    if SITE_VERSION == "NEW_SKIN":
        template_name = "2023/cart/cart.html"

    if request.method == 'POST':
        try:
            postdata = request.POST.copy()
            submit = postdata.get('submit')

            if submit == 'Remove':
                cart.remove_from_cart(request)
                messages.success(request, "Item removed.")
            elif submit == 'Update':
                cart.update_cart(request)
                messages.success(request, "Quantity updated.")
            elif submit == 'Checkout':
                checkout_url = checkout.get_checkout_url(request)
                return HttpResponseRedirect(checkout_url)
            elif submit == 'beginCheckout':
                checkout_url = checkout.get_checkout_url(request)
                return HttpResponseRedirect(checkout_url)
            else:
                # Unknown or missing action
                messages.warning(request, "We couldn’t process your request. Please try again.")
                logger.warning("Unknown submit action: %r; keys=%s", submit, list(postdata.keys()))

        except Exception as e:
            logger.exception("Error processing cart POST: %s", e)
            msg = str(e).splitlines()[0] if str(e) else "Something went wrong."
            messages.error(request, f"Error: {msg}")

    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = cart.cart_subtotal(request)
    # need for Google Checkout button
    merchant_id = settings.GOOGLE_CHECKOUT_MERCHANT_ID
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    if request.flavour == 'mobile':
         template_name = 'mobile/home/showcart.html'


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

def recover_cart(request, template_name="cart/cart.html"):
    from ecomstore.cart import CART_ID_SESSION_KEY
    email = request.GET.get("email")
    cis = CartItem.objects.filter(email=email)
    cart_id = None
    for c in cis:
        cart_id = c.cart_id
        break
    request.session[CART_ID_SESSION_KEY] = cart_id
    return HttpResponseRedirect("/cart/")

@login_required
def add2wishlist(request, template_name="cart/wishlist.html"):
    try:
       wishlist = WishList.objects.get(user=request.user)
    except WishList.DoesNotExist:
       wishlist = WishList(user=request.user)
       wishlist.save()
       wishlist = WishList.objects.get(user=request.user)

    if request.method == "GET":
       product_slug = request.session.get('product_slug', '')
       if product_slug:
          p = get_object_or_404(Product, slug=product_slug)
          #wishlist.products.add(p)
       wishlists = wishlist.products.all()
       return render(request, template_name, locals())


    postdata = request.POST.copy()
    product_slug = postdata.get('product_slug', '')
    action = ''
    if not product_slug:
       product_slug = request.session.get('product_slug', '')
       action = 'add2wishlist'


    p = get_object_or_404(Product, slug=product_slug)

    if not action:
       action = postdata.get('action', '')
    if action == 'add2wishlist':
       wishlist.products.add(p)
    else:
       cart.add_to_cart(request)
       wishlist.products.remove(p)

    wishlists = wishlist.products.all()

    return render(request, template_name, locals())
