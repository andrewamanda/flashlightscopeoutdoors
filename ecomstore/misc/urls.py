from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.misc import views as myviews

urlpatterns = [
	url(r'^store_policy/$', myviews.store_policy,
	 	{'template_name': 'misc/customer_service.html', 'SSL': settings.ENABLE_SSL}, 'store_policy'),
	url(r'^return_policy/$', myviews.return_policy,
	 	{'template_name': 'misc/returns.html', 'SSL': settings.ENABLE_SSL}, 'return_policy'),
	url(r'^product_warranty/$', myviews.product_warranty,
	 	{'template_name': 'misc/product_warranty.html', 'SSL': settings.ENABLE_SSL}, 'product_warranty'),
	url(r'^email_signup/$', myviews.email_signup,
	 	{'template_name': 'misc/email_signup.html', 'SSL': settings.ENABLE_SSL}, 'email_signup'),
	url(r'^email_unsubscribe/$', myviews.email_unsubscribe,
	 	{'template_name': 'misc/email_unsubscribe.html', 'SSL': settings.ENABLE_SSL}, 'email_unsubscribe'),

	url(r'^customer_service/$', myviews.customer_service,
	 	{'template_name': 'misc/customer_service.html', 'SSL': settings.ENABLE_SSL}, 'customer_service'),
	#(r'^promotion/$', 'promotion',
	# 	{'template_name': 'misc/promotion.html'}, 'promotion'),
	url(r'^aboutus/$', myviews.aboutus,
	 	{'template_name': 'misc/aboutus.html', 'SSL': settings.ENABLE_SSL}, 'aboutus'),
	url(r'^testimonial/$', myviews.testimonial_manage,
	 	{'template_name': 'misc/testimonial.html', 'SSL': settings.ENABLE_SSL}, 'testimonial'),
	url(r'^secure_shopping/$', myviews.secure_shopping,
	 	{'template_name': 'misc/secure_shopping.html', 'SSL': settings.ENABLE_SSL}, 'secure_shopping'),
	url(r'^savingschannel/$', myviews.savings_channel,
	 	{'template_name': 'misc/savings_channel.html', 'SSL': settings.ENABLE_SSL}, 'savings_channel'),
	url(r'^securelogin/$', myviews.secure_login,
	 	{'template_name': 'misc/secure_login.html', 'SSL': settings.ENABLE_SSL}, 'secure_login'),
	url(r'^freeshipping/$', myviews.free_shipping,
	 	{'template_name': 'misc/free_shipping.html', 'SSL': settings.ENABLE_SSL}, 'free_shipping'),
	url(r'^privacy/$', myviews.privacy,
	 	{'template_name': 'misc/privacy.html', 'SSL': settings.ENABLE_SSL}, 'privacy'),



	url(r'^dumpemails/$', myviews.dumpemails,
	 	{'template_name': 'misc/dumpemails.html'}, 'dumpemails'),
	url(r'^barcode/$', myviews.barcode),





]
