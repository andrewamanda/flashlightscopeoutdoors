from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from ecomstore.cart import cart
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import user_passes_test


from ecomstore.dealers.models import DealerApplication, DealerDiscountRate
from ecomstore.dealers.forms import DealerOrderForm

from ecomstore.utils.captcha import createCaptcha, verifyCaptcha

from ecomstore.settings import DISTRIBUTOR_NAME

def dealer_enroll(request, template_name="for_dealers/dealer_enroll.html"):
    """ page displaying the Aimkon return policy """
    page_title = DISTRIBUTOR_NAME + ' Dealer Enrollment'

    if request.method == 'POST':

        if (verifyCaptcha(request.POST.get('imghash'),request.POST.get('imgtext')) == False):
           captcha_error = 'Error on captcha. Please type again.'
           captcha = createCaptcha(request)
           imgpath = captcha['imgpath']
           imghash = captcha['imghash']
           return render_to_response(request, template_name, locals())

        dealerApplication = DealerApplication();
        dealerApplication.business_name = request.POST.get('business_name', '')
        dealerApplication.location = request.POST.get('location', '')
        dealerApplication.contact = request.POST.get('contact', '')
        dealerApplication.email = request.POST.get('email', '')
        dealerApplication.phone = request.POST.get('phone', '')
        dealerApplication.message = request.POST.get('message', '')
        dealerApplication.website = request.POST.get('website', '')


        dealerApplication.save()

        template_name = "for_dealers/dealer_enroll_response.html"
        return render(request, template_name, locals(), context_instance=RequestContext(request))

    name = request.user.username

    captcha_error = "Type the characters you see in the image for security purposes"
    captcha = createCaptcha(request)
    imgpath = captcha['imgpath']
    imghash = captcha['imghash']

    return render(request, template_name, locals())


def dealer_pricing(request, template_name="for_dealers/dealer_pricing.html"):
    """ page displaying the Aimkon return policy """
    page_title = DISTRIBUTOR_NAME + ' Dealer Pricing'

    dealerdiscountrate = DealerDiscountRate.objects.all()

    return render(request, template_name, locals())
dealer_pricing = user_passes_test(lambda u: u.is_authenticated() and u.has_perm("dealers.change_dealerdiscountrate"), login_url='/accounts/login/')(dealer_pricing)


def how_to_order(request, template_name="for_dealers/how_to_order.html"):
    """ page displaying the Aimkon return policy """
    page_title = 'Olight Gear How To Order'

    if request.method == "POST":
        new_data = request.POST.copy()
        form = DealerOrderForm(new_data)
        if form.is_valid():
            form.save(request)
            url = reverse('order_response')
            return HttpResponseRedirect(url)
    else:
       form = DealerOrderForm()

    return render(request, template_name, locals())

how_to_order = user_passes_test(lambda u: u.is_authenticated() and u.has_perm("dealers.add_dealerorder"), login_url='/accounts/login/')(how_to_order)

def order_response(request, template_name="for_dealers/order_response.html"):
    """ page displaying the Aimkon return policy """
    page_title = DISTRIBUTOR_NAME + ' How To Order'


    return render(request, template_name, locals())

def dealer_locator(request, template_name="for_dealers/dealer_locator.html"):
    """ page displaying the Aimkon return policy """
    page_title = DISTRIBUTOR_NAME + ' Dealer Locator'


    return render(request, template_name, locals())

def company(request, template_name="for_dealers/company.html"):
    """ page displaying the Aimkon return policy """
    page_title = DISTRIBUTOR_NAME + ' Company'


    return render(request, template_name, locals())



def dealer_cart(request, template_name="for_dealers/cart.html"):
    """ page displaying the Aimkon return policy """
    page_title = DISTRIBUTOR_NAME + ' How To Order'
    if request.method == 'POST':
        postdata = request.POST.copy()
        if postdata['submit'] == 'Remove':
            cart.remove_from_cart(request)
        if postdata['submit'] == 'Update':
            cart.update_cart(request)
        if postdata['submit'] == 'Checkout':
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
        if postdata['submit'] == 'beginCheckout':
            checkout_url = checkout.get_checkout_url(request)
            return HttpResponseRedirect(checkout_url)
    cart_items = cart.get_cart_items(request)
    page_title = 'Shopping Cart'
    cart_subtotal = cart.cart_subtotal(request)


    return render(request, template_name, locals())
