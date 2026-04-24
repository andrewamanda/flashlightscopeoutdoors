from ecomstore.catalog.models import Product
from ecomstore import settings


from datetime import datetime

def get_effective_price(product):
    """ get the effective price """
    """ No longer used, merged into the product.sale_price """
    effective_price = product.price
    if product.sale_price:
        effective_price = product.sale_price
    else:
        curr = datetime.now()
        deals = product.dealoftheday_set.filter(end_date__gte=curr).exclude(start_date__gte=curr)
        for d in deals:
            if d.quantity > 0:
                effective_price = d.deal_price
    return effective_price

