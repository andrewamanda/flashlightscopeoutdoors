from django.contrib import admin
from ecomstore.csvimport_app.models import emails_from_paypal


class emails_from_paypalAdmin(admin.ModelAdmin):
    list_display = ('email','name','imported_at')
    search_fields = ('email',)
    ordering = ['email']
    
admin.site.register(emails_from_paypal, emails_from_paypalAdmin)
