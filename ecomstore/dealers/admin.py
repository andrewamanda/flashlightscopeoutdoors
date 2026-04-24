from django.contrib import admin
from ecomstore.dealers.models import DealerApplication, DealerDiscountRate, DealerOrder, DealerOrderItem


class DealerApplicationAdmin(admin.ModelAdmin):
    list_display = ('date','status','business_name', 'user')
    search_fields = ('business_name',)
    ordering = ['date']
    
admin.site.register(DealerApplication, DealerApplicationAdmin)

class DealerDiscountRateAdmin(admin.ModelAdmin):
    list_display = ('min','max','discount_rate')
    search_fields = ('min',)
    ordering = ['min']
    
admin.site.register(DealerDiscountRate, DealerDiscountRateAdmin)

class DealerOrderItemInline(admin.TabularInline):
    model = DealerOrderItem
    extra = 0

class DealerOrderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','date','status','user')
    list_filter = ('status','date')
    search_fields = ('user',)
    inlines = [DealerOrderItemInline,]

    
admin.site.register(DealerOrder, DealerOrderAdmin)



