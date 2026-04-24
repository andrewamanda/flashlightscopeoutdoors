from django.contrib import admin
from ecomstore.stats.models import ProductView


class ProductViewAdmin(admin.ModelAdmin):
    list_display = ('date','ip_address','tracking_id', 'product', 'user')
    search_fields = ('ip_address','product')
    ordering = ['date']

admin.site.register(ProductView, ProductViewAdmin)

