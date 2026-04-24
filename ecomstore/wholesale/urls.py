from django.urls import re_path as url, include
from ecomstore import settings
from ecomstore.wholesale.views import wholesale

urlpatterns = [
	url(r'^wholesale/$', wholesale,
	 	{'template_name': 'wholesale/wholesale.html', 'SSL': settings.ENABLE_SSL}, 'wholesale'),
]
