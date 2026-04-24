from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from ecomstore.stats import stats
from ecomstore.newsletter.models import EmailSubscription, EmailSubscription_Excluded
from ecomstore.misc.models import Testimonial
from ecomstore.csvimport_app.models import emails_from_paypal
from ecomstore.checkout.models import Order
from ecomstore.catalog.models import Product, Category, Brand, DealOfTheDay
from ecomstore.settings import PRODUCTS_PER_ROW, SITE_NAME, EMAIL_ORDER

import datetime

from django.http import HttpResponseRedirect, HttpResponse
from ecomstore.utils.captcha import createCaptcha, verifyCaptcha
from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME






# Create your views here.
def return_policy(request, template_name="misc/return_ploicy.html"):
    """ page displaying the Aimkon return policy """
    page_title = ' Return Policy'
    name = request.user.username
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)
    return render(request, template_name, locals())

def store_policy(request, template_name="misc/store_ploicy.html"):
    """ page displaying the Aimkon return policy """
    page_title = ' Store Policy'
    if request.flavour == 'mobile':
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
         template_name = 'mobile/home/store_policy.html'

    return render(request, template_name, locals())

def product_warranty(request, template_name="misc/product_warranty.html"):
    """ page displaying the Aimkon shipping info """
    page_title = ' Product Warranty'
    name = request.user.username

    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    return render(request, template_name, locals())

def email_signup(request, template_name="misc/email_signup.html"):
    """ page displaying the Aimkon email signup """
    if request.method == 'POST':

        if (verifyCaptcha(request.POST.get('imghash'),request.POST.get('imgtext')) == False):
           captcha_error = 'Error on captcha. Please type again.'
           captcha = createCaptcha(request)
           imgpath = captcha['imgpath']
           imghash = captcha['imghash']
           return render(request, template_name, locals())

        template_name = 'misc/email_signup_response.html';
        email_subscription = EmailSubscription();
        email_subscription.name = request.POST.get('name', '')
        email_subscription.email = request.POST.get('email', '')
        email_subscription.interestedProducts = request.POST.get('InterestedProducts', '')
        email_subscription.save()
        request.session['email_registered'] = 'Your email has been registered'
        return HttpResponseRedirect("/")

    page_title = ' Email Signup'
    name = request.user.username

    captcha_error = "Type the characters you see in the image for security purposes"
    captcha = createCaptcha(request)
    imgpath = captcha['imgpath']
    imghash = captcha['imghash']

    return render(request, template_name, locals())

def email_unsubscribe(request, template_name="misc/email_unsubscribe.html"):
    """ page displaying the Aimkon email signup """
    if request.method == 'POST':
        template_name = 'misc/email_unsubscribe_response.html';
        unsubscribe_email = request.POST.get('email', '')
        #email_sub = get_object_or_404(EmailSubscription, email = unsubscribe_email)
        #email_sub.interestedProducts = 'unsubscribed'
        #email_sub.save()
        excluded = EmailSubscription_Excluded()
        excluded.why = 'User unsubscribed'
        excluded.email = unsubscribe_email
        excluded.save()
        return render(request, template_name, locals())

    page_title = ' Email Unsubscribe'
    name = request.user.username


    captcha_error = "Type the characters you see in the image for security purposes"
    captcha = createCaptcha(request)
    imgpath = captcha['imgpath']
    imghash = captcha['imghash']

    return render(request, template_name, locals())


def customer_service(request, template_name="misc/customer_service.html"):
    """ page displaying the Aimkon Customer Service """
    page_title = ' Customer Service'
    #featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    if request.flavour == 'mobile':
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
         template_name = 'mobile/home/customer_service.html'


    return render(request, template_name, locals())

def promotion(request, template_name="misc/promotion.html"):
    """ page displaying the Aimkon promotion """
    page_title = 'Promotion'
    return render(request, template_name, locals())

def secure_shopping(request, template_name="misc/secure_shopping.html"):
    """ page displaying the Aimkon promotion """
    page_title = ' Secure Shopping'
    return render(request, template_name, locals())

def savings_channel(request, template_name="misc/savings_channel.html"):
    """ page displaying the Aimkon promotion """
    page_title = ' Our Unbeatable Savings Channels'


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

    clearance = Product.objects.filter(clearance=True)

    return render(request, template_name, locals())

	
def secure_login(request, template_name="misc/secure_login.html"):
    """ page displaying the Aimkon promotion """
    page_title = ' Secure and Easy Login'
    return render(request, template_name, locals())

def free_shipping(request, template_name="misc/free_shipping.html"):
    """ page displaying the Aimkon promotion """
    page_title = ' Free Shipping on US domestic orders over $25'
    return render(request, template_name, locals())

def privacy(request, template_name="misc/privacy.html"):
    """ page displaying the Aimkon promotion """
    page_title = ' We value your privacy'
    return render(request, template_name, locals())

	
def aboutus(request, template_name="misc/aboutus.html"):
    """ page displaying the Aimkon aboutus """
    page_title = 'About ' + SITE_NAME 


    calendar_months = [ "jan", "feb", "mar", "apr", "may", "jun",
                    "jul", "aug", "sep", "oct", "nov", "dec" ]


    now = datetime.datetime.now( )
    month_name = calendar_months[ now.month-1 ]
    todays_file = month_name + "_" + ("%02d" % now.day)
    calendar_spec = "calendar_" + todays_file + ".jpg"

    if request.flavour == 'mobile':
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
         template_name = 'mobile/home/aboutus.html'

    return render(request, template_name, locals())


def dumpemails(request, template_name="misc/dumpemails.html"):
    """ page displaying the Aimkon aboutus """

    from  django.utils.encoding import iri_to_uri

    page_title = 'Welcome to ' + SITE_NAME + '!'

    excludes = []
    for e in EmailSubscription_Excluded.objects.all():
        excludes.append(e.email)

    users_emails = EMAIL_ORDER + ';'
    for e in User.objects.all().exclude(email__in=excludes):
        users_emails += iri_to_uri(e.email) + ';'

    newsletter_emails = EMAIL_ORDER + ';'
    for e in EmailSubscription.objects.all().exclude(email__in=excludes):
        newsletter_emails += iri_to_uri(e.email) + ';'

    orders_emails = EMAIL_ORDER + ';'
    for e in Order.objects.all().exclude(email__in=excludes):
        orders_emails += iri_to_uri(e.email) + ';'
		
    all_emails = EMAIL_ORDER + ';'
    for e in emails_from_paypal.objects.all().exclude(email__in=excludes):
        all_emails += iri_to_uri(e.email) + ';'


    return render(request, template_name, locals())


def testimonial_manage(request, template_name="misc/testimonial.html"):
    """ page displaying the Aimkon email signup """
    if request.method == 'POST':

        testimonials = Testimonial.objects.all()

        if (verifyCaptcha(request.POST.get('imghash'),request.POST.get('imgtext')) == False):
           captcha_error = 'Error on captcha. Please type again.'
           captcha = createCaptcha(request)
           imgpath = captcha['imgpath']
           imghash = captcha['imghash']
           return render(request, template_name, locals())


        testimonial = Testimonial();
        testimonial.name = request.POST.get('name', '')
        testimonial.comment = request.POST.get('comment', '')
        testimonial.save()
        return render(request, template_name, locals())

    page_title = SITE_NAME + ' Testimonial!'
    name = request.user.username
    testimonials = Testimonial.objects.all()

    captcha_error = "Type the characters you see in the image for security purposes"
    captcha = createCaptcha(request)
    imgpath = captcha['imgpath']
    imghash = captcha['imghash']

    return render(request, template_name, locals())

def barcode(request):
    #instantiate a drawing object
    import mybarcode
    d = mybarcode.MyBarcodeDrawing("HELLO WORLD")
    binaryStuff = d.asString('gif')
    return HttpResponse(binaryStuff, 'image/gif')






