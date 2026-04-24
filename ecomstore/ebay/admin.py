from django.contrib import admin
from ecomstore.ebay.models import EBayListing,RichTextField,BonusAccessories

from tinymce.widgets import TinyMCE

class BonusAccessoriesInline(admin.TabularInline):
   model = BonusAccessories
   extra = 0

class EBayListingAdmin(admin.ModelAdmin):
   list_display = ('name','all_included','posted','price','little_ebay_title','big_ebay_title')
   list_display_links = ('name','all_included')
   list_editable = ('posted','price','little_ebay_title','big_ebay_title')
   ordering = ['name']
   search_fields = ['name',]
   exclude = []

   list_filter = ('posted',)
   filter_horizontal = ('products', )
   list_per_page = 30

   formfield_overrides = {
        RichTextField: { 'widget': TinyMCE() },
        }
   pass
   class Media:
         js = ('/media/js/jquery.js',
               '/media/js/jquery-1.4.4.min.js',
               '/media/js/tinymce.placeholdereditor.js',
               '/media/js/jquery.ui.core.js',
               '/media/js/placeholder_editor_registry.js',
               '/media/js/jquery.wymeditor.js',
               '/media/js/myFileBrowser.js',
               '/media/css/jquery-ui.css',
               '/media/css/tinymce_toolbar.css'
               )


   fieldsets = (
                 ('Basics', {'fields': ('name','products','front_image','little_ebay_title','big_ebay_title','price',)}),
                 ('Add-On', {'fields': ('comment_little_ebay','comment_big_ebay')}),
                 ('Generated', {'fields': ('little_ebay_description','big_ebay_description','amazon_description','posted',)}),
                 )

   inlines = [BonusAccessoriesInline,]
   save_on_top = True
   save_as = True

admin.site.register(EBayListing, EBayListingAdmin)
