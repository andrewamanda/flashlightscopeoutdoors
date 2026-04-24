from django.contrib import admin
from ecomstore.nameyourprice.models import NameYourPrice, OfferHistory, ProductOffered

class OfferHistoryInline(admin.StackedInline):
    model = OfferHistory
    readonly_fields = ('buyer_offer_date','buyer_offer_price','buyer_comment',)
    fieldsets = (
                 ('Buyer Offer', {'fields': (('buyer_offer_date','buyer_offer_price','buyer_comment',),)}),
                 ('Seller Counter Offer', {'fields': (('seller_offer_date','seller_offer_price','seller_comment',),)}),
                 )

    extra = 0

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

class ProductOfferedInline(admin.TabularInline):
    model = ProductOffered
    form = make_ajax_form(ProductOffered,{'product':'products'})
    extra = 0

class NameYourPriceAdmin(admin.ModelAdmin):
    list_display = ('user','status', 'last_offer', 'bin_price', 'device', 'last_updated')
    list_per_page = 10
    list_filter = ('status','device',)
    ordering = ['-last_updated']
    search_fields = ['user__username']

    readonly_fields = ('last_offer','bin_price','sale_price','status','user_email',)

    fieldsets = (
                 ('Basics', {'fields': (('user','shipping_country','user_email',),('status', 'bin_price', 'sale_price', 'last_offer',), ('seller_to_accept', 'reason',))}),
                 )

    inlines = [OfferHistoryInline, ProductOfferedInline,]

    def last_offer(self, obj):
        return obj.last_offer()
    def bin_price(self, obj):
        return "${}".format(obj.bin_price())
    def user_email(self, obj):
        return obj.user.email
    
admin.site.register(NameYourPrice, NameYourPriceAdmin)

