from django.urls import re_path as url, include
from django.conf import settings
from ecomstore.newsletter.views import newsletter, iscrivi, disiscrivi
#from ecomstore.newsletter.views import newsletter

urlpatterns = [
        url(r'^$', newsletter, {'template_name': 'newsletter/newsletter.html'}),
        url(r'^iscrivi/$', iscrivi),
        url(r'^disiscrivi/$', disiscrivi),
]
