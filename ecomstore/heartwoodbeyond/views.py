from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

from django.http import HttpResponseRedirect
from ecomstore.heartwoodbeyond.models import *
from ecomstore import settings

from django.contrib.auth.decorators import login_required

from django.core.cache import cache
from ecomstore.utils.strops import normalize_str
from django.contrib.auth.models import User
from ecomstore.misc.models import Testimonial
from django.template.loader import render_to_string
import json as simplejson
from django.http import HttpResponseRedirect, HttpResponse
from ecomstore.utils.captcha import createCaptcha, verifyCaptcha
from ecomstore.newsletter.models import EmailSubscription, EmailSubscription_Excluded
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME





def about(request, template_name="heartwoodandbeyond/about.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    if request.method == 'POST':
        postdata = request.POST.copy()
        recaptcha_response = request.POST.get('g-recaptcha-response')
        print ("recaptcha_resonse = %".format(recaptcha_response))


    return render(request, template_name, locals())

def why(request, template_name="heartwoodandbeyond/faq/faq.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())


def grade(request, template_name="heartwoodandbeyond/our-heartpine-grades.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())




def gallery(request, template_name="heartwoodandbeyond/gallery_new.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())


def heartpine_products(request, template_name="heartwoodandbeyond/heartpine-products.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def free_quote(request, template_name="heartwoodandbeyond/free_quote.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'
    print("***** get free quote****")
    captcha_error = "Type the characters you see in the image for security purposes"
    captcha = createCaptcha(request)
    imgpath = captcha['imgpath']
    imghash = captcha['imghash']

    return render(request, template_name, locals())

def leave_review(request, template_name="heartwoodandbeyond/faq/leave-review.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def shipping(request, template_name="heartwoodandbeyond/faq/shipping.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def contact(request, template_name="heartwoodandbeyond/faq/contact.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'
    print("**** in Contact")
    if request.method == 'POST':
        print("**** in contact POST")
        if (verifyCaptcha(request.POST.get('imghash'),request.POST.get('imgtext')) == False):
           captcha_error = 'Error on captcha. Please type again.'
           captcha = createCaptcha(request)
           imgpath = captcha['imgpath']
           imghash = captcha['imghash']
           return render(request, template_name, locals())

    captcha_error = "Type the characters you see in the image for security purposes"
    captcha = createCaptcha(request)
    imgpath = captcha['imgpath']
    imghash = captcha['imghash']

    return render(request, template_name, locals())

def tobacco_pine_rustic(request, template_name="heartwoodandbeyond/tobacco-pine-rustic.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def installation_tips(request, template_name="heartwoodandbeyond/why_heartpine/installation-tips.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def post_installation(request, template_name="heartwoodandbeyond/faq/post_installation.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def reclaiming_process(request, template_name="heartwoodandbeyond/why_heartpine/reclaiming-process.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def our_heartpine_grades(request, template_name="heartwoodandbeyond/our-heartpine-grades.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())


def select_1_heartpine(request, template_name="heartwoodandbeyond/grades/select-1-heartpine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def select_1_heartpine_0(request, template_name="heartwoodandbeyond/grades/select-1-heartpine-0.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())




def antique_quartersawn(request, template_name="heartwoodandbeyond/grades/antique-quarterswan-heartpine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def natural_antique_heartpine(request, template_name="heartwoodandbeyond/grades/natural-antique-heartpine.html.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def character_heartpine(request, template_name="heartwoodandbeyond/grades/character-heartpine.html.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def antique_southern_yellow_pine(request, template_name="heartwoodandbeyond/grades/antique-southern-yellow-pine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def american_tobacco_co_reclaimed_tobacco_pine(request, template_name="heartwoodandbeyond/grades/american-tobacco-co-reclaimed-tobacco-pine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def oak(request, template_name="heartwoodandbeyond/grades/oak.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def finest_heart_pine_floors(request, template_name="heartwoodandbeyond/finest-heart-pine-floors-moncure-nc.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def why_reclaiming_process(request, template_name="heartwoodandbeyond/faq/reclaiming-process.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def gallery_quartersawn_heartpine(request, template_name="heartwoodandbeyond/gallery/quartersawn-heartpine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def gallery_additional_products(request, template_name="heartwoodandbeyond/gallery/additional-products.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def gallery_tobacco_pine_rustic(request, template_name="heartwoodandbeyond/gallery/tobacco-pine-rustic.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def gallery_natural_antique_heartpine(request, template_name="heartwoodandbeyond/gallery/natural-antique-heartpine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def gallery_character_heartpine(request, template_name="heartwoodandbeyond/gallery/character-heartpine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def gallery_antique_southern_yellow_pine(request, template_name="heartwoodandbeyond/gallery/antique-southern-yellow-pine.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())

def message_center(request, template_name="heartwoodandbeyond/message_center.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    return render(request, template_name, locals())


from ecomstore.utils.reCaptcha import check_recaptcha
from django.shortcuts import render, redirect

SPAM_EMAILS = {"sandsplace","gmx","webpage","blog","mailbab","funny", "next4.ir",}


@check_recaptcha
def request4moreinfo(request, template_name="heartwoodandbeyond/responses/more_info.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    if request.method == 'POST':
        postdata = request.POST.copy()
        if request.recaptcha_is_valid:
            if (verifyCaptcha(request.POST.get('imghash'),request.POST.get('imgtext')) == False):
                captcha_error = 'Error on captcha. Please type again.'
                captcha = createCaptcha(request)
                imgpath = captcha['imgpath']
                imghash = captcha['imghash']
                print("**** Failed the verification")
                return redirect("free_quote")
            first_name = normalize_str(postdata.get('submitted[name][first_name]',''))
            last_name = normalize_str(postdata.get('submitted[name][last_name]',''))
            email = normalize_str(postdata.get('submitted[contact][email]',''))
            phone = normalize_str(postdata.get('submitted[contact][phone]',''))
            address = normalize_str(postdata.get('submitted[address]',''))
            city = normalize_str(postdata.get('submitted[locale][city]',''))
            state = normalize_str(postdata.get('submitted[locale][state]',''))
            current_customer = postdata.get('submitted[are_you_a_current_customer]','')
            comments = normalize_str(postdata.get('submitted[comments]',''))
            sign_up_for_our_monthly_newsletter = postdata.get('submitted[sign_up_for_our_monthly_newsletter]','')

            is_current_customer = True if current_customer == "option1" else False
            sign_up_for_newsletter = True if sign_up_for_our_monthly_newsletter == "option1" else False

            print ("first name/last name = ",first_name, last_name)
            print ("phone, email = ", phone, email)
            print ("city, state, current customer, comments = ", city, state, is_current_customer, comments)
            print ("sign for newsletter = ", sign_up_for_newsletter)

            for keyword in SPAM_EMAILS:
                if keyword in email or keyword in comments:
                    print ("Skip ....  first name/last name = ",first_name, last_name)
                    print ("Skip ....  phone, email = ", phone, email)
                    print ("Skip ....  city, state, current customer, comments = ", city, state, is_current_customer, comments)

                    return render(request, template_name, locals())

            try:
                crmObj = CustomerRelationship.objects.get(email = normalize_str(email))
                print ("find the existing customer entry")
            except CustomerRelationship.DoesNotExist:
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    print ("User does not exist, creating one")
                    user = User(username=email, email=email)
                    print ("A new user created")
                    user.save()

                crmObj = CustomerRelationship(user=user, first_name=first_name, last_name=last_name, email=email, phone=phone, address=address, city=city, state=state, is_current_customer=is_current_customer, sign_up_for_newsletter=sign_up_for_newsletter, comments=comments)
                crmObj.save()
                print ("create a new customer entry")
            messageEntry = CorrespondenceEntry(subject="A new message from a customer", customer_comment=comments, contact_entry=crmObj)
            messageEntry.save()

            """ Build and send email to hwp staffs """

            #from_email = "sales@heartwoodandbeyond.com"
            from_email = "coleen@heartwoodpine.com"
            coleen_email = "heartwoodandbeyond@gmail.com"
            coleen_email = from_email
            replyto_email = email
            recipient_list = []
            recipient_list.append(coleen_email)
            #recipient_list.append(from_email)

            curr_message = comments
            message = "Customer: {} {}\nEmail: {}\nPhone: {} ".format(first_name, last_name, email, phone)
            message += "\n\n\t{}".format(curr_message)

            subject = "A message from {} {}".format(first_name, last_name)

            print("***Sending email: " + message)

            #from django.core.mail import EmailMessage
            from ecomstore.utils.email import send_mail_with_attachment

            send_mail_with_attachment(subject, message, from_email, replyto_email, recipient_list, [])

            return render(request, template_name, locals())


    return redirect("free_quote")


@check_recaptcha
def request4sample(request, template_name="heartwoodandbeyond/responses/sample_request.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Shopping Cart'

    if request.method == 'POST':
        postdata = request.POST.copy()
        if request.recaptcha_is_valid:
            first_name = postdata.get('submitted[fieldset][first_name]','')
            last_name = postdata.get('submitted[fieldset][last_name]','')
            email = postdata.get('submitted[fieldset2][email]','')
            phone = postdata.get('submitted[fieldset2][phone]','')
            details = postdata.get('submitted[details]','')
            sign_up_for_our_monthly_newsletter = postdata.get('submitted[sign_up_for_our_monthly_newsletter]','')

            print ("first name/last name = {% %}".format(first_name, last_name))
            return render(request, template_name, locals())

    return render(request, template_name, locals())

@check_recaptcha
def testimonial(request, template_name="heartwoodandbeyond/responses/testimonial_response.html"):
    """ page displaying the Aimkon email signup """
    print ("testimonial")
    if request.method == 'POST':
        print ("post testimonial")
        if request.recaptcha_is_valid:
            print ("Cap va;id")
            testimonial = Testimonial();
            testimonial.name = request.POST.get('submitted[name][name]', '')
            testimonial.comment = request.POST.get('submitted[comments]', '')
            #testimonial.save()
        return render(request, template_name, locals())


    return render(request, template_name, locals())

from ecomstore.inventorymanagement.models import *
def heartpine_pricing(request, template_name="heartwoodandbeyond/heartpine_pricing.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Heartpine Pricing'
    floors = Product.objects.filter(finishing_type__name="finished").filter(usage_type__name="Floors").order_by('ordering')
    stairs = Product.objects.filter(finishing_type__name="finished").filter(usage_type__name="Stairs").order_by('ordering')
    panels = Product.objects.filter(finishing_type__name="finished").filter(usage_type__name="Paneling").order_by('ordering')
    registers = Product.objects.filter(finishing_type__name="finished").filter(usage_type__name="Registers").order_by('ordering')
    f_usagetype = UsageType.objects.get(name='Floors')
    s_usagetype = UsageType.objects.get(name='Stairs')
    p_usagetype = UsageType.objects.get(name='Paneling')
    r_usagetype = UsageType.objects.get(name='Registers')
    return render(request, template_name, locals())


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def heartpine_productdetails(request, template_name="nameyourprice/view_offers.html"):
        b_id = request.POST.get("b_id")
        bid = get_object_or_404(Product, id=b_id)

        template = "heartwoodandbeyond/tags/tag_productdetails.html"
        html = render_to_string(template, {'request': request, 'details': bid.description, 'lead_time': bid.lead_time})
        response = simplejson.dumps({'success':'True', 'html': html})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

def milling(request, template_name="heartwoodandbeyond/milling.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Custom Milling Service'

    return render(request, template_name, locals())

def our_products(request, template_name="heartwoodandbeyond/products/product-collections.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def product_floors(request, template_name="heartwoodandbeyond/products/floors.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def product_tabletops(request, template_name="heartwoodandbeyond/products/tabletops.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def product_panels(request, template_name="heartwoodandbeyond/product/panels.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def product_stairs(request, template_name="heartwoodandbeyond/product/stairs.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def product_beams(request, template_name="heartwoodandbeyond/products/beams.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def product_shoemouldings(request, template_name="heartwoodandbeyond/products/shoemouldings.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())

def wholesalelumber(request, template_name="heartwoodandbeyond/wholesalelumber/wholesale.html"):
    """ view function for the page displaying the customer shopping cart, and allows for the updating of quantities
    and removal product instances

    """
    page_title = 'Our Product Collections'

    return render(request, template_name, locals())


from django.http.response import HttpResponseNotFound, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
import json
from ecomstore.cart.cart import CART_ID_SESSION_KEY
# below are for Stripe integration



@csrf_exempt
def makeapayment(request, template_name='heartwoodandbeyond/faq/makeapayment_hpw.html'):
    """ make a standalone payment to Stripe """

    print ("in Make a Payment")
    page_title = 'Send a Payment'

    return render(request, template_name, locals())

@csrf_exempt
def iframe_makeapayment(request, template_name='tags/payment_stripe.html'):
    """ make a standalone payment to Stripe """

    print ("Make payment in iframe")
    page_title = 'Send a Payment'

    return render(request, template_name, locals())


def email_unsubscribe(request, template_name="heartwoodandbeyond/email_unsubscribe.html"):
    """ page displaying the Aimkon email signup """
    if request.method == 'POST':
        if (verifyCaptcha(request.POST.get('imghash'),request.POST.get('imgtext')) == False):
           captcha_error = 'Error on captcha. Please type again.'
           captcha = createCaptcha(request)
           imgpath = captcha['imgpath']
           imghash = captcha['imghash']
           return render(request, template_name, locals())

        template_name = 'heartwoodandbeyond/email_unsubscribe_response.html';
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


def show_blog(request, blog_slug, template_name="heartwoodandbeyond/faq/faq_template.html"):



    request.session['last_path'] = request.path
    request.session['current_store'] = blog_slug

    blog_cache_key = request.path
    b = cache.get(blog_cache_key)
    if not b:
        b = get_object_or_404(Reclaimed_Blog.active, slug=blog_slug)
        cache.set(blog_cache_key, b, CACHE_TIMEOUT)

    return render(request, template_name, locals())
