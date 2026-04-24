from decimal import Decimal, ROUND_UP
from ecomstore.cart.models import CartItem, CartItemOption
from ecomstore.catalog.models import Product
from ecomstore.catalog import deal_processor
from ecomstore import settings

from ecomstore.nameyourprice.util import is_auction

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.db.models import Max

from datetime import datetime, timedelta
import decimal
import random



CART_ID_SESSION_KEY = 'cart_id'

def _cart_id(request):
    """ get the current user's cart id, sets new one if blank;
    Note: the syntax below matches the text, but an alternative,
    clearer way of checking for a cart ID would be the following:

    if not CART_ID_SESSION_KEY in request.session:

    """
    if request.session.get(CART_ID_SESSION_KEY,'') == '':
        request.session[CART_ID_SESSION_KEY] = _generate_cart_id()
    return request.session[CART_ID_SESSION_KEY]

def _generate_cart_id():
    """ function for generating random cart ID values """
    cart_id = ''
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
    cart_id_length = 50
    for y in range(cart_id_length):
        cart_id += characters[random.randint(0, len(characters)-1)]
    return cart_id

def get_cart_items(request):
    """ return all items from the current user's cart """
    return CartItem.objects.filter(cart_id=_cart_id(request))

def add_buyitnow_to_cart(request, p, quantity):

    cart_products = get_cart_items(request)
    product_in_cart = False
    # check to see if item is already in cart

    for cart_item in cart_products:
        if cart_item.product.id == p.id:
            cart_item.augment_quantity(quantity)
            product_in_cart = True

    # create and save a new cart item
    if not product_in_cart:
        ci = CartItem()
        ci.product = p
        ci.quantity = quantity
        ci.cart_id = _cart_id(request)
        try:
            ci.email = request.user.email
        except:
            ci.email = None
        ci.save()

    p.quantity = p.quantity - int(quantity)
    p.save()

def add_auction_to_cart(request):
    product_slug = request.session.get('product_slug')
    quantity = request.session.get('quantity')

    p = get_object_or_404(Product, slug=product_slug)

    # create and save a new cart item
    ci = CartItem()
    ci.product = p
    ci.quantity = quantity
    ci.cart_id = _cart_id(request)
    try:
        ci.email = request.user.email
    except:
        ci.email = None

    ci.save()

    p.quantity = p.quantity - int(quantity)
    p.save()

def add_to_cart(request):
    """ function that takes a POST request and adds a product instance to the current customer's shopping cart """
    postdata = request.POST.copy()


    # get product slug from post data, return blank if empty
    product_slug = postdata.get('product_slug','')
    # get quantity added, return 1 if empty
    quantity = postdata.get('quantity',1)
    # fetch the product or return a missing page error
    p = get_object_or_404(Product, slug=product_slug)


    #get products in cart
    cart_products = get_cart_items(request)
    product_in_cart = False
    # check to see if item is already in cart

    for cart_item in cart_products:
        if p.slug == 'gift-certificate':
            break

        if cart_item.product.id == p.id:
            same_option = True
            cios = cart_item.cartitemoption_set.all()
            if cios:
                for cio in cios:
                    if cio.option != postdata.get(cio.title_normalize):
                         same_option = False
            else:
                more_choices = p.optionalchoices_set.all()
                for mc in more_choices:
                    if postdata.get(mc.title_normalize):
                        same_option = False

            # update the quantity if found
            if same_option:
                cart_item.augment_quantity(quantity)
                product_in_cart = True
            else:
                product_in_cart = False


    if not product_in_cart:
        # create and save a new cart item
        ci = CartItem()
        ci.product = p
        if isinstance(quantity, int):
            ci.quantity = quantity
        elif isinstance(quantity, float) and quantity.is_integer():
            ci.quantity = int(quantity)  # Convert float to integer if it's whole
        elif isinstance(quantity, str) and quantity.isdigit():
            ci.quantity = int(quantity)  # Convert numeric string to integer
        else:
            raise ValueError("Quantity must be an integer or a numeric equivalent.")



        ci.cart_id = _cart_id(request)
        try:
            ci.email = request.user.email
        except:
            ci.email = None

        ci.save()

        more_choices = p.optionalchoices_set.all()

        if more_choices:
            for c in more_choices:
                if not postdata.get(c.title_normalize):
                    break

                cio = CartItemOption()
                cio.title = c.title
                cio.option = postdata.get(c.title_normalize)
                ic = c.individualchoice_set.all()
                for i in ic:
                    if cio.option == i.description:
                         cio.price = i.additional_price
                         if i.quantity <= 0:
                             cio.availability = 'Soldout'
                         break
                cio.cartitem = ci
                if p.slug == 'gift-certificate':
                     lucky_email = postdata.get('lucky_email','')
                     cio.option += '--' + lucky_email
                     cio.gift_message = postdata.get('giftcert_message', '')
                     cio.lucky_email = postdata.get('lucky_email', '')
                     #print 'giftcert_message:' + postdata.get('giftcert_message', '')
                cio.save()
    try:
        p.quantity = p.quantity - int(quantity)
        p.save()
    except Exception as e:
        print(f"Error occurred: {e}")


def get_single_item(request, item_id):
    return get_object_or_404(CartItem, id=item_id, cart_id=_cart_id(request))

# update quantity for single item
def update_cart(request):
    """ function takes a POST request that updates the quantity for single product instance in the
    current customer's shopping cart

    """
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    quantity = postdata['quantity']
    if not quantity:
        quantity = 0
    cart_item = get_single_item(request, item_id)
    if cart_item:
        p = cart_item.product
        p.quantity = p.quantity + cart_item.quantity
        if int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
            p.quantity = p.quantity - int(quantity)
        else:
            remove_from_cart(request)
        p.save()

# remove a single item from cart
def remove_from_cart(request):
    """ function that takes a POST request removes a single product instance from the current customer's
    shopping cart
    """
    postdata = request.POST.copy()
    item_id = postdata['item_id']
    cart_item = get_single_item(request, item_id)
    if cart_item:
        p = cart_item.product
        p.quantity = p.quantity + cart_item.quantity
        p.save()
        cart_item.delete()

def cart_subtotal(request):
    """ gets the subtotal for the current shopping cart """
    is_deal = False
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        """ some cart items may come from the deal of the day section """
        #effective_price = deal_processor.get_effective_price(cart_item.product)
        effective_price = cart_item.product.sale_price
        cart_total += effective_price * cart_item.quantity

        if effective_price < cart_item.product.price:
            is_deal = True

        """ some item may have additional price for a chosen option """
        oc = cart_item.cartitemoption_set.all()
        for o in oc:
            try:
                cart_total += o.price * cart_item.quantity
            except e:
                continue
    request.session["is_deal"] = is_deal

    return cart_total

def cart_subtotal_4_nonsale(request):
    """ gets the subtotal for the current shopping cart """
    cart_total = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
      """ some cart items may come from the deal of the day section """
      if cart_item.product.sale_price == cart_item.product.price:
        effective_price = cart_item.product.sale_price
        cart_total += effective_price * cart_item.quantity

        """ some item may have additional price for a chosen option """
        oc = cart_item.cartitemoption_set.all()
        for o in oc:
            cart_total += o.price * cart_item.quantity

    return cart_total

def cart_productonlypromotion(request, pop, cart_subtotal):
    """ return the product only promotion """

    cart_products = get_cart_items(request)
    if (pop.minimum_price < cart_subtotal) and (pop.discount_amount != 0):
        sale_products = pop.products.all()
        discount = 0.0
        for cart_item in cart_products:
            if (cart_item.product in sale_products) and (cart_item.product.sale_price == cart_item.product.price):
               discount += pop.discount_amount
        return discount

    else:
        if (pop.minimum_price < cart_subtotal) and (pop.discount_percentage != 0.0):
           sale_products = pop.products.all()
           discount = 0.0

           for cart_item in cart_products:
              if (cart_item.product in sale_products) and (cart_item.product.sale_price == cart_item.product.price):
                  oc = cart_item.cartitemoption_set.all()
                  item_total = cart_item.price * cart_item.quantity
                  for o in oc:
                      item_total += o.price * cart_item.quantity

                  discount += float(item_total * pop.discount_percentage)
           return discount

def cart_totalweight(request):
    """ gets the subtotal for the current shopping cart """
    cart_totalweight = decimal.Decimal('0.00')
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        """ some cart items may come from the deal of the day section """
        cart_totalweight += cart_item.product.weight * cart_item.quantity


    return cart_totalweight

def shipping_handling(request, shipping_rate):
    """ calculates the shipping and handling charge for the current shopping cart """
    shipping_charge = decimal.Decimal('0.00')

    if only_giftcertificate_in_cart(request):
        return shipping_charge

    cart_total = cart_subtotal(request)
    if cart_total < settings.MINIMUM_FOR_FREE and decimal.Decimal(shipping_rate) == float(0.00):
        #shipping_charge = cart_total * decimal.Decimal(shipping_rate)
        shipping_charge = float(settings.MINIMUM_POSTAGE)
    else:
        #if  decimal.Decimal(shipping_rate) >= float(0.18):
        surcharge = decimal.Decimal('0.00')
        if decimal.Decimal(shipping_rate) != float(0.00) and cart_total > settings.PRIORITY_EXPRESS_FREE_LIMIT:
            surcharge = cart_total * decimal.Decimal(settings.PRIORITY_EXPRESS_RATE_OVER_LIMIT)
        shipping_charge = shipping_rate + surcharge

    if is_auction(request) and shipping_rate == 0.00:
        shipping_charge = 0.00

    shipping_charge = Decimal(shipping_charge).quantize(Decimal(".01"), rounding = ROUND_UP)
    return shipping_charge

from ecomstore.checkout.models import ShippingMethod
def international_shipping_handling(request, shipping_method_name):
    shippingmethod = ShippingMethod.objects.filter(name=shipping_method_name)[0]
    if "First" in shippingmethod.name:
         if is_auction(request):
             shipping_charge = 0
         else:
             shipping_charge = 17 + (cart_totalweight(request) - 1) * shippingmethod.shipping_rate
    elif "Priority" in shippingmethod.name:
         shipping_charge = 49 + (cart_totalweight(request) - 1) * shippingmethod.shipping_rate
    elif "Express" in shippingmethod.name:
         shipping_charge = 69 + (cart_totalweight(request) - 1) * shippingmethod.shipping_rate
    elif "Fedex" in shippingmethod.name:
         shipping_charge = 59 + (cart_totalweight(request) - 1) * shippingmethod.shipping_rate

    return shipping_charge

def is_bottle(request):
    """ add shipping charge to bottle orders """
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
      """ some cart items may come from the deal of the day section """
      if "89-900" in cart_item.product.name:
          return True
    return False

def domestic_shipping_charge(request, shipping_method_name):
    """ calculates the shipping and handling charge for the current shopping cart """
    shipping_charge = decimal.Decimal('0.00')

    if only_giftcertificate_in_cart(request):
        return shipping_charge

    cart_total = cart_subtotal(request)
    cart_weight = cart_totalweight(request)
    if "Standard" in shipping_method_name:
        if cart_total < settings.MINIMUM_FOR_FREE:
             if cart_weight < 6:
                 shipping_charge = decimal.Decimal('2.5')
             else:
                if cart_weight < 12:
                   shipping_charge = decimal.Decimal('3.75')
                else:
                   shipping_charge = decimal.Decimal('5.35')
        if is_bottle(request):
            shipping_charge = decimal.Decimal('8.0') + cart_weight * decimal.Decimal('0.02')
    else:
        if "Expedited" in shipping_method_name:
             shipping_charge = decimal.Decimal('12.0') + cart_weight * decimal.Decimal('0.2')
        else:
             shipping_charge = decimal.Decimal('24.0') + cart_weight * decimal.Decimal('0.3')

    return shipping_charge

def international_shipping_charge(request, shipping_method_name):
    """ calculates the shipping and handling charge for the current shopping cart """
    shipping_charge = decimal.Decimal('0.00')

    if only_giftcertificate_in_cart(request):
        return shipping_charge

    cart_weight = cart_totalweight(request)
    if "First" in shipping_method_name:
             if cart_weight > 56:
                 shipping_charge = decimal.Decimal('39.00')
             else:
                if cart_weight > 26:
                   shipping_charge = decimal.Decimal('24.75')
                else:
                   shipping_charge = decimal.Decimal('19.00')
    #if "i-Parcel" in shipping_method_name:
    #    from ecomstore.iparcel_driver.driver import iParcel
    #    driver = iParcel()
    #    shipping_charge = driver.GetQuote(request)
    else:
        if "Fedex" in shipping_method_name:
             shipping_charge = 60 + cart_weight * decimal.Decimal('0.4')
        elif "Priority" in shipping_method_name:
             shipping_charge = 39 + cart_weight * decimal.Decimal('0.1')
        else:
             shipping_charge = 55 + cart_weight * decimal.Decimal('0.2')

    return shipping_charge



def shipping_charge(request):
    shipping_country = request.session.get('shipping_country','')
    shipping_method_name = request.session.get('shippingLevel','')
    shippingmethod = ShippingMethod.objects.filter(name=shipping_method_name)[0]
    if shipping_country == 'US':
        shipping_charge = domestic_shipping_charge(request, shipping_method_name)
        #shipping_charge = shipping_handling(request, shippingmethod.shipping_rate)
    else:
        #shipping_charge = international_shipping_handling(request, shipping_method_name)
        shipping_charge = international_shipping_charge(request, shipping_method_name)

    shipping_charge = Decimal(shipping_charge).quantize(Decimal(".01"), rounding = ROUND_UP)
    return shipping_charge


# returns the total number of items in the user's cart
def cart_distinct_item_count(request):
    return get_cart_items(request).count()

def is_empty(request):
    return cart_distinct_item_count(request) == 0

def empty_cart(request):
    """ empties the shopping cart of the current customer """
    user_cart = get_cart_items(request)
    user_cart.delete()

def remove_old_cart_items():
    """ 1. calculate date of 90 days ago (or session lifespan)
    2. create a list of cart IDs that haven't been modified
    3. delete those CartItem instances

    """
    #print "Removing old carts"
    remove_before = datetime.now() + timedelta(days=-settings.SESSION_COOKIE_DAYS)
    cart_ids = []
    old_items = CartItem.objects.values('cart_id').annotate(last_change=Max('date_added')).filter(last_change__lt=remove_before).order_by()
    for item in old_items:
        p = item.product
        p.quantity = p.quantity + item.quantity
        p.save()
        cart_ids.append(item['cart_id'])
    to_remove = CartItem.objects.filter(cart_id__in=cart_ids)
    to_remove.delete()
    #print str(len(cart_ids)) + " carts were removed"

def is_giftcertificate_in_cart(request):
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        if cart_item.product.slug == 'gift-certificate':
             return True
    return False

def only_giftcertificate_in_cart(request):
    cart_products = get_cart_items(request)
    for cart_item in cart_products:
        if cart_item.product.slug != 'gift-certificate':
             return False
    return True


def giftcertificate_value_in_cart(request):
    cart_products = get_cart_items(request)
    gift_value = decimal.Decimal(0.0)
    for cart_item in cart_products:
        if cart_item.product.slug == 'gift-certificate':
           oc = cart_item.cartitemoption_set.all()
           for o in oc:
              gift_value += o.price * cart_item.quantity
    #print 'gift_value: ' + str(gift_value)
    return gift_value
