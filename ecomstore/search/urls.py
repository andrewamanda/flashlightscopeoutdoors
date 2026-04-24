from django.urls import re_path as url, include
from ecomstore.search.views import results
from ecomstore import settings

urlpatterns = [
    url(r'^results/$',results,{'template_name': 'search/results.html', 'SSL': settings.ENABLE_SSL}, 'search_results'),
]
