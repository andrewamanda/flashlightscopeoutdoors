from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.home import views as myviews

urlpatterns = [
      # toggle the below two lines to switch between the HWP and AA
      #url(r'^$',myviews.hpwhome, {'template_name': 'heartwoodandbeyond/index.html', 'SSL': settings.ENABLE_SSL}, name='hpwhome'),
      url(r'^$',myviews.home, {'template_name': 'home/home.html', 'SSL': settings.ENABLE_SSL}, name='home'),

      #(r'^$','index', {'template_name': 'home/index.html'}, 'home'),
]
