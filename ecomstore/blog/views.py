from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render






def blog(request, template_name="blog/blog.html"):
    """ page displaying the Aimkon auction items on ebay """
    page_title = 'Blog!'
    return render(request, template_name, locals())


