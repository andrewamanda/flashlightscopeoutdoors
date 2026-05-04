from django.urls import re_path as url, include
from ecomstore import settings
from django.contrib import admin
from django.contrib.sites.models import Site
from ecomstore.checkout import views as myviews
from django.urls import path

admin.autodiscover()

site = Site.objects.get_current()

urlpatterns = [
    url(r'^$', myviews.show_checkout, {'template_name': 'checkout/checkout.html', 'SSL': settings.ENABLE_SSL }, 'checkout'),
    url(r'^receipt/$', myviews.receipt, {'template_name': 'checkout/receipt.html', 'SSL': settings.ENABLE_SSL },'checkout_receipt'),
    url(r'^receipt_mobile/$', myviews.receipt, {'template_name': 'checkout/receipt.html'},'checkout_receipt_mobile'),
    url(r'^checkout_begin/$', myviews.checkout_begin, {'template_name': 'checkout/addresses.html', 'SSL': settings.ENABLE_SSL }, 'beginCheckout'),
    url(r'^checkout_shipping_method/$', myviews.checkout_shipping_method, {'template_name': 'checkout/shipping_method.html', 'SSL': settings.ENABLE_SSL }, 'shipping_method'),
    url(r'^checkout_payment/$', myviews.checkout_payment, {'template_name': 'checkout/payment.html',
                                                  'SSL': settings.ENABLE_SSL,
                                                  'return_url': 'http://' + site.domain + '/checkout/paypal/docheckout/',
                                                  'cancel_url': 'http://' + site.domain + '/checkout/checkout_payment/',
                                                  'error_url': 'http://' + site.domain + '/checkout/paypal/error/'}, 'payment'),

    url(r'^paypal/success/$', myviews.paypal_success_page, {}, 'base-success'),
    url(r'^paypal/cancel/$', myviews.paypal_cancel_page, {}, 'base-cancel'),
    url(r'^paypal/error/$', myviews.paypal_error_page, {},'base-error'),

    url(r'^create-payment-intent', myviews.createpayment, {'SSL': settings.ENABLE_SSL},name="create-payment-intent"),
    url(r'^payment-complete', myviews.paymentcomplete, {'SSL': settings.ENABLE_SSL}, 'payment-complete'),

    url(r'^makeapayment', myviews.makeapayment, {'SSL': settings.ENABLE_SSL}, 'makeapayment'),
    url(r'^makeapaymentcomplete', myviews.makeapaymentcomplete, {'SSL': settings.ENABLE_SSL}, 'makeapayment-complete'),
]

from ecomstore.paypal_driver import views as paypalviews
urlpatterns += [
    url(r'^setcheckout/$', paypalviews.setcheckout,
        {'template': 'checkout/paypal/setcheckout.html',
         'return_url': 'http://' + site.domain + '/checkout/paypal/docheckout/',
         'cancel_url': 'http://' + site.domain + '/checkout/paypal/cancel',
         'error_url': 'http://' + site.domain + '/checkout/paypal/error/'}, 'paypal-setcheckout'),
    url(r'^paypal/docheckout/$', paypalviews.docheckout,
        {'success_url': "/checkout/paypal/success/",
         'error_url': '/checkout/paypal/error/', 
         }, 'paypal-docheckout'),

]
