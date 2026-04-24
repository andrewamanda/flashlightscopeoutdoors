# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ecomstore.catalog.models import Product

# Create your models here.

class CustomerAccounts(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=30)
    customer_address = models.CharField(max_length=200)
    credit_card_number = models.CharField(max_length=16)
    credit_card_security = models.CharField(max_length=10)
    credit_card_expiration = models.DateField(null=True, blank=True)
    description = models.TextField()

    class Meta:
         db_table = "customer_accounts"
         ordering = ['customer_name']

    def __str__(self):
        return self.customer_email

    def __unicode__(self):
         return self.customer_email

class CustomerOffers(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    product = models.ForeignKey(Product)
    offer_price = models.CharField(max_length = 10)
    quantity = models.IntegerField()
    notes = models.CharField(max_length = 200)
    account = models.ForeignKey(CustomerAccounts)
