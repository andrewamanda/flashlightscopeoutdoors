from django.urls import re_path as url, include
from ecomstore.cart import views as myviews
from ecomstore import settings

urlpatterns = [
    url(r'^$', myviews.show_cart, {'template_name':'cart/cart.html', 'SSL': settings.ENABLE_SSL}, 'show_cart'),
    url(r'^add2wishlist/$', myviews.add2wishlist, {'template_name':'cart/wishlist.html', 'SSL': settings.ENABLE_SSL}, 'wishlist'),
    url(r'^recovery/$', myviews.recover_cart, {'template_name':'cart/cart.html', 'SSL': settings.ENABLE_SSL}, 'recover'),


]
