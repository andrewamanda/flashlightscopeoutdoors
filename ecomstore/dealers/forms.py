from django import forms
from ecomstore.catalog.models import Brand, Product, Category, ProductReview
from tagging.models import Tag
from ecomstore.settings import DISTRIBUTOR_BRAND_SLUG
from django.shortcuts import get_object_or_404

from ecomstore.dealers.models import DealerOrder, DealerOrderItem


class DealerOrderForm(forms.Form):

    def __init__(self, *args, **kwargs):
        #products = kwargs.pop('products', None)

        super(DealerOrderForm, self).__init__(*args, **kwargs)

        brand = get_object_or_404(Brand.active, slug=DISTRIBUTOR_BRAND_SLUG)
        active_series = brand.series_set.filter(is_active=True).order_by('ranking')
        products = brand.product_set.filter(is_active=True) 

        for series in active_series:
            for product in products:
              if product.series.name == series.name:
 
                kw = {
                'label' : product.meta_description,
                'help_text' : round(product.price/2),
                'initial' : product.quantity,
                'widget' : forms.TextInput(attrs={'size':'10'}) }



                kw['initial'] = 0
                qty = forms.DecimalField(**kw)
                self.fields['qty__%s' % product.slug] = qty
                qty.slug = product.slug
                qty.product_id = product.id


 

    def save(self, request):
        self.full_clean()

        dealerOrder = DealerOrder()
        dealerOrder.user = request.user
 
        dealerOrder.save()

        for name, value in self.cleaned_data.items():
            opt, key = name.split('__')

            prod = Product.objects.get(slug__exact=key)
            if opt=='qty':
                if value != 0:
                    request.user.message_set.create(message='Updated %s stock to %s' % (key, value))
                    #log.debug('Saving new qty=%d for %s' % (value, key))

                    dealerOrderItem = DealerOrderItem()
                    dealerOrderItem.product = prod
                    dealerOrderItem.quantity = value
                    dealerOrderItem.order = dealerOrder
                    dealerOrderItem.save()
