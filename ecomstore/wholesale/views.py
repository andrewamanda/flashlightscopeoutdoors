from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404

from ecomstore.stats import stats
from ecomstore.settings import PRODUCTS_PER_ROW, NUM_OF_NEW_ARRIVALS, SITE_NAME
from ecomstore.catalog.models import Product



# Create your views here.
def wholesale(request, template_name="wholesale/wholesale.html"):
    """ page displaying the Aimkon Wholesale """
    page_title = SITE_NAME + ' Wholesale'
    name = request.user.username
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    #recently_viewed = stats.get_recently_viewed(request)

    return render(request, template_name, locals())

