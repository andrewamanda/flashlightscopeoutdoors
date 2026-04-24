from django.contrib import admin
from ecomstore.store.models import Config


class ConfigOptions(admin.ModelAdmin):
    list_display = ('site', 'store_name')
    fieldsets = (
        (None, {'fields': (
            'site', 'store_name', 'store_description')
            }),
        ('Store Contact', {'fields' : (
            'store_email', 'phone', 'street1', 'street2',
            'city', 'state', 'postal_code',)
            })
    )

admin.site.register(Config, ConfigOptions)
