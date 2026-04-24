from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.facebookapp import views as myviews

urlpatterns = [
      url(r'^$',myviews.facebookapp, {'template_name': 'facebookapp/home.html', 'SSL': settings.ENABLE_SSL}, 'facebookapp'),
      url(r'^makeoffer/$',myviews.MakeOffer, {'template_name': 'facebookapp/MakeOffer.html', 'SSL': settings.ENABLE_SSL}, 'facebookmakeoffer'),
      url(r'^dealofday/$',myviews.DealOfDay, {'template_name': 'facebookapp/dealoftheday.html', 'SSL': settings.ENABLE_SSL}, 'fb_dealofday'),


]
