from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.functionaltests import views as myviews

urlpatterns = [
	url(r'^testbrowsertimeout/$', myviews.testbrowsertimeout,
	 	{'template_name': 'functionaltests/testbrowsertimeout.html'}, 'testbrowsertimeout'),
	url(r'^setbrowsertimeout/$', myviews.setbrowsertimeout,
	 	{'template_name': 'functionaltests/testbrowsertimeout.html'}, 'setbrowsertimeout'),
	url(r'^getbrowsertimeout/$', myviews.getbrowsertimeout,
	 	{'template_name': 'functionaltests/testbrowsertimeout.html'}, 'getbrowsertimeout'),




]
