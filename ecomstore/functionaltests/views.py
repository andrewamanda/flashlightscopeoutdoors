from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from ecomstore.nameyourprice.models import NameYourPrice, ProductOffered, OfferHistory
from ecomstore.catalog.models import Product
from django.template.loader import render_to_string
#from django.utils import simplejson
import json as simplejson
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from ecomstore.cart import cart
from ecomstore.utils.getip import get_user_ip

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME


from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def testbrowsertimeout(request, template_name):
     if request.method == 'POST':
        import time
        i = 0
        while i < timeout:
             #print "Count {} seconds".format(i)
             i += 1
             time.sleep(1)
        response = simplejson.dumps({'success':'True'})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

     return render(request,template_name, locals(), context_instance=RequestContext(request))

@csrf_exempt
def getbrowsertimeout(request, template_name):
        timeout = request.POST.get("time_out")
        #print timeout
        import time
        i = 0
        while i < int(timeout):
             #print "Count {} seconds".format(i)
             i += 1
             time.sleep(1)
        response = simplejson.dumps({'success':'True'})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@csrf_exempt
def setbrowsertimeout(request, template_name):
        timeout = request.POST.get("time_out")
        #print timeout
        import time
        i = 0
        while i < int(timeout):
             #print "Count {} seconds".format(i)
             i += 1
             time.sleep(1)
        response = simplejson.dumps({'success':'True'})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')



