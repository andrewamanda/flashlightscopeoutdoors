from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from ecomstore.settings import CURRENT_PATH
from ecomstore.catalog.models import Product
from ecomstore.marketing.models import * 
from ecomstore.marketing.forms import * 
from django.db.models import Q
import json

import os
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

ROBOTS_PATH = os.path.join(CURRENT_PATH, 'marketing/robots.txt')

def robots(request):
    """ view for robots.txt file """
    return HttpResponse(open(ROBOTS_PATH).read(), 'text/plain')

def google_base(request):
    """ view for Google Base Product feed template; returns XML response """
    products = Product.active.all()
    template = get_template("marketing/google_base.xml")
    xml = template.render(Context(locals()))
    return HttpResponse(xml, mimetype="text/xml")

@login_required
def GroupBuy(request, template_name="marketing/group_buy.html"):
    try:
        p = GroupBuyProduct.objects.get(status = 'OPEN')
    except:
        p = None
    already_participated = False 
    if request.user.is_authenticated:
        try:
            i = GroupBuyParticipant.objects.get(user=request.user, p = p)
            groupbuy_form = GroupBuyForm(instance = i)
            already_participated = True
        except:
             groupbuy_form = GroupBuyForm()
             already_participated = False 
    else:
        groupbuy_form = GroupBuyForm()
    if request.method == "GET":
        if request.GET.get("load_participants"):
              try:
                  qs = GroupBuyParticipant.objects.filter(Q(p_id__exact=p.id))
              except:
                  qs = []
              dicts = [ obj.as_dict() for obj in qs ]
              return HttpResponse(json.dumps({"data": dicts}), content_type='application/json')
    else:
        action = request.POST.get("action")
        if action == None:
              exist_users = GroupBuyParticipant.objects.filter(user=request.user, p = p)
              if len(exist_users) > 0:
                    return HttpResponse(json.dumps({"success": "False", "username":request.user.username}), content_type='application/json')
              
              eventRecord = GroupBuyParticipant()
              eventRecord.p = p
              eventRecord.user = request.user
              eventRecord.name = request.POST.get("name"," ")
              eventRecord.quantity = request.POST.get("quantity"," ")
              eventRecord.state = request.POST.get("state"," ")
              eventRecord.country = request.POST.get("country"," ")
              eventRecord.reason = request.POST.get("reason"," ")
              eventRecord.email = request.user.email
              eventRecord.save()
              return HttpResponse(json.dumps({"success": "True", "username":request.user.username, "date":str(eventRecord.last_updated),"id": eventRecord.id}), content_type='application/json')
        if action == "delete":
              id = i.id
              i.delete()
              return HttpResponse(json.dumps({"success": "True", "id":id}), content_type='application/json')

        if action == "get_status":
              return HttpResponse(json.dumps({"success": "True", "already_participated":already_participated}), content_type='application/json')


    return render(request, template_name, locals())
