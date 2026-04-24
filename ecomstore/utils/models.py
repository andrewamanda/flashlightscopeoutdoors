from django.db import models

# Create your models here.

class base_country(models.Model):
    """ model class for storing the shipping methods """
    id = models.PositiveIntegerField(primary_key = True)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)
    name_en = models.CharField(max_length=64, null=True, blank=True)
    name_fr = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        db_table = 'base_country'
    
    def __unicode__(self):
        return unicode(self.name_en)
