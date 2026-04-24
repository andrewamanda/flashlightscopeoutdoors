from django import template
import locale
from decimal import Decimal

register = template.Library()

@register.filter(name='currency')
def currency(value):
    try:
        locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
    except:
        locale.setlocale(locale.LC_ALL,'')
    loc = locale.localeconv()
    if value == None:
        value = '0.00'
    return locale.currency(Decimal(value), loc['currency_symbol'], grouping=True)

# this can be used if you're having trouble configuring the proper locale 
# for your operating system
#@register.filter(name='currency')
#def currency(value):
#    return '$' + str(value)

@register.filter(name='utcconverter')
def utcconverter(value):
	return value.strftime('%m/%d/%Y %H:%M')

	
@register.filter(name='utcconverter2')
def utcconverter2(value):
    return value.strftime('%Y-%m-%dT%H:%M:%S')
	
def contains(value, arg):
    """
    Usage:
    {% if link_url|contains:"http://www.youtube.com/" %}
    Stuff
    {% else %}
    Not stuff
    {% endif %}
    """
    return arg in value

register.filter('contains', contains)

@register.simple_tag 
def percentage(value): 
    return '{0:.2%}'.format(value) 

@register.filter(name='multiply')
def multiply(value, arg):
    return Decimal(value)*Decimal(arg)

@register.filter(name='hasOffer')
def hasOffer(request):
    if not request.user.is_authenticated:
        return False
    from ecomstore.nameyourprice.models import NameYourPrice
    bids = NameYourPrice.objects.filter(user=request.user)
    bid = None
    status = False
    for b in bids:
        if b.status == 'BUYERACCEPTED' or b.status == 'SELLERACCEPTED':
            status = True
            break
    return status
