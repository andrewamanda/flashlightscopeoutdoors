from django.contrib import admin
from ecomstore.purchases.models import *
from django.utils.html import format_html
from ecomstore.catalog.models import RichTextField
from ckeditor.widgets import CKEditorWidget
from tinymce.widgets import TinyMCE

# Register your models here.

class AssetDetailsInline(admin.TabularInline):
    model = asset_details
    extra = 0

class AssetServiceHistoryInline(admin.StackedInline):
    model = asset_service_history
    fieldsets = (
                 (None, {'fields': (('service_date','description',),)}),
                 (None, {'fields': (('image1','image2','image3','image4',),)}),
                 (None, {'fields': (('document1','document2','document3','document4',),)}),
                 )
    extra = 0
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }



class AssetTypeAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name',) 

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name']
    exclude = []
# registers your product model with the admin site
admin.site.register(AssetType, AssetTypeAdmin)

class StageAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name',) 

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name']
    exclude = []
# registers your product model with the admin site
admin.site.register(Stage, StageAdmin)



class AssetAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name', 'type', 'stage','usage', 'purchase_date', 'purchase_price', 'purchase_quantity', 'unit_price', 'view_vendor','rating',)

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name', 'vendor']
    list_filter = ('type','vendor')

    fieldsets = (
                 ('Basics', {'fields': ('name','type', ('stage','usage'), 'description','condition','updated_at')}),
                 ('Purchase details', {'fields': ('purchase_date','purchase_price','purchase_quantity','vendor','vendor_url','vendor_phone_number','vendor_email','rating',)}),
                 )
    inlines = [AssetDetailsInline, AssetServiceHistoryInline,]
    exclude = []
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }

    def view_vendor(self, obj):
        return format_html("<a target='_blank' href='http://{url}'>{vendor}</a>", url=obj.vendor_url, vendor=obj.vendor)
    view_vendor.allow_tags = True
    view_vendor.short_description = "Vendor"


# registers your product model with the admin site
admin.site.register(Asset, AssetAdmin)

class AssetDetailsInline(admin.StackedInline):
    model = asset_details
    extra = 0

class ProcurementAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name', 'type', 'usage', 'purchase_date', 'purchase_price', 'purchase_quantity', 'unit_price', 'view_vendor','rating','status','requested_by','approved_by','purchased_by')

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name', 'vendor']
    list_filter = ('status','type','vendor','requested_by','approved_by','purchased_by',)

    fieldsets = (
                 ('Basics', {'fields': ('name','type', ('status','requested_by','approved_by','purchased_by',), 'description','condition','updated_at')}),
                 ('Purchase details', {'fields': ('purchase_date','purchase_price','purchase_quantity','vendor','vendor_url','vendor_phone_number','vendor_email','rating',)}),
                 ('Documents', {'fields': (('receipt1','receipt2'), ('image1','image2'))}),
                 )
    exclude = []
    readonly_fields=('requested_by',)

    def view_vendor(self, obj):
        return format_html("<a target='_blank' href='http://{url}'>{vendor}</a>", url=obj.vendor_url, vendor=obj.vendor)
    view_vendor.allow_tags = True
    view_vendor.short_description = "Vendor"

    def save_model(self, request, obj, form, change):
        if obj.requested_by is None:
             obj.requested_by = request.user.username
             super().save_model(request, obj, form, change)
        else:
             super().save_model(request, obj, form, change)


# registers your product model with the admin site
admin.site.register(Procurement, ProcurementAdmin)

