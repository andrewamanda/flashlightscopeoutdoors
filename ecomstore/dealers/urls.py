from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.dealers import views as myviews

urlpatterns = [
	url(r'^dealer_enroll/$', myviews.dealer_enroll,
	 	{'template_name': 'for_dealers/dealer_enroll.html', 'SSL': settings.ENABLE_SSL}, 'dealer_enroll'),
	url(r'^dealer_pricing/$', myviews.dealer_pricing,
	 	{'template_name': 'for_dealers/dealer_pricing.html', 'SSL': settings.ENABLE_SSL}, 'dealer_pricing'),
	url(r'^how_to_order/$', myviews.how_to_order,
	 	{'template_name': 'for_dealers/how_to_order.html', 'SSL': settings.ENABLE_SSL}, 'how_to_order'),
	url(r'^dealer_cart/$', myviews.dealer_cart,
	 	{'template_name': 'for_dealers/cart.html', 'SSL': settings.ENABLE_SSL}, 'dealer_cart'),
	url(r'^order_response/$', myviews.order_response,
	 	{'template_name': 'for_dealers/order_response.html', 'SSL': settings.ENABLE_SSL}, 'order_response'),
	url(r'^dealer_locator/$', myviews.dealer_locator,
	 	{'template_name': 'for_dealers/dealer_locator.html', 'SSL': settings.ENABLE_SSL}, 'dealer_locator'),
	url(r'^company/$', myviews.company,
	 	{'template_name': 'for_dealers/company.html', 'SSL': settings.ENABLE_SSL}, 'company'),
]
