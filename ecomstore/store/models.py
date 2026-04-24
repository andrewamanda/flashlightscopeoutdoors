from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import gettext, gettext_lazy as _

from django.core.cache import cache
from ecomstore.settings import CACHE_TIMEOUT, SITE_NAME





class NullConfig(object):
    """Standin for a real config when we don't have one yet."""

    def __init__(self):
        self.store_name = self.store_description = _("Test Store")
        self.store_email = self.street1 = self.street2 = self.city = self.state = self.postal_code = self.phone = ""
        self.site = self.country = None
        self.in_country_only = True
        self.sales_country = None

    def _options(self):
        return ConfigurationSettings()

    options = property(fget=_options)

    def __str__(self):
        return "Test Store - no configured store exists!"

class ConfigManager(models.Manager):
    def get_current(self, site=None):
        """Convenience method to get the current shop config"""
        if not site:
            site = Site.objects.get_current()

        site = site.id

        shop_config = cache.get("Config")
        if not shop_config:
             shop_config = self.get(site__id__exact=site)
             cache.set("Config", shop_config, CACHE_TIMEOUT)

        return shop_config

class Config(models.Model):
    """
    Used to store specific information about a store.  Also used to
    configure various store behaviors
    """
    site = models.OneToOneField(Site, verbose_name=_("Site"), primary_key=True, on_delete=models.CASCADE)
    store_name = models.CharField(_("Store Name"),max_length=100, unique=True)
    store_description = models.TextField(_("Description"), blank=True, null=True)
    store_email = models.EmailField(_("Email"), blank=True, null=True, max_length=75)
    street1=models.CharField(_("Street"),max_length=50, blank=True, null=True)
    street2=models.CharField(_("Street"), max_length=50, blank=True, null=True)
    city=models.CharField(_("City"), max_length=50, blank=True, null=True)
    state=models.CharField(_("State"), max_length=30, blank=True, null=True)
    postal_code=models.CharField(_("Zip Code"), blank=True, null=True, max_length=9)
    #country=models.ForeignKey(Country, blank=False, null=False, verbose_name=_('Country'), on_delete=models.CASCADE)
    phone = models.CharField(_("Phone Number"), blank=True, null=True, max_length=30)
    in_country_only = models.BooleanField(
        _("Only sell to in-country customers?"),
        default=True)

    """
    sales_country = models.ForeignKey(
        Country, blank=True, null=True,
        related_name='sales_country',
        verbose_name=_("Default country for customers"), on_delete=models.CASCADE)
    shipping_countries = models.ManyToManyField(
        Country,
        blank=True,
        verbose_name=_("Shipping Countries"),
        related_name="shop_configs")
    """

    objects = ConfigManager()

    def _options(self):
        return ConfigurationSettings()

    options = property(fget=_options)


    def __unicode__(self):
        return self.store_name

    class Meta:
        verbose_name = _("Store Configuration")
        verbose_name_plural = _("Store Configurations")


