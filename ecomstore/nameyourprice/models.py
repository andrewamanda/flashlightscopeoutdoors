from django.db import models
from ecomstore.catalog.models import Product
from datetime import datetime
#from django_model_changes import ChangesMixin, post_change
#from django.dispatch import receiver

from django.contrib.auth.models import User
from django.utils.encoding import smart_str

# Create your models here.

BID_STATUS_TUPLES = (
    ('WAIT4SELLER', 'Wait for Seller'),
    ('WAIT4BUYER', 'Wait for Buyer'),
    ('BUYERACCEPTED', 'Accepted by Buyer'),
    ('SELLERACCEPTED', 'Accepted by Seller'),
    ('BUYERDECLINED', 'Declined by Buyer'),
    ('SELLERDECLINED', 'Declined by Seller'),
    ('BUYERCANCELLED', 'Cancelled by Buyer'),
    ('PAID', 'Paid by Buyer'),
)

class NameYourPrice(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20,choices=BID_STATUS_TUPLES, default='WAIT4SELLER')
    seller_to_accept = models.BooleanField(default=False)
    reason = models.TextField(blank=True, null=True)
    shipping_country = models.CharField(max_length=20,default='United States')
    device = models.CharField(max_length=20,default='Desktop')
    last_updated = models.DateTimeField(auto_now_add=True)

    class Meta:
       db_table = 'nameyourprice'

    def save(self):
        if self.status == "WAIT4SELLER" and self.seller_to_accept == True:
            self.status = "SELLERACCEPTED"
        super(NameYourPrice, self).save()

        if self.status == "BUYERCANCELLED" or self.status == "BUYERDECLINED" or self.status == "BUYERACCEPTED" or self.status == "SELLERACCEPTED":
            send_email_if_bid_status_change(self)

    def last_offer(self):
        offerhistories = self.offerhistory_set.all().order_by('-buyer_offer_date')
        if len(offerhistories) == 0:
            return "No Offer history"
        if offerhistories[0].seller_offer_price:
             return '${} by {} on {}'.format(offerhistories[0].seller_offer_price,'Seller',offerhistories[0].seller_offer_date)
        return '${} by {} on {}'.format(offerhistories[0].buyer_offer_price,self.user.email,offerhistories[0].buyer_offer_date)

    def all_products(self):
        products = self.productoffered_set.all()
        return ', '.join([c.product.name for c in products.all()])
    def is_open(self):
       if self.status == "WAIT4BUYER" or self.status == "WAIT4SELLER" or self.status == "BUYERACCEPTED" or self.status == "SELLERACCEPTED":
           return True
       else:
          return False

    def bin_price(self):
        products = self.productoffered_set.all()
        buyitnow_price = 0
        for p in products:
            buyitnow_price += p.product.price * p.qty_offered
        return buyitnow_price

    def sale_price(self):
        products = self.productoffered_set.all()
        total_sale_price = 0
        for p in products:
            total_sale_price += p.product.sale_price * p.qty_offered
        return total_sale_price

    
class ProductOffered(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty_offered = models.IntegerField()
    bid = models.ForeignKey(NameYourPrice, on_delete=models.CASCADE)

    class Meta:
        db_table = 'nameyourprice_productoffered'

class OfferHistory(models.Model):
    buyer_offer_date = models.DateTimeField(blank=True, null=True)
    buyer_offer_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True, null=True)
    buyer_comment = models.TextField(blank=True, null=True)

    seller_offer_date = models.DateTimeField(blank=True, null=True)
    seller_offer_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True, null=True)
    seller_comment = models.TextField(blank=True, null=True)

    bid = models.ForeignKey(NameYourPrice, on_delete=models.CASCADE)

    class Meta:
       db_table = 'nameyourprice_offerhistory'

    def save(self):
        super(OfferHistory, self).save()
        if self.seller_offer_price:
            self.bid.status = 'WAIT4BUYER'
            self.bid.save()
            send_email_if_bid_status_change(self.bid)
        else:
            self.bid.status = 'WAIT4SELLER'
            self.bid.save()
            send_email_if_bid_status_change(self.bid)
    
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



#def send_email_if_flag_enabled(sender, instance, **kwargs):
#    if instance.previous_instance().wait4buyer == False and instance.wait4buyer == True:
#        # send email
#        print "Wait for buyer flag set"

#post_change.connect(send_email_if_flag_enabled, NameYourPrice)
