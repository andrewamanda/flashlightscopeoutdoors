from django.contrib import admin
from ecomstore.checkout.models import Order, OrderItem, ShippingMethod, Promotion, ProductOnlyPromotion, checkout_audit, referral, GiftCertificate
import requests
import json
from ecomstore.checkout.order_management import *
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    form = make_ajax_form(OrderItem,{'product':'products'})

class OrderAdmin(admin.ModelAdmin):
    #list_display = ('__unicode__','all_products','status','transaction_id','user','invoice','packingslip','shippinglabel','date')
    list_display = ('__unicode__','invoice_number','all_products','status','transaction_id','user','tracking','ship_date','invoice','date')
    #list_editable = ('status','user','tracking','ship_date')
    list_filter = ('status','date')
    list_per_page = 25
    search_fields = ('user__username','email','shipping_name','billing_name','invoice_number','id','transaction_id',)
    inlines = [OrderItemInline,]

    readonly_fields = ('isItAuction','auction_price',)

    save_on_top = True
    fieldsets = (
                 ('Basics', {'fields': ('status','email','phone','user','invoice_number')}),
                 ('Shipping', {'fields':('shipping_name','shipping_address_1',
                'shipping_address_2','shipping_city','shipping_state',
                'shipping_zip','shipping_country','shipping_method')}),
                ('Billing', {'fields':('billing_name','billing_address_1',
                'billing_address_2','billing_city','billing_state',
                'billing_zip','billing_country','promotion')}),
                 ('Gift Information', {'fields': ('isItGift','pricePrinted','giftmessage')}),
                 ('Auction', {'fields': ('isItAuction','auction_price')}),
                 ('Order Note', {'fields': ('note',)}),
                 ('Shipment', {'fields': ('tracking','ship_date','shipping_charged')}),
                 )


admin.site.register(Order, OrderAdmin)

class ShippingMethodAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists shipping methods
    list_display = ('name', 'description', 'carrier', 'cutoff_time',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description']
    exclude = []


admin.site.register(ShippingMethod, ShippingMethodAdmin)


class GiftCertificateAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists promotion codes
    list_display = ('code', 'face_value', 'balance', 'value_in_cart', 'from_email', 'to_email', 'created_at', 'updated_at',)
    list_display_links = ('code',)
    list_per_page = 20
    ordering = ['code']
    search_fields = ['code']
    exclude = []

    readonly_fields =('orders_redeemed', )





admin.site.register(GiftCertificate, GiftCertificateAdmin)


class PromotionAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists promotion codes
    list_display = ('code', 'description', 'discount_amount', 'discount_percentage', 'minimum_price', 'valid_from', 'valid_until',)
    list_display_links = ('code',)
    list_per_page = 20
    ordering = ['code']
    search_fields = ['code', 'description']
    exclude = []


admin.site.register(Promotion, PromotionAdmin)

class ProductOnlyPromotionAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists promotion codes
    list_display = ('code', 'description', 'discount_amount', 'discount_percentage', 'minimum_price', 'valid_from', 'valid_until', 'all_products',)
    list_display_links = ('code',)
    list_per_page = 20
    ordering = ['code']
    search_fields = ['code', 'description']
    exclude = []

    filter_horizontal = ('products',)



admin.site.register(ProductOnlyPromotion, ProductOnlyPromotionAdmin)


class AuditAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists promotion codes
    list_display = ('created_at', 'email', 'stage','message','status','ipaddress','cart_id',)
    list_display_links = ('email',)
    list_per_page = 20
    ordering = ['created_at']
    search_fields = ['ipaddress', 'email','cart_id', 'message',]
    exclude = []


admin.site.register(checkout_audit, AuditAdmin)


class ReferalAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','referralCode', 'email')
    filter_horizontal = ('orders',)

admin.site.register(referral, ReferalAdmin)
