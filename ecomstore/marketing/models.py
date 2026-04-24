from django.db import models
from ecomstore.catalog.models import Product
from django.contrib.auth.models import User
from ecomstore.utils.countries import *
from datetime import timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import logging

# Create your models here.

GROUPBUY_STATUS_TUPLES = (
    ('NOTSTART', 'Not started'),
    ('OPEN', 'Open for enrolling'),
    ('CLOSED_COUPON_SENT', 'Closed, Coupon emailed'),
    ('CLOSED_COUPON_WAITING', 'Closed, Pending coupon'),
    ('CLOSED_NOT_ENOUGH', 'Closed, Few participants'),
)

class GroupBuyProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    min_quantity = models.IntegerField()
    max_quantity = models.IntegerField()
    start_date = models.DateField()
    cutoff_date = models.DateField()
    comment = models.CharField(max_length=300, blank=True, null=True)
    status = models.CharField(max_length=30,choices=GROUPBUY_STATUS_TUPLES, default='NOTSTART')
    coupon = models.CharField(max_length=30, blank=True, null=True)
    discount = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'groupbuy_product'

class GroupBuyParticipant(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField()
    reason = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=2,choices=COUNTRY_TUPLES, default='US')
    state = models.CharField(max_length=20, blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True)
    p=models.ForeignKey(GroupBuyProduct, on_delete=models.CASCADE)

    class Meta:
       db_table = 'groupbuy_participants'


    def as_dict(self):
        return {
             "id": self.id,
             "user": self.user.username,
             "email": self.email,
             "name": self.name,
             "quantity": self.quantity,
             "reason": self.reason,
             "country": self.country,
             "state": self.state,
             "last_updated": str(self.last_updated)
        }

    def sendgroupbuycoupon(self):
        status = False
        email = self.email
        name = self.name
        template = "marketing/groupbuycoupon.html"
        expires = self.p.cutoff_date + timedelta(days=7)
        msg = render_to_string(template, {'coupon': self.p.coupon, 'discount': self.p.discount,'email': email, 'name': name, 'product': self.p.product.meta_description, 'url': self.p.product.get_absolute_url(), 'expires': expires})
        subject = "Group Buy Coupon Delivery for {})".format(self.p.product.name)

        EmailMsg = EmailMessage(subject,msg,"sales@andrew-amanda.com",[email],headers={'Reply-To':settings.EMAIL_ORDER})
        EmailMsg.content_subtype = "html"
        try:
              EmailMsg.send()
              status = True
        except Exception as e:
              logging.error("In Exc sending mail to %s -- Error: %s", self.email, e)

        return status
