from django.urls import re_path as url, include
from ecomstore.marketing.sitemaps import SITEMAPS
from ecomstore.marketing import views as myviews

urlpatterns = [
    url(r'^robots\.txt$', myviews.robots),
    url(r'^google_base\.xml$', myviews.google_base),
    url(r'^groupbuy/$', myviews.GroupBuy, {'template_name': 'marketing/group_buy.html'}, 'group_buy'),

]

from django.contrib.sitemaps.views import sitemap
urlpatterns += [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': SITEMAPS }),
]
