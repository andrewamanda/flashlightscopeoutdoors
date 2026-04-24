from django.db import models
from django.contrib.auth.models import User
from ecomstore.checkout.models import BaseOrderInfo

#from django_facebook.models import FacebookProfileModel


class UserProfile(BaseOrderInfo):
    """ stores customer order information used with the last order placed; can be attached to the checkout order form
    as a convenience to registered customers who have placed an order in the past.

    """
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)


    def __str__(self):
        return 'User Profile for: ' + self.user.username

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """Create a matching profile whenever a user object is created."""
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
