#from django.conf.urls.defaults import *
from django.urls import re_path as url
from django.conf.urls import include
from ecomstore import settings
from ajax_select import urls as ajax_select_urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
import os
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap, ProductSitemap, BrandSitemap, CategorySitemap, DepartmentSitemap, SubCategorySitemap, SeriesSitemap

sitemaps = {
    'static':StaticViewSitemap,
    'product':ProductSitemap,
    'brand':BrandSitemap,
    'series':SeriesSitemap,
    'category':CategorySitemap,
    'subcategory':SubCategorySitemap,
    'department':DepartmentSitemap,
}

urlpatterns = [
    # Example:
    # (r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
    url(r'^admin/lookups/', include(ajax_select_urls), {'SSL': settings.ENABLE_SSL}),
    url(r'^admin/', admin.site.urls, {'SSL': settings.ENABLE_SSL}),

    #(r'^admin_media/(?P<path>.*)$', 'django.views.static.serve',
    #             {'document_root': settings.ADMIN_MEDIAHOST_DIR}),
    url(r'^catalog/', include('ecomstore.catalog.urls')),
    url(r'^catalog-', include('ecomstore.catalog.urls')),

    url(r'^$', include('ecomstore.home.urls')),
    url(r'^2023/$', include('ecomstore.home.urls')),


    url(r'^cart/', include('ecomstore.cart.urls')),
    url(r'^checkout/', include('ecomstore.checkout.urls')),
    #url(r'^heartwoodbeyond/', include('ecomstore.heartwoodbeyond.urls')),
    url(r'^accounts/', include('ecomstore.accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    #url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('social_django.urls', namespace='social')),
    url(r'^search/', include('ecomstore.search.urls')),
    url(r'^billing/', include('ecomstore.billing.urls')),
    url(r'^ebay/', include('ecomstore.ebay.urls')),
    url(r'^wholesale/', include('ecomstore.wholesale.urls')),
    url(r'^misc/', include('ecomstore.misc.urls')),
    url(r'^newsletter/', include('ecomstore.newsletter.urls')),
    url(r'^$', include('ecomstore.marketing.urls')),
    #(r'^$','ecomstore.home.views.home', {'template_name': 'home/home.html'}, 'home'),
    #(r'^sentry/', include('sentry.urls')),
    #(r'^sentry/', include('sentry.web.urls')),
    #(r'^forum/', include('dinette.urls')),

    url(r'^process_order/', include('ecomstore.process_order.urls')),

    #(r'^accounts/', include('registration.backends.default.urls')),
    #(r'^facebook/', include('django_facebook.urls')),

    url(r'^dealers/', include('ecomstore.dealers.urls')),
    url(r'^nameyourprice/', include('ecomstore.nameyourprice.urls')),
    url(r'^marketing/', include('ecomstore.marketing.urls')),
    url(r'^facebookapp/', include('ecomstore.facebookapp.urls')),
    url(r'^functionaltests/', include('ecomstore.functionaltests.urls')),
    #(r'^dowser/', include('django_dowser.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^mobile/', include('ecomstore.mobile.urls')),
    #(r'helpdesk/', include('helpdesk.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps, 'SSL': settings.ENABLE_SSL}),
    url('^robots.txt$',include('robots.urls')),

    #reenable these lines if want blog
    #url(r'^weblog/', include('zinnia.urls')),
    #url(r'^comments/', include('django_comments.urls')),
    #url(r'^blog/', include('ecomstore.blog.urls')),

    url(r'^pages/', include('django.contrib.flatpages.urls')),


]

if not settings.PRODUCTION:
   from django.views.static import serve
   urlpatterns += [
      url(r'^static/(?P<path>.*)$', serve,
            { 'document_root' : os.path.join(settings.CURRENT_PATH, 'static') }),
]

handler404 = 'ecomstore.views.file_not_found_404'
handler500 = 'ecomstore.views.server_error_500'


from django.urls import path
from django.conf import settings

def test_500_email(request):
    if request.GET.get("key") != "Prevouscoffee610":
        raise Http404()
    raise Exception("Test production exception email")

urlpatterns += [
    path("test-500-email/", test_500_email),
]
