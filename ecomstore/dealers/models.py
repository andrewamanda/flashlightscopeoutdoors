from django.db import models
from django.contrib.auth.models import User
from ecomstore.catalog.models import Product
from ecomstore.checkout.models import BaseOrderInfo

# Create your models here.

class DealerApplication(models.Model):

    # each individual status
    SUBMITTED = 1
    APPROVED = 2
    REJECTED = 3
    CANCELLED = 4
    # set of possible order statuses
    ENROLLMENT_STATUSES = ((SUBMITTED,'Submitted'),
                      (APPROVED,'Approved'),
                      (REJECTED,'Rejected'),
                      (CANCELLED,'Cancelled'),)


    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=ENROLLMENT_STATUSES, default=SUBMITTED)
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    business_name = models.CharField(max_length=50)
    location = models.TextField()
    contact = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    website = models.CharField(max_length=50)

    message = models.TextField()

    distributor_comment = models.TextField()

    class Meta:
        db_table = 'dealer_enrollment'
        ordering = ['date']
        
    def __unicode__(self):
        return "Request #" + str(self.id) + " from " + self.business_name + ", " + self.contact


class DealerDiscountRate(models.Model):

    min = models.IntegerField()
    max = models.IntegerField()
    discount_rate = models.DecimalField(max_digits=9,decimal_places=2)


    class Meta:
        db_table = 'dealer_discount_rate'
        ordering = ['min']
        
    def __unicode__(self):
        return "Request #" + str(self.id) + " from " + str(self.min) + " to " + str(self.max)


class DealerOrder(models.Model):

    # each individual status
    SUBMITTED = 1
    PROCESSED = 2
    SHIPPED = 3
    CANCELLED = 4
    # set of possible order statuses
    ORDER_STATUSES = ((SUBMITTED,'Submitted'),
                      (PROCESSED,'Processed'),
                      (SHIPPED,'Shipped'),
                      (CANCELLED,'Cancelled'),)
    #order info
    date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=ORDER_STATUSES, default=SUBMITTED)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  
    discount = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00)

    paymentDate = models.DateTimeField(null=True)
    paymentMethod = models.CharField(max_length=100)


    class Meta:
        db_table = 'dealer_order'
        ordering = ['date']
        
    def __unicode__(self):
        return "Request #" + str(self.id)

class DealerOrderItem(models.Model):
    """ model class for storing each Product instance purchased in each order """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order = models.ForeignKey(DealerOrder, on_delete=models.CASCADE)
    
    @property
    def total(self):
        return self.quantity * round(self.product.price/2)
    
    @property
    def name(self):
        return self.product.name
    
    @property
    def sku(self):
        return self.product.sku
    
    def __unicode__(self):
        return self.product.name + ' (' + self.product.sku + ')'
    
    def get_absolute_url(self):
        return self.product.get_absolute_url()

    @property
    def itemunit(self):
        return self.product.name + '(' + str(self.quantity) + ')'

