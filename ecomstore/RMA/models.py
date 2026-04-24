from django.db import models
import random, string
from ecomstore.catalog.models import Product

from stdimage.models import StdImageField
from ckeditor.widgets import CKEditorWidget
from ecomstore.catalog.models import RichTextField


ID_FIELD_LENGTH = 16
ID_EACH_SEG = 4

PENDING_RETURN = 1
RETURN_RECEIVED = 2
REFUNDED = 3
REPLACEMENT_SHIPPED = 4
PENDING_ACTION = 5
ANDREW_NOTIFIED = 6

RMA_STATUSES = ((PENDING_RETURN,'PENDING_RETURN'),
                 (ANDREW_NOTIFIED,'ANDREW NOTIFIED'),
                 (RETURN_RECEIVED,'RETURN_RECEIVED'),
                 (REFUNDED,'CLOSED-REFUNDED'),
                 (REPLACEMENT_SHIPPED,'CLOSED-REPLACED'),
                 (PENDING_ACTION, 'PENDING_ACTION'),)

ANDREW_AMANDA_DOT_COM = 1
EBAY_ANDREW_AMANDA = 2
EBAY_FLASHLIGHTS_SCOPES = 3
AMAZON = 4
OTHER = 5
ECOSENSA_DOT_COM = 6


STORE_FRONTS = ((ANDREW_AMANDA_DOT_COM,'www.andrew-amanda.com'),
                 (ECOSENSA_DOT_COM,'www.eco-sensa.com'),
                 (EBAY_ANDREW_AMANDA,'eBay: Andrew-Amanda-Outdoors'),
                 (EBAY_FLASHLIGHTS_SCOPES,'eBay: Flashlights-Scopes-Outdoors'),
                 (AMAZON,'Amazon Marketplace'),
                 (OTHER,'Other Source'),)


# Create your models here.


class return_authorization(models.Model):
    # each individual status
    # set of possible RMA statuses

    RMA_number = models.CharField(max_length=ID_FIELD_LENGTH, null=True, blank=True)
    product = models.CharField(max_length=50, null=True, blank=True)
    serial_number = models.CharField(max_length=20, null=True, blank=True, unique=True)
    customer_id_or_order_number = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    rma_status = models.IntegerField(choices=RMA_STATUSES, default=PENDING_RETURN)
    store_front = models.IntegerField(choices=STORE_FRONTS, default=EBAY_ANDREW_AMANDA)
    original_tracking_number = models.CharField(max_length=30, null=True, blank=True)
    replacement_tracking_number = models.CharField(max_length=30, null=True, blank=True)
    condition_returned = models.TextField()
    next_action = models.TextField()
    next_action_date = models.DateField(blank=True, null=True)

    # below attributes are for exporting to Nitecore's RMA Sheet
    Nitecore_to_be_exported = models.BooleanField(default=False)
    problem_description = models.CharField(max_length=50, null=True, blank=True)

    created_at = models.DateField(auto_now=True)
    created_at.editable = True
    closed_at = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.RMA_number
    class Meta:
        db_table = 'rma_management'




    def save(self):
        if not self.RMA_number:
            self.RMA_number = str(random.randint(1000,10000)) + '-' + str(random.randint(100,1000)) + '-' + str(random.randint(1000,10000))
        super(return_authorization, self).save()

class RMAImages(models.Model):
    #a_image = StdImageField(upload_to='images/products/main', size=(300,500))
    #a_image_zoom = StdImageField(upload_to='images/products/main', size=(1024,1024))
    #a_thumbnail = StdImageField(upload_to='images/products/thumbnails', size=(50,50))
    a_image = StdImageField(upload_to='images/rma/main',
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    image_caption = models.CharField(max_length=200, null=True, blank=True)
    return_authorization = models.ForeignKey(return_authorization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'RMAImages'



class actions_taken(models.Model):
    #action_taken = models.TextField()
    last_updated = models.DateField(auto_now=True)
    last_updated.editable = True
    a_image = StdImageField(upload_to='images/rma/main',
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    image_caption = models.CharField(max_length=200, null=True, blank=True, verbose_name="Short Notes")

    return_authorization = models.ForeignKey(return_authorization, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Action Taken'
        verbose_name_plural = 'Actions Taken'

PENDING_AFFIDAVIT = 1
UNDER_REVIEW = 2
REIMBURSED = 3
DENIED = 4

CLAIM_STATUSES = ((PENDING_AFFIDAVIT,'PENDING_AFFIDAVIT'),
                 (UNDER_REVIEW,'UNDER_REVIEW'),
                 (REIMBURSED,'REIMBURSED'),
                 (DENIED, 'DENIED'),)

class insurance_claims(models.Model):
    # each individual status
    # set of possible RMA statuses

    case_number = models.CharField(max_length=20, null=True, blank=True)
    product = models.CharField(max_length=50, null=True, blank=True)
    customer_id_or_order_number = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    store_front = models.IntegerField(choices=STORE_FRONTS, default=EBAY_ANDREW_AMANDA)
    tracking_number = models.CharField(max_length=30, null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    is_buyer_refunded = models.BooleanField(default=False)
    insured_amount = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)

    claim_status = models.IntegerField(choices=CLAIM_STATUSES, default=PENDING_AFFIDAVIT)
    reimbursed_amount = models.DecimalField(max_digits=9,decimal_places=2,
                                    blank=True,default=0.00)
    details = models.TextField()
    closed_date = models.DateField(blank=True, null=True)


    created_at = models.DateField(auto_now=True)
    created_at.editable = True


    def __unicode__(self):
        return self.case_number
    class Meta:
        db_table = 'insurance_claims'

WAIT4APPROVAL = 1
WAIT4SCHEDULING = 2
WIP = 3
WAIT4INFO = 4
CLOSED = 5

TICKET_STATUSES = ((WAIT4APPROVAL,'PENDING APPROVAL'),
                 (WAIT4SCHEDULING,'PENDING SCHEDULING'),
                 (WIP,'WORK IN PROGRESS'),
                 (WAIT4INFO,'NEED MORE INFO'),
                 (CLOSED,'CLOSED'),)

class support_ticket(models.Model):
    # each individual status
    # set of possible RMA statuses

    case_number = models.CharField(max_length=20, null=True, blank=True)
    product = models.CharField(max_length=100, null=True, blank=True, verbose_name="subject")
    customer_id_or_order_number = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    store_front = models.IntegerField(choices=STORE_FRONTS, default=ANDREW_AMANDA_DOT_COM)
    tracking_number = models.CharField(max_length=30, null=True, blank=True)

    ticket_status = models.IntegerField(choices=TICKET_STATUSES, default=WAIT4APPROVAL)
    details = RichTextField()
    closed_date = models.DateField(blank=True, null=True)


    created_at = models.DateField(auto_now=True)
    created_at.editable = True


    def __unicode__(self):
        return self.case_number
    class Meta:
        db_table = 'support_ticket'
        verbose_name = 'Internal Support/Feature Request'
        verbose_name_plural = 'Internal Support/Feature Requests'

class attachment_to_support_ticket(models.Model):
    subject = models.CharField(max_length=40,default="No subject")
    attachment = models.FileField(upload_to='support_ticket/',blank=True)
    support_ticket_entry = models.ForeignKey(support_ticket, on_delete=models.CASCADE)

    class Meta:
       db_table = 'support_ticket_attachments'

LPN_STATUS = (
                  ('NOT RECEIVED' , 'NOT RECEIVED'),
                  ('RECEIVED, READY TO CHECK' , 'RECEIVED, READY TO CHECK'),
                  ('NEW CONDITION' , 'NEW CONDITION'),
                  ('DAMAGED RETURN' , 'DAMAGED RETURN'),
                  ('FRAUD RETURN', 'FRAUD RETURN'),
                  ('REPORTED', 'REPORTED'),
                  ('REJECTED', 'REJECTED'),
                  ('RESOVLED', 'RESOLVED'),
                 )

class AmazonOrderReturnAudit(models.Model):
    return_date = models.CharField(max_length=30, null=True, blank=True)
    order_id = models.CharField(max_length=30)
    sku = models.CharField(max_length=30)
    asin = models.CharField(max_length=30)
    fnsku = models.CharField(max_length=30)
    product_name = models.CharField(max_length=500)
    quantity = models.IntegerField()
    fulfillment_center_id = models.CharField(max_length=30)
    detailed_disposition = models.CharField(max_length=100)
    reason = models.CharField(max_length = 100)
    status = models.CharField(max_length = 30)
    lpn = models.CharField(max_length = 30)
    ticket_id = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(auto_now=True)
    customer_comments = models.CharField(max_length=500, null=True, blank=True)
    internal_status = models.CharField(max_length=50, default='NOT RECEIVED', choices=LPN_STATUS)
    internal_comments = models.TextField(default="Please enter the below information: - The Removal Order ID - FNSKU - Full images of the units received - Image of the tracking label or packing slip from the package that contained the damaged unit - Images of the LPN numbers related to your issue", blank=True)


    def __str__(self):
        return str(self.order_id)

    def __unicode__(self):
        return str(self.order_id)

    class Meta:
        db_table = 'amazonorderreturnaudit'


class AmazonOrderReturnAuditImages(models.Model):
    #a_image = StdImageField(upload_to='images/products/main', size=(300,500))
    #a_image_zoom = StdImageField(upload_to='images/products/main', size=(1024,1024))
    #a_thumbnail = StdImageField(upload_to='images/products/thumbnails', size=(50,50))
    a_image = StdImageField(upload_to='images/AmazonOrderReturnAudit/main',
                    variations={'super': (2024,2048), 'large': (300, 500), 'thumbnail': (50, 50, True)})

    image_caption = models.CharField(max_length=200, null=True, blank=True)
    AmazonOrderReturnAudit = models.ForeignKey(AmazonOrderReturnAudit, on_delete=models.CASCADE)

    class Meta:
        db_table = 'AmazonOrderReturnAuditImages'


alphabet = string.ascii_lowercase + string.digits

for loser in 'l1o0':
    i = alphabet.index(loser)
    alphabet = alphabet[:i] + alphabet[i+1:]

def byte_to_base32_chr(byte):
    return alphabet[byte & 21]

def random_id(length):
    random_bytes = [random.randint(0, 0xFF) for i in range(length)]
    return ''.join(map(byte_to_base32_chr, random_bytes))
