from django.db import models

# Create your models here.
		
class emails_from_paypal(models.Model):
    """
    This table now holds all the emails from the paypal, the newsletter subscription and the orders
    """
    email = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    imported_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        db_table = 'emails_from_paypal'
        ordering = ['email']
  

    def __unicode__(self):
        return u"%s" % (self.email)


