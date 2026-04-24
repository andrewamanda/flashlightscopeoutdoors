from django import template

register = template.Library()

@register.inclusion_tag("tags/form_table_row.html")
def form_table_row(form_field):
    return {'form_field': form_field }

@register.inclusion_tag("tags/checkout_product_option.html")
def optionalchoices(cartitem, description):
    cio = cartitem.cartitemoption_set.all()
    availability = 'Avail'
    for c in cio:
        if c.availability == 'Soldout':
            availability = 'Soldout'
    return { 'cio': cio, 'description': description, 'availability': availability }

@register.simple_tag 
def express(value): 
    if 'Overnight' in value:
        return 'be delivered'
    else:
        return 'ship'

