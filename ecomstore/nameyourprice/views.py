from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.forms import ModelForm
from django import forms
from ecomstore.nameyourprice.models import NameYourPrice, ProductOffered, OfferHistory
from ecomstore.catalog.models import Product, Brand, Category, Department
from django.template.loader import render_to_string
#from django.utils import simplejson
import json as simplejson
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from ecomstore.cart import cart
from ecomstore.utils.getip import get_user_ip

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME

class BidForm(ModelForm):

    products=forms.ModelMultipleChoiceField(Product.objects.all(),
                  widget= FilteredSelectMultiple("Product",False,attrs={'rows':'10'}))
    class Meta:
        model= NameYourPrice
        fields = '__all__'

@login_required
def Bidding(request, template_name="nameyourprice/nameyourprice.html"):
    page_title = "Name your price, make an offer"
    bids = NameYourPrice.objects.filter(user=request.user)
    bid = None
    count = 0
    for b in bids:
        if b.status == 'WAIT4BUYER' or b.status == 'WAIT4SELLER' or b.status == 'BUYERACCEPTED' or b.status == 'SELLERACCEPTED':
            count += 1
            bid = b
    request.session['open_offer_count'] = count
    if bid:
        products = bid.productoffered_set.all()
        offerhistories = bid.offerhistory_set.all().order_by('-buyer_offer_date')
        buyitnow_price = 0
        for p in products:
            buyitnow_price += p.product.price * p.qty_offered

        template_name = "nameyourprice/view_offers.html"
        if request.flavour == 'mobile':
            list_cache_key = 'active_category_link_list'
            active_categories = cache.get(list_cache_key)
            if not active_categories:
                active_categories = Category.active.all().order_by('ranking')
                cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

            brand_cache_key = 'active_brand_link_list'
            active_brands = cache.get(brand_cache_key)
            if not active_brands:
                active_brands = Brand.active.all().order_by('ranking')
                cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)
            template_name = 'mobile/nameyourprice/view_offers.html'
        return render(request, template_name, locals())


    #form=BidForm()
    pSlug = request.GET.get('p','')
    if pSlug:
        product_interested = Product.objects.get(slug=pSlug)
        request.session['product_interested'] = product_interested.name

    if request.flavour == 'mobile':
         if pSlug and pSlug.strip():
             #product_interested = Product.objects.get(slug=pSlug)
             interested_qty = request.GET.get('qty','')
         list_cache_key = 'active_category_link_list'
         active_categories = cache.get(list_cache_key)
         if not active_categories:
                active_categories = Category.active.all().order_by('ranking')
                cache.set(list_cache_key, active_categories, CACHE_TIMEOUT)

         brand_cache_key = 'active_brand_link_list'
         active_brands = cache.get(brand_cache_key)
         if not active_brands:
                active_brands = Brand.active.all().order_by('ranking')
                cache.set(brand_cache_key, active_brands, CACHE_TIMEOUT)
         template_name = 'mobile/nameyourprice/nameyourprice.html'
         return render(request, template_name,locals())

    all_products_cache_key = 'all_products_'
    products = cache.get(all_products_cache_key)

    if not products :
        products = []
        departments = Department.active.filter(is_active=True).order_by('ranking')
        for d in departments:
             products_in_d = Product.objects.filter(is_active=True, brand__department__slug=d.slug).values('id','name').order_by('created_at').reverse()
             products += products_in_d
        #import sys
        #import cPickle
        #p_string = cPickle.dumps(products)
        #print "size of products", sys.getsizeof(p_string)
        cache.set(all_products_cache_key, products, CACHE_TIMEOUT)

    return render(request, template_name,locals())

def getDictArray(post, name):
    dic = {}
    for k in post.keys():
        if k.startswith(name):
            rest = k[len(name):]

            # split the string into different components
            parts = [p[:-1] for p in rest.split('[')][1:]
            id = int(parts[0])

            # add a new dictionary if it doesn't exist yet
            if id not in dic:
                dic[id] = {}

            # add the information to the dictionary
            dic[id][parts[1]] = post.get(k)
    return dic

def SellerOffers(request, template_name="nameyourprice/wish_list.html"):
        ids = request.POST.getlist("products[]")

        products = []
        subtotal = 0
        for pid in ids:
            product = Product.objects.get(id = pid)
            products.append(product)
            subtotal += product.sale_price

        #form=BidForm(request.POST)
        #form.save()
        template = "nameyourprice/wish_list.html"
        html = render_to_string(template, {'request': request, 'products': products, 'subtotal': subtotal })
        response = simplejson.dumps({'success':'True', 'html': html, 'selected': len(ids)})

        log_error(request, "Get Quote")

        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def BuyItNow(request, template_name="nameyourprice/success_buyeroffer_made.html"):

        products = getDictArray(request.POST, 'products_chosen')
        for key in products:
            product = Product.objects.get(id = products[key]['id'])
            qty = products[key]['qty']
            cart.add_buyitnow_to_cart(request, product, qty)

        log_error(request, "BuyItNow")
        response = simplejson.dumps({'success':'True'})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def BuyerOffers(request, template_name="nameyourprice/success_buyeroffer_made.html"):

        bid = None

        products = getDictArray(request.POST, 'products_chosen')
        for key in products:
            product = Product.objects.get(id = products[key]['id'])
            qty = products[key]['qty']
            message = products[key]['msg']
            buyerofferprice = products[key]['buyerofferprice']

            if bid == None:
                bid = NameYourPrice()
                bid.user = request.user
                bid.shipping_country = products[key]['shipping_country']
                bid.device = request.flavour
                bid.save()


            productoffered = ProductOffered()
            productoffered.bid = bid
            productoffered.product = product
            productoffered.qty_offered = qty
            productoffered.save()

        offerhistory = OfferHistory()
        offerhistory.bid = bid
        offerhistory.buyer_offer_date = datetime.datetime.now( )
        offerhistory.buyer_offer_price = buyerofferprice
        offerhistory.buyer_comment = message
        offerhistory.save()

        log_error(request, "Buy Offer")

        html = render_to_string(template_name, {'request': request, 'products': products, 'subtotal': buyerofferprice })
        response = simplejson.dumps({'success':'True', 'html': html})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def BuyerCounterOffer(request, template_name="nameyourprice/success_buyeroffer_made.html"):

        b_id = request.POST.get("b_id")
        bid = get_object_or_404(NameYourPrice, id=b_id)

        offerhistory = OfferHistory()
        offerhistory.bid = bid
        offerhistory.buyer_offer_date = datetime.datetime.now( )
        offerhistory.buyer_offer_price = request.POST.get('price')
        offerhistory.buyer_comment = request.POST.get('comment')
        offerhistory.save()

        log_error(request, "Buy Counter Offer")

        response = simplejson.dumps({'success':'True'})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')



@login_required
def ViewOffers(request, template_name="nameyourprice/view_offers.html"):
       bids = NameYourPrice.objects.filter(user=request.user)
       for b in bids:
          if bid.status == 'WAIT4BUYER' or bid.status == 'WAIT4SELLER':
             offerhistories = bid.offerhistory_set.all().order_by('-buyer_offer_date')


@login_required
def CancelOffer(request, template_name="nameyourprice/view_offers.html"):
      open_count = request.session['open_offer_count']
      b_id = request.POST.get("b_id")
      comment = request.POST.get("comment")
      bid = get_object_or_404(NameYourPrice, id=b_id)
      bid.reason = comment
      bid.status = "BUYERCANCELLED"
      bid.seller_to_accept = False
      open_count -= 1
      request.session['open_offer_count'] = open_count
      bid.save()

      log_error(request, "Cancel Offer")

      Cleanup_auction_session(request)
      response = simplejson.dumps({'success':'True', 'open_offer_count':open_count})
      return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def DeclineOffer(request, template_name="nameyourprice/view_offers.html"):
      open_count = request.session['open_offer_count']
      open_count -= 1
      request.session['open_offer_count'] = open_count
      b_id = request.POST.get("b_id")
      comment = request.POST.get("comment")
      bid = get_object_or_404(NameYourPrice, id=b_id)
      bid.reason = comment
      bid.status = "BUYERDECLINED"
      bid.save()
      log_error(request, "Decline Offer")
      response = simplejson.dumps({'success':'True', 'html': "success"})
      return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def BuyerAcceptOffer(request, template_name="nameyourprice/view_offers.html"):
      b_id = request.POST.get("b_id")
      comment = request.POST.get("comment")
      bid = get_object_or_404(NameYourPrice, id=b_id)
      bid.reason = comment
      bid.status = "BUYERACCEPTED"
      bid.save()

      offerhistories = bid.offerhistory_set.all().order_by('-buyer_offer_date')
      latest_seller_price = str(offerhistories[0].seller_offer_price)
      log_error(request, "Buyer Accept Offer")
      response = simplejson.dumps({'success':'True', 'accepted_price': latest_seller_price})
      return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def ViewYourOffers(request, template_name="nameyourprice/all_offers.html"):
    bids = NameYourPrice.objects.filter(user=request.user).order_by('-last_updated')

    log_error(request, "View Offers")

    return render(request, template_name,locals())


def ViewOfferHistory(request, template_name="nameyourprice/tag_offerhistory.html"):
        b_id = request.POST.get("b_id")
        bid = get_object_or_404(NameYourPrice, id=b_id)
        products = bid.productoffered_set.all()
        offerhistories = bid.offerhistory_set.all().order_by('-buyer_offer_date')

        log_error(request, "View Offer History")
        template = "nameyourprice/tag_offerhistory.html"
        html = render_to_string(template, {'request': request, 'products': products, 'offerhistories': offerhistories })
        response = simplejson.dumps({'success':'True', 'html': html})
        return HttpResponse(response,
                        content_type='application/javascript; charset=utf-8')

@login_required
def PollYourOffer(request, template_name="nameyourprice/view_offers.html"):
    return "BUYERACCEPTED"

@login_required
def CheckOutAuction(request, template_name="nameyourprice/view_offers.html"):
    bids = NameYourPrice.objects.filter(user=request.user)
    bid = None
    for b in bids:
        if b.status == 'BUYERACCEPTED' or b.status == 'SELLERACCEPTED':
            request.session['b_id'] = b.id
            bid = b
            break
    if bid:
        products = bid.productoffered_set.all()
        offerhistories = bid.offerhistory_set.all().order_by('-buyer_offer_date')

    cart.empty_cart(request)

    for p in products:
       p_slug = p.product.slug
       qty = p.qty_offered
       request.session['product_slug'] = p_slug
       request.session['quantity'] = qty
       cart.add_auction_to_cart(request)

    if bid.status == "BUYERACCEPTED":
       win_price = offerhistories[0].seller_offer_price
    else:
       win_price = offerhistories[0].buyer_offer_price

    request.session['win_price'] = str(win_price)

    from django.urls import reverse
    url = reverse('show_cart')
    url += "?bid_id=" + str(bid.id)
    return HttpResponseRedirect(url)

def Cleanup_auction_session(request):
    if 'product_slug' in request.session:
        del request.session['product_slug']
    if 'quantity' in request.session:
        del request.session['quantity']
    if 'win_price' in request.session:
        del request.session['win_price']

    if 'b_id' in request.session:
        del request.session['b_id']

    request.session['open_offer_count'] = 0

    cart.empty_cart(request)

def log_error(request, from_method):
    try:
        email = request.user.email
    except:
        email = "No email address"
    #print "{} from ip -- {} by {} {}".format(from_method, get_user_ip(request), request.user.username, email)
