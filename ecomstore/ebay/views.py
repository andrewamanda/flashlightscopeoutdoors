from django.contrib.auth.models import User
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from ecomstore.stats import stats
from ecomstore.catalog.models import Product
from ecomstore.settings import PRODUCTS_PER_ROW
from ecomstore.ebay.models import EBayListing



# Create your views here.
def myebay(request, template_name="ebay/query.html"):
    pass



def auction(request, template_name="ebay/auction.html"):
    """ page displaying the Aimkon auction items on ebay """
    page_title = 'Aimkon Auction!'
    name = request.user.username
    featured = Product.featured.all()[0:PRODUCTS_PER_ROW]
    recently_viewed = stats.get_recently_viewed(request)
    return render(request, template_name, locals(), context_instance=RequestContext(request))

def listing(request, template_name="ebay/listing.html"):
    """ page displaying the Aimkon auction items on ebay """
    page_title = 'Aimkon Auction!'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

