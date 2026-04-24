from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.urls import reverse

STATUS_TUPLES = (
    ('WAIT4ADMIN', 'Wait for Administrator'),
    ('WAIT4CUSTOMER', 'Wait for Customer'),
)

class CustomerRelationship(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=STATUS_TUPLES, default='WAIT4ADMIN')
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    is_current_customer = models.BooleanField(default=False)

    is_business = models.BooleanField(default=False)
    business_type = models.CharField(max_length=30, blank=True, null=True)
    business_name = models.CharField(max_length=30, blank=True, null=True)

    sign_up_for_newsletter = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)

    device = models.CharField(max_length=20,default='Desktop')
    last_updated = models.DateField(auto_now_add=True)

    class Meta:
       db_table = 'heartwood_customerrelationship'



class CorrespondenceEntry(models.Model):
    customer_contact_date = models.DateField(blank=True, null=True, verbose_name='Date')
    subject = models.CharField(max_length=40,default="No subject")
    customer_comment = models.TextField(blank=True, null=True, verbose_name='Customer Message')

    admin_contact_date = models.DateField(blank=True, null=True, verbose_name='Date')
    admin_comment = models.TextField(blank=True, null=True, verbose_name='Our Response')

    customer_attachment_1 = models.FileField(upload_to='customercontact/',blank=True)
    customer_attachment_2 = models.FileField(upload_to='customercontact/',blank=True)
    our_attachment_1 = models.FileField(upload_to='customercontact/',blank=True)
    our_attachment_2 = models.FileField(upload_to='customercontact/',blank=True)
    has_response_been_sent = models.BooleanField(default=False, verbose_name='Our response sent?')


    contact_entry = models.ForeignKey(CustomerRelationship, on_delete=models.CASCADE)

    class Meta:
       db_table = 'heartwood_correspondence'



def send_email_if_bid_status_change(bid):
    customer_email = bid.user.email
    seller_email = "sales@andrew-amanda.com"

    products = bid.productoffered_set.all()
    offerhistories = bid.offerhistory_set.all().order_by('-buyer_offer_date')

    all_products = ""
    for p in products:
       all_products += "\n\n\t{}  Qty: {}".format(smart_str(p.product.meta_description), p.qty_offered)

    newoffer = False
    if len(offerhistories) == 1 and bid.status == 'WAIT4SELLER':
       newoffer = True

    curr_offer = offerhistories[0]
    if curr_offer.seller_offer_price:
       outstandingoffer = curr_offer.seller_offer_price
    else:
       outstandingoffer = curr_offer.buyer_offer_price

    message = "Customer:\t{} ".format(bid.user.email)
    message += "\n\nShipping country:\t{}".format(bid.shipping_country)
    message += "\n\nStatus:\t{}".format(bid.get_status_display())
    message += "\n\n"

    if bid.status == "WAIT4BUYER" or bid.status == "WAIT4SELLER":
        if newoffer:
            message += "You have received an offer for the following product(s):"
            subject = "You have received a new offer"
        else:
            subject = "You have received a counter offer"
            message += "You have received a counter offer for the following product(s):"

    if bid.status == "BUYERCANCELLED":
       subject = "Buyer has cancelled his offer"
       message += "Buyer has cancelled his offer for the following products:"
    elif bid.status == "BUYERDECLINED":
       subject = "Buyer has declined your offer"
       message += "Buyer has declined your offer for the following products:"
    elif bid.status == "BUYERACCEPTED":
       subject = "Buyer has accepted your offer"
       message += "Buyer has accepted your offer for the following products:"
    elif bid.status == "SELLERACCEPTED":
       subject = "Seller has accepted your offer"
       message += "Seller has accepted your offer for the following products:"


    message += all_products

    message += "\n\nBuy It Now Price:\t${}".format(bid.bin_price())
    message += "\n\nLatest Offer Price:\t${}".format(outstandingoffer)

    if bid.status == 'SELLERACCEPTED':
       if bid.reason:
          message += "\n\nSeller Comment:\t{}".format(smart_str(bid.reason))


    if bid.status == 'WAIT4SELLER' and curr_offer.buyer_comment:
       message += "\n\nBuyer Comment:\t{}".format(smart_str(curr_offer.buyer_comment))
    if bid.status == 'WAIT4BUYER' and curr_offer.seller_comment:
       message += "\n\nSeller Comment:\t{}".format(curr_offer.seller_comment)

    if bid.status == "BUYERCANCELLED" or bid.status == "BUYERDECLINED":
       if bid.reason:
          message += "\n\nReason:\t{}".format(smart_str(bid.reason))

    from django.contrib.sites.models import Site
    message += smart_str("\n\nPlease visit back our web store http://" + Site.objects.get_current().domain + "/nameyourprice/viewyouroffer/ to view your offer and proceed to the next action")


    #from django.core.mail import EmailMessage
    from ecomstore.utils.email import send_mail_async
    if bid.status == 'WAIT4SELLER' or bid.status == "BUYERACCEPTED" or bid.status == 'BUYERCANCELLED' or bid.status == 'BUYERDECLINED':
       #EmailMsg = EmailMessage(subject, message, seller_email, [seller_email],[seller_email], headers={'Reply-To':seller_email})
       send_mail_async(subject, message, seller_email, [seller_email],fail_silently=False, html='')
    else:
       #EmailMsg = EmailMessage(subject, pList, seller_email, [customer_email],[seller_email], headers={'Reply-To':seller_email})
       send_mail_async(subject, message, seller_email, [customer_email,seller_email],fail_silently=False, html='')
    #EmailMsg.send()

BIZTYPE_TUPLES = (
    ('PRIVATELAB', 'PRIVATE LABORATORY'),
    ('PRIVATECORP', 'PRIVATE COMPANY'),
    ('NONPROFIT', 'Non Profit Organization'),
    ('GOV', 'Government Agency'),
    ('GOVDESIGNATE', 'Government Designated Laboratory'),
    ('HOMEOWNER', 'HomeOwner'),
    ('OTHERS', 'Others'),
)
from ecomstore.catalog.models import RichTextField

class CustomerLead(models.Model):
    followup_required = models.BooleanField(default=False)
    date_to_follow = models.DateField(blank=True, null=True)
    converted_to_orders = models.BooleanField(default=False)

    customer_name = models.CharField(max_length=100, default=' ')
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    open_balance = models.DecimalField(max_digits=9,decimal_places=2, default=0.0)


    is_business = models.BooleanField(default=False)
    business_type = models.CharField(max_length=20,choices=BIZTYPE_TUPLES, default='HOMEOWNER')
    company = models.CharField(max_length=50, blank=True, null=True)

    notes = RichTextField(blank=True, null=True)

    last_updated = models.DateField(auto_now_add=True)

    class Meta:
       db_table = 'heartwood_customerleads'

class CallLogs(models.Model):
    contact_date = models.DateField(blank=True, null=True, verbose_name='Date')
    subject = models.CharField(max_length=40,default="No subject")
    notes = models.TextField(blank=True, null=True,)
    attachment = models.FileField(upload_to='customerleads/',blank=True)

    lead_entry = models.ForeignKey(CustomerLead, on_delete=models.CASCADE)

    class Meta:
       db_table = 'heartwood_calllogs'

class Leads_Purchased(models.Model):
    email_sent = models.BooleanField(default=False)

    first_name = models.CharField(max_length=100,blank=True, null=True)
    middle_name = models.CharField(max_length=100,blank=True, null=True)
    last_name = models.CharField(max_length=100,blank=True, null=True)
    company_name = models.CharField(max_length=100,blank=True, null=True)
    executive_title = models.CharField(max_length=50,blank=True, null=True)

    address_line_1 = models.CharField(max_length=100, blank=True, null=True)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True)
    revenue = models.CharField(max_length=100, blank=True, null=True)
    employees_size = models.CharField(max_length=10, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    email_address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)


    notes = RichTextField(blank=True, null=True)

    last_updated = models.DateField(auto_now_add=True)

    class Meta:
       db_table = 'heartwood_leadspurchased'



class ActiveBlogManager(models.Manager):
    """ Manager class to return only those categories where each instance is active """
    def get_queryset(self):
        return super(ActiveBlogManager, self).get_queryset().filter(ready_to_publish=True)
import uuid
class Reclaimed_Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ready_to_publish = models.BooleanField(default=False)
    name = models.CharField(max_length=100,blank=True, null=True)
    title = models.CharField(max_length=300,blank=True, null=True)
    subtitle = models.CharField(max_length=300,blank=True, null=True)
    summary = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    content = RichTextField(blank=True, null=True)

    last_updated = models.DateField(auto_now_add=True)

    RANKING_CHOICES = [(i, i) for i in range(1, 101)]
    ranking = models.IntegerField(choices=RANKING_CHOICES)

    objects = models.Manager()
    active = ActiveBlogManager()

    class Meta:
       db_table = 'reclaimed_blog'
    def __str__(self):
        return str(self.id)
    def __unicode__(self):
        return str(self.id)
    def get_absolute_url(self):
        return reverse('blog', args=(self.slug,))
