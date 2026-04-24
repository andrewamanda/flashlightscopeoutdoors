from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.nameyourprice import views as myviews

urlpatterns = [
	url(r'^makeoffer_ssl/$', myviews.Bidding,
	 	{'template_name': 'nameyourprice/nameyourprice.html', 'SSL': settings.ENABLE_SSL}, 'nameyourprice'),
	url(r'^makeoffer/$', myviews.Bidding,
	 	{'template_name': 'nameyourprice/nameyourprice.html', 'SSL': settings.ENABLE_SSL}, 'nameyourprice'),
	url(r'^getselleroffers/$', myviews.SellerOffers,
	 	{'template_name': 'nameyourprice/nameyourprice.html', 'SSL': settings.ENABLE_SSL}, 'selleroffers'),
	url(r'^buyermakeoffer/$', myviews.BuyerOffers,
	 	{'template_name': 'nameyourprice/success_buyeroffer_made.html', 'SSL': settings.ENABLE_SSL}, 'buyeroffers'),
	url(r'^viewyouroffers/$', myviews.ViewOffers,
	 	{'template_name': 'nameyourprice/view_offers.html', 'SSL': settings.ENABLE_SSL}, 'viewoffers'),
	url(r'^cancelyouroffer/$', myviews.CancelOffer,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'canceloffer'),
	url(r'^declineyouroffer/$', myviews.DeclineOffer,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'declineoffer'),
	url(r'^buyercounteryouroffer/$', myviews.BuyerCounterOffer,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'buyercounteroffer'),
	url(r'^acceptoffer/$', myviews.BuyerAcceptOffer,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'buyeracceptoffer'),
	url(r'^checkoutauction/$', myviews.CheckOutAuction,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'checkoutauction'),
	url(r'^buyitnow/$', myviews.BuyItNow,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'BuyItNow'),
	url(r'^pollyouroffer/$', myviews.PollYourOffer,
	 	{'template_name': 'nameyourprice/View_offers.html', 'SSL': settings.ENABLE_SSL}, 'PollYourOffer'),
	url(r'^viewyouroffer/$', myviews.ViewYourOffers,
	 	{'template_name': 'nameyourprice/all_offers.html', 'SSL': settings.ENABLE_SSL}, 'ViewYourOffers'),
	url(r'^getofferhistory/$', myviews.ViewOfferHistory,
	 	{'template_name': 'nameyourprice/all_offers.html', 'SSL': settings.ENABLE_SSL}, 'ViewOfferHistory'),




]
