from django.urls import re_path as url, include
from ecomstore.catalog import views as myviews
from ecomstore import settings
from django.urls import path
from . import views

urlpatterns = [
    url(r'^catalog/$',myviews.index, {'template_name': 'catalog/index.html', 'SSL': settings.ENABLE_SSL}, 'catalog_home'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', myviews.show_category,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'catalog_category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', myviews.show_product,
       {'template_name': 'catalog/product.html', 'SSL': settings.ENABLE_SSL}, 'catalog_product'),

    url(r'^category-(?P<category_slug>[-\w]+)/$', myviews.show_category,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'category'),
    url(r'^product-(?P<product_slug>[-\w]+)/$', myviews.show_product,
       {'template_name': 'catalog/product.html', 'SSL': settings.ENABLE_SSL}, 'product'),
    url(r'^brand-(?P<brand_slug>[-\w]+)/$', myviews.show_brand,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'brand'),
    url(r'^brand-(?P<brand_slug>[-\w]+)/(?P<series_slug>[-\w]+)/$', myviews.show_series,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'series'),
    url(r'^category-(?P<category_slug>[-\w]+)/(?P<subcategory_slug>[-\w]+)/$', myviews.show_subcategory,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'subcategory'),




    url(r'^tag_cloud/$', myviews.tag_cloud,
       {'template_name': 'catalog/tag_cloud.html', 'SSL': settings.ENABLE_SSL}, 'tag_cloud'),
    url(r'^tag/(?P<tag>[-\w]+)/$', myviews.tag,
       {'template_name': 'catalog/tag.html', 'SSL': settings.ENABLE_SSL}, 'tag'),
    url(r'^review/product/add/$', myviews.add_review, {'SSL': settings.ENABLE_SSL}, 'add_product_review'),
    url(r'^question/product/add/$', myviews.add_question, { 'SSL': settings.ENABLE_SSL}, 'add_product_question'),
    url(r'^tag/product/add/$', myviews.add_tag),
    url(r'^brand/(?P<brand_slug>[-\w]+)/$', myviews.show_brand,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'brand_category'),
    url(r'^brand/(?P<brand_slug>[-\w]+)/(?P<series_slug>[-\w]+)/$', myviews.show_series,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'brand_series'),
    url(r'^category/(?P<category_slug>[-\w]+)/(?P<subcategory_slug>[-\w]+)/$', myviews.show_subcategory,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'category_subcategory'),

    url(r'^price/(?P<priceranges_slug>[-\w]+)/$', myviews.show_pricerange,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'price_ranges'),

    url(r'^brightness/(?P<brightnessranges_slug>[-\w]+)/$', myviews.show_brightnessrange,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'brightness_ranges'),

    url(r'^store/(?P<department_slug>[-\w]+)/$', myviews.show_store,
       {'template_name': 'catalog/store.html', 'SSL': settings.ENABLE_SSL}, 'store'),
    url(r'^all_departments/$', myviews.show_alldepartments,
       {'template_name': 'catalog/all_departments.html', 'SSL': settings.ENABLE_SSL}, 'alldepartments'),
    url(r'^all_brands/$', myviews.show_alldepartments,
       {'template_name': 'catalog/all_brands.html', 'SSL': settings.ENABLE_SSL}, 'allbrands'),
    url(r'^all_bundles/$', myviews.show_allbundles,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'allbundles'),


    url(r'^dealoftheday/$', myviews.show_deal,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'dealoftheday'),
    url(r'^clearance/$', myviews.show_clearance,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'clearance'),
    url(r'^promotion/$', myviews.show_promotion,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'promotion'),
    url(r'^newarrival/$', myviews.show_newarrival,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'newarrival'),
    url(r'^open_box/$', myviews.show_open_box,
       {'template_name': 'catalog/category.html', 'SSL': settings.ENABLE_SSL}, 'open_box'),
    url(r'^relatedproducts/$', myviews.show_related, {'SSL': settings.ENABLE_SSL}, 'related_products'),
    path('test-widget/', views.test_widget_view, name='test_widget'),
    path('test-template/', views.test_template_view, name='test_template'),
    path('test-upload/', views.test_image_upload, name='test_upload'),
]

from ecomstore.catalog import adminviews
urlpatterns += [
    url(r'^admin/inventory/edit/$',
        adminviews.edit_inventory, {}, 'satchmo_admin_edit_inventory'),
]
