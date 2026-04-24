from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.mobile import views as myviews

urlpatterns = [
	url(r'^productautocomplete/$', myviews.getProductAutoComplete,
	 	{}, 'productautocomplete'),
	url(r'^productautocomplete_ssl/$', myviews.getProductAutoComplete,
	 	{'SSL': settings.ENABLE_SSL}, 'productautocomplete_ssl'),
	url(r'^add2cart/$', myviews.add2Cart, {'SSL': settings.ENABLE_SSL}, 'add2cart'),
	url(r'^getcartsize/$', myviews.getCartCount, {}, 'getCartCount'),
	url(r'^getcartsize_ssl/$', myviews.getCartCount, {'SSL': settings.ENABLE_SSL}, 'getCartCount_ssl'),
	url(r'^messageoftheday_m/$', myviews.messageoftheday, {}, 'messageoftheday_mobile'),
	url(r'^email_signup/$', myviews.email_signup, {}, 'm_email_signup'),
	#(r'^switch_flavour/$', 'switch_flavour', {}, 'switch_flavour'),


]
