from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect

from ecomstore.checkout.models import Order, OrderItem, GiftCertificate
from ecomstore.accounts.forms import UserProfileForm, RegistrationForm, LoginForm
from ecomstore.accounts import profile
from ecomstore.catalog.models import Product, Category, Brand
from ecomstore.settings import PRODUCTS_PER_ROW

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from ecomstore.settings import CACHE_TIMEOUT
from django.core.cache import cache



from ecomstore.stats import stats
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_user(request):
    page_title = "Account Login"
    username = password = ''
    form = LoginForm(request.POST or None)
    if request.POST:
        username = request.POST.get('username', 'Guest')
        password = request.POST.get('password', "None")
        url = request.POST.get('next')
        if url == '' or url == "None":
            url = "/"
            if request.flavour == 'mobile':
                url = reverse('my_account')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(url)
    #form = AuthenticationForm
    template_name = 'registration/login.html'
    next = request.GET.get("next")
    if request.flavour == 'mobile':
         template_name = 'mobile/home/login.html'

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

def register(request, template_name="registration/register.html"):
    """ view displaying customer registration form """

    page_title = "Account Registration"
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RegistrationForm(postdata)
        if form.is_valid():
            #form.save()
            user = form.save(commit=False)  # new
            user.email = postdata.get('email','')  # new
            user.save()  # new
            un = postdata.get('username','')
            pw = postdata.get('password1','')
            from django.contrib.auth import login, authenticate
            new_user = authenticate(username=un, password=pw)
            if new_user and new_user.is_active:
                login(request, new_user)
                url = reverse('my_account')
                return HttpResponseRedirect(url)
    else:
        form = RegistrationForm()
        if request.flavour == 'mobile':
            template_name = 'mobile/home/register.html'

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


    page_title = 'User Registration'

    return render(request, template_name, locals())

def reset_password(request):
    """ page displaying customer account information, past order list and account options """
    page_title = 'Password reset'
    name = request.user.username
    return render(request, template_name, locals())


@login_required
def my_account(request, template_name="registration/my_account.html"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)
    if request.flavour == 'mobile':
         template_name = 'mobile/home/profile.html'
         user_profile = profile.retrieve(request)

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

@login_required
def order_details(request, order_id, template_name="registration/order_details.html"):
    """ displays the details of a past customer order; order details can only be loaded by the same
    user to whom the order instance belongs.

    """

    l = order_id.find("-")
    if l == -1:
        o_id = order_id
    else:
        h = order_id.rfind("-")
        o_id = order_id[l+1:h]

    order = get_object_or_404(Order, invoice_number=order_id, user=request.user)
    page_title = 'Order Details for Order #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    return render(request, template_name, locals())

@login_required
def order_info(request, template_name="checkout/addresses.html"):
    """ page containing a form that allows a customer to edit their billing and shipping information that
    will be displayed in the order form next time they are logged in and go to check out """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserProfileForm(postdata)
        if form.is_valid():
            profile.set(request)
            url = reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = profile.retrieve(request)
        form = UserProfileForm(instance=user_profile)
    page_title = 'Update shipping and billing addresses'
    stage = 'account'
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)
    if request.flavour == 'mobile':
         template_name = 'mobile/home/addresses.html'

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

def gift_account(request, template_name="registration/gift_account.html"):

    if request.method == 'POST':
        postdata = request.POST.copy()
        email = postdata.get('email','')
        gift_code = postdata.get('cert_code','')

        if gift_code and email:
            try:
                giftcert = GiftCertificate.objects.get(to_email = email, code = gift_code)
                balance = giftcert.balance + giftcert.value_in_cart
                orders = giftcert.orders_redeemed
            except GiftCertificate.DoesNotExist:
                error_message = 'This is not a valid gift certificate code or the email is not valid. Please correct and reenter'
        else:
            error_message = 'This is not a valid gift certificate code or the email is not valid. Please correct and reenter'

    return render(request, template_name, locals())
