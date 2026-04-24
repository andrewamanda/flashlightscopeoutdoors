from django.contrib import admin
from ecomstore.inventorymanagement.models import *
from django.utils.html import format_html, mark_safe

# Register your models here.

class ProductItemsInline(admin.TabularInline):
    model = product_item
    readonly_fields=('total_value',)
    extra = 0

class MoreDetailsInline(admin.TabularInline):
    model = more_detail 
    readonly_fields=('image_tag',)
    extra = 0

class FinishingTypeAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name',)

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name',]

    exclude = []

# registers your product model with the admin site
admin.site.register(FinishingType, FinishingTypeAdmin)

class UsageTypeAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name',)

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name',]

    exclude = []

# registers your product model with the admin site
admin.site.register(UsageType, UsageTypeAdmin)

class FinishingGradeAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name',)

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name',]

    exclude = []

# registers your product model with the admin site
admin.site.register(FinishingGrade, FinishingGradeAdmin)

class FinishingPatternAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name',)

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name',]

    exclude = []

# registers your product model with the admin site
admin.site.register(FinishingPattern, FinishingPatternAdmin)

class ProductAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name', 'finishing_type', 'usage_type','finishing_grade', 'finishing_pattern', 'total_quantity', 'total_cost', 'yield_estimate',)

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-name']
    search_fields = ['name', 'vendor']
    list_filter = ('finishing_type','usage_type', 'finishing_grade', 'finishing_pattern')

    fieldsets = (
                 ('Basics', {'fields': ('name','description','updated_at',)}),
                 ('Vendor Information', {'classes': ('collapse', 'open'), 'fields': ('purchase_date','purchase_price','purchase_quantity','vendor','vendor_url','vendor_phone_number','vendor_email')}),
                 ('Specification', {'fields': ('finishing_type','usage_type','finishing_grade','finishing_pattern',)}),
                 ('Cost & Performance', {'fields': ('total_quantity', 'total_cost', 'yield_estimate',)}),
                 )
    inlines = [ProductItemsInline,MoreDetailsInline,]
    exclude = []
    readonly_fields=('total_quantity','total_cost',)

# registers your product model with the admin site
admin.site.register(Product, ProductAdmin)


