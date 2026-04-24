from django.conf.urls import url, include
from ecomstore import settings
from ecomstore.blog import views as myviews

urlpatterns = [
	url(r'^', myviews.blog,
	 	{'template_name': 'blog/blog.html'}, 'blog'),

]
