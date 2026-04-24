from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.ebay import views as myviews

urlpatterns = [
	url(r'^auction/$', myviews.auction,
	 	{'template_name': 'ebay/auction.html'}, 'auction'),
	url(r'^listing/$', myviews.listing,
	 	{'template_name': 'ebay/listing.html'}, 'listing'),

]
