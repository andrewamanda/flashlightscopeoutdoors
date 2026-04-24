# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin


from ecomstore.customers.models import *

from django.contrib.admin import DateFieldListFilter
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin


class CustomerOffersInline(admin.StackedInline):
    model = CustomerOffers
    extra = 0
    form = make_ajax_form(CustomerOffers,{'product':'products'})


class CustomerAccountsAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email',)
    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('customer_name','customer_email')
    list_per_page = 50
    ordering = ['-customer_name']
    search_fields = ['customer_name', 'customer_email',]
    inlines = [CustomerOffersInline,]


    fieldsets = (
                 ('Customer Info', {'fields': (('customer_name'),('customer_email','customer_address'),)}),
                 ('Credit Card', {'fields': (('credit_card_number','credit_card_security','credit_card_expiration',),)}),
                 ('Extra', {'fields': (('description'),)})
                )

admin.site.register(CustomerAccounts, CustomerAccountsAdmin)
