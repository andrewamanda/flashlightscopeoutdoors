from django.contrib import admin
from ecomstore.misc.models import MessageOfTheDay, Testimonial, BannerControl,Customs_Duty_Tracking
from ecomstore.misc.models import barcode, ean_prefix, MediaImage, TodaysNews
from django.db import models
from ckeditor.widgets import CKEditorWidget

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageCustom)

class MessageOfTheDayAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'start_date', 'end_date', 'ranking',)
    list_editable = ('start_date','end_date', 'ranking',)
    formfield_overrides = {
        models.TextField: { 'widget': CKEditorWidget() },
        }


    ordering = ['title']

    save_as = True

    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce.js',
            '/static/js/admin_pages.js'
        )

    actions = ['post_to_facebook_twitter']


    def get_actions(self, request):
        actions = super(MessageOfTheDayAdmin, self).get_actions(request)
        #del actions['delete_selected']
        return actions

    def post_to_facebook_twitter(self, request, queryset):
        for obj in queryset:
            twitterStatus = obj.post2twitter()

        if twitterStatus:
           self.message_user(request, "The message was successfully posted to twitter.")
        else:
           self.message_user(request, "The message was failed to post to twitter.")

    post_to_facebook_twitter.short_description = "Post to facebook and twitter"


admin.site.register(MessageOfTheDay, MessageOfTheDayAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('created_at','name','comment')
    search_fields = ('name',)
    ordering = ['created_at']

admin.site.register(Testimonial, TestimonialAdmin)

class BannerControlAdmin(admin.ModelAdmin):
    list_display = ('name','banner','valid_from', 'valid_to')
    search_fields = ('name',)
    ordering = ['name']

admin.site.register(BannerControl, BannerControlAdmin)

class CustomsDutyAdmin(admin.ModelAdmin):
    list_display = ('order_number','order_amount','tracking_number','customer_name','product_name', 'sku', 'serial_number')
    search_fields = ('manufacturer','tracking_number','pi_number','carrier_invoice_number')
    ordering = ['shipping_date']

    fieldsets = (
                 ('Basic Info', {'fields': (('manufacturer','tracking_number','shipping_date','pi_number','pi_value','details','duty_status'),)}),
                 ('Other Info', {'fields': (('carrier_invoice_number','carrier','declared_value','duty_amount','closed_date',),)}),
                 )

admin.site.register(Customs_Duty_Tracking, CustomsDutyAdmin)


class ean_prefixAdmin(admin.ModelAdmin):
     list_display = ('prefix', 'brand')
     search_fields = ('prefix',)

admin.site.register(ean_prefix, ean_prefixAdmin)

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin
class barcodeAdmin(admin.ModelAdmin):
     list_display = ('EAN', 'product', 'is_used_by_amazon_com', 'is_used_by_amazon_ca','created_at')
     search_fields = ('EAN','product__name')
     ordering = ['created_at',]
     form = make_ajax_form(barcode,{'product':'products'})

admin.site.register(barcode, barcodeAdmin)

class MediaImageAdmin(admin.ModelAdmin):
     list_display = ('type', 'is_active', 'url_link', 'description','order', 'image')
     search_fields = ('type',)
     list_filter = ('type','is_active')
     #list_editable = ('type', 'is_active', 'url_link', 'description','order', 'image')
     ordering = ['order']

admin.site.register(MediaImage, MediaImageAdmin)

from tinymce.widgets import TinyMCE
from ecomstore.catalog.models import RichTextField

class TodaysNewsAdmin(admin.ModelAdmin):
     list_display = ('is_active', 'url_link', 'title','order', 'image', 'valid_from', 'valid_until',)
     search_fields = ('title',)
     list_filter = ('is_active',)
     #list_editable = ('type', 'is_active', 'url_link', 'description','order', 'image')
     ordering = ['order']

     formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
     pass

admin.site.register(TodaysNews, TodaysNewsAdmin)
