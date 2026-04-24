from django.urls import re_path as url, include
from ecomstore.billing import views

urlpatterns = [
    url(r'^add_card/$', views.add_card),
]
