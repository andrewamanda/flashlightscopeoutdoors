from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.process_order import views as myviews
#Urls which need to be loaded at root level.
urlpatterns = [
    url(r'^satchmo/print/(?P<doc>[-\w]+)/(?P<id>[-\w]+)',
        myviews.displayDoc, {},
        'satchmo_print_shipping'),
    url(r'^orders/$', myviews.all_orders,
	  {'template_name': 'process_order/all_orders.html'}, 'all_orders'),
    url(r'^process_orders_by_shipstation/$', myviews.process_orders_by_shipstation,
	  {'template_name': 'process_order/shipstation_orders.xml', 'SSL': settings.ENABLE_SSL}, 'process_orders_by_shipstation'),
    url(r'^process_orders_by_shipstation_4jet/$', myviews.process_orders_by_shipstation_4jet,
	  {'template_name': 'process_order/shipstation_orders_4jet.xml', 'SSL': settings.ENABLE_SSL}, 'process_orders_by_shipstation_4jet'),
    url(r'^process_orders_by_shipworks', myviews.process_orders_by_shipworks,
	  {'template_name': 'process_order/shipstation_orders.xml', 'SSL': settings.ENABLE_SSL}, 'process_orders_by_shipworks'),

]
