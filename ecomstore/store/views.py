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

        try:
            shop_config = keyedcache.cache_get("Config", site)
        except keyedcache.NotCachedError, nce:
            try:
                shop_config = self.get(site__id__exact=site)
                keyedcache.cache_set(nce.key, value=shop_config)
            except Config.DoesNotExist:
                log.warning("No Shop Config found, using test shop config for site=%s.", site)
                shop_config = NullConfig()

        return shop_config

class Config(models.Model):
    """
    Used to store specific information about a store.  Also used to
    configure various store behaviors
    """
    site = models.OneToOneField(Site, verbose_name=_("Site"), primary_key=True)
    store_name = models.CharField(_("Store Name"),max_length=100, unique=True)
    store_description = models.TextField(_("Description"), blank=True, null=True)
    store_email = models.EmailField(_("Email"), blank=True, null=True, max_length=75)
    street1=models.CharField(_("Street"),max_length=50, blank=True, null=True)
    street2=models.CharField(_("Street"), max_length=50, blank=True, null=True)
    city=models.CharField(_("City"), max_length=50, blank=True, null=True)
    state=models.CharField(_("State"), max_length=30, blank=True, null=True)
    postal_code=models.CharField(_("Zip Code"), blank=True, null=True, max_length=9)
    country=models.ForeignKey(Country, blank=False, null=False, verbose_name=_('Country'))
    phone = models.CharField(_("Phone Number"), blank=True, null=True, max_length=30)
    in_country_only = models.BooleanField(
        _("Only sell to in-country customers?"),
        default=True)
    sales_country = models.ForeignKey(
        Country, blank=True, null=True,
        related_name='sales_country',
        verbose_name=_("Default country for customers"))
    shipping_countries = models.ManyToManyField(
        Country,
        blank=True,
        verbose_name=_("Shipping Countries"),
        related_name="shop_configs")

    objects = ConfigManager()

    def _options(self):
        return ConfigurationSettings()

    options = property(fget=_options)

    def areas(self):
        """Get country areas (states/counties).  Used in forms."""
        if self.in_country_only:
            return self.sales_country.adminarea_set.filter(active=True)
        else:
            return None

    def countries(self):
        """Get country selections.  Used in forms."""
        if self.in_country_only:
            return Country.objects.filter(pk=self.sales_country.pk)
        else:
            return self.shipping_countries.filter(active=True)


    def _base_url(self, secure=False):
        prefix = "http"
        if secure:
            prefix += "s"
        return prefix + "://" + self.site.domain

    base_url = property(fget=_base_url)

    def save(self, **kwargs):
        keyedcache.cache_delete("Config", self.site.id)
        # ensure the default country is in shipping countries
        mycountry = self.country

        if mycountry:
            if not self.sales_country:
                log.debug("%s: No sales_country set, adding country of store, '%s'", self, mycountry)
                self.sales_country = mycountry

# This code doesn't work when creating a new site. At the time of creation, all of the necessary relationships
# aren't setup. I modified the load_store code so that it would create this relationship manually when running
# with sample data. This is a bit of a django limitation so I'm leaving this in here for now. - CBM
#            salescountry = self.sales_country
#            try:
#                need = self.shipping_countries.get(pk=salescountry.pk)
#            except Country.DoesNotExist:
#                log.debug("%s: Adding default country '%s' to shipping countries", self, salescountry.iso2_code)
#                self.shipping_countries.add(salescountry)
        else:
            log.warn("%s: has no country set", self)

        super(Config, self).save(**kwargs)
        keyedcache.cache_set("Config", self.site.id, value=self)

    def __unicode__(self):
        return self.store_name

    class Meta:
        verbose_name = _("Store Configuration")
        verbose_name_plural = _("Store Configurations")


