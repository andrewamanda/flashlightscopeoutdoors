from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from pprint import pformat
import sys, datetime, logging
import smtplib
from email.mime.text import MIMEText
import logging
from django.core.mail import EmailMessage
from ecomstore.catalog.models import RichTextField
from ckeditor.widgets import CKEditorWidget

class ReferenceUSADataBase(models.Model):
    """
    This table now holds all the emails from the paypal, the newsletter subscription and the orders
    """
    company_name = models.CharField(max_length=255)
    executive_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True, unique=True)
    city = models.CharField(max_length=55, null=True, blank=True)
    state = models.CharField(max_length=55, null=True, blank=True)
    zip = models.CharField(max_length=10, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    primary_sic_code = models.CharField(max_length=55, null=True, blank=True)
    primary_sic_description = models.CharField(max_length=255, null=True, blank=True)
    sic_code_1 = models.CharField(max_length=55, null=True, blank=True)
    sic_code_1_description = models.CharField(max_length=255, null=True, blank=True)
    sic_code_2 = models.CharField(max_length=55, null=True, blank=True)
    sic_code_2_description = models.CharField(max_length=255, null=True, blank=True)
    sic_code_3 = models.CharField(max_length=55, null=True, blank=True)
    sic_code_3_description = models.CharField(max_length=255, null=True, blank=True)
    sic_code_4 = models.CharField(max_length=55, null=True, blank=True)
    sic_code_4_description = models.CharField(max_length=255, null=True, blank=True)
    sic_code_5 = models.CharField(max_length=55, null=True, blank=True)
    sic_code_5_description = models.CharField(max_length=255, null=True, blank=True)
    primary_naics_code = models.CharField(max_length=55, null=True, blank=True)
    primary_naics_description = models.CharField(max_length=255, null=True, blank=True)
    naics_code_1 = models.CharField(max_length=55, null=True, blank=True)
    naics_1_description = models.CharField(max_length=255, null=True, blank=True)
    naics_code_2 = models.CharField(max_length=55, null=True, blank=True)
    naics_2_description = models.CharField(max_length=255, null=True, blank=True)
    naics_code_3 = models.CharField(max_length=55, null=True, blank=True)
    naics_3_description = models.CharField(max_length=255, null=True, blank=True)
    naics_code_4 = models.CharField(max_length=55, null=True, blank=True)
    naics_4_description = models.CharField(max_length=255, null=True, blank=True)
    naics_code_5 = models.CharField(max_length=55, null=True, blank=True)
    naics_5_description = models.CharField(max_length=255, null=True, blank=True)
    location_employee = models.CharField(max_length=55, null=True, blank=True)
    phone = models.CharField(max_length=55, null=True, blank=True)
    tollfree = models.CharField(max_length=55, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    googleplus = models.CharField(max_length=500, null=True, blank=True)

    never_send_email = models.BooleanField(default=False, db_column="site_crawled")
    email_addresses = models.TextField(null=True, blank=True, verbose_name="keywords", help_text="We no longer use this field to store emails, we use it to store keywords crawled")
    valid_emails = models.CharField(max_length=255, null=True, blank=True)
    email_sent = models.BooleanField(default=False)
    has_crawled = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)


    department = models.CharField(max_length=55, default="labscience_private", help_text="Please use labscience, flashlights or batterycharger")


    immported_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        abstract = True


    def __str__(self):
        return u"%s-%s-%s" % (self.company_name, self.city, self.state)

    def __unicode__(self):
        return u"%s-%s-%s" % (self.company_name, self.city, self.state)

    def crawl_email(self,limit):
        from ecomstore.utils.email_extractor import get_emails
        if self.website:
            emails = get_emails(self.website, limit)
            self.email_addresses = ''
            gabage = 0
            for e in emails:
                val = e.split("@",1)[1]
                if '.' not in val:
                    gabage += 1
                    continue
                self.email_addresses += e + ','
            self.has_crawled = True
            self.save()
            return " Actual depth = " + emails[0] + ", " + str(len(emails) - gabage) + " emails found"
        else:
            return "This company does not provide a web site URL"

    def crawl_water_sites(self,limit):
        from ecomstore.utils.email_extractor import get_water_sites
        if self.website:
            emails = get_water_sites(self.website, limit)
            self.email_addresses = ''
            gabage = 0
            for e in emails:
                #val = e.split("@",1)[1]
                #if '.' not in val:
                #    gabage += 1
                #    continue
                self.email_addresses += e + ','
            self.has_crawled = True
            self.save()
            return "Crawled"
        else:
            return "This company does not provide a web site URL"


class ReferenceUSAData(ReferenceUSADataBase):
    class Meta:
        verbose_name = 'US Companies For Lab & Science'
        verbose_name_plural = 'US Companies For Lab & Science'
        db_table = 'referenceusa'
        ordering = ['company_name']

class ReferenceUSAData_4_Flashlights(ReferenceUSADataBase):
    class Meta:
        verbose_name = 'US Companies For Flashlights'
        verbose_name_plural = 'US Companies For Flashlights'
        db_table = 'referenceusa4flashlights'
        ordering = ['company_name']



class StateCounty(models.Model):
    """
    This table now holds all the emails from the paypal, the newsletter subscription and the orders
    """
    state = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    urls = models.CharField(max_length=1000, null=True, blank=True)
    address = models.CharField(max_length=1000, null=True, blank=True)
    phone = models.CharField(max_length=55, null=True, blank=True)
    email_addresses = models.CharField(max_length=1000, null=True, blank=True)
    email_sent = models.BooleanField(default=False)
    mail_sent = models.BooleanField(default=False)
    letter = models.FileField(upload_to='referenceusa/',blank=True)

    note = RichTextField(blank=True)

    class Meta:
        abstract = True


    def __str__(self):
        return u"%s-%s" % (self.state, self.county)

    def __unicode__(self):
        return u"%s-%s" % (self.state, self.county)


class StateCounty4Labs(StateCounty):
    class Meta:
        verbose_name = 'States & Counties For Lab'
        verbose_name_plural = 'States & Counties For Lab'
        db_table = 'statecounty4lab'
        ordering = ['state']

class StateCounty4Flashlights(StateCounty):
    class Meta:
        verbose_name = 'States & Counties For Flashlights'
        verbose_name_plural = 'States & Counties For Flashlights'
        db_table = 'statecounty4flashlights'
        ordering = ['state']


class LexisNexisBase(models.Model):
    """
    This table now holds all the emails from the paypal, the newsletter subscription and the orders
    """
    company_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    function = models.CharField(max_length=50, null=True, blank=True)
    specialty = models.CharField(max_length=50, null=True, blank=True)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    telephone_number_1 = models.CharField(max_length=20, null=True, blank=True)
    telephone_number_2 = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.CharField(max_length=100, unique=True)
    no_of_employees = models.CharField(max_length=20, null=True, blank=True)
    primary_sic_code = models.CharField(max_length=255, null=True, blank=True)
    primary_naics_code = models.CharField(max_length=255, null=True, blank=True)
    business_description = models.CharField(max_length=255, null=True, blank=True)

    never_send_email = models.BooleanField(default=False)
    email_sent = models.BooleanField(default=False)

    department = models.CharField(max_length=55, default="labscience_private", help_text="Please use labscience, flashlights or batterycharger")


    immported_at = models.DateTimeField(auto_now=True, null=True, blank=True)


    class Meta:
        abstract = True


    def __str__(self):
        return self.email_address

    def __unicode__(self):
        return self.email_address


class LexisNexisLabScience(LexisNexisBase):
    class Meta:
        verbose_name = 'LexisNexis Companies For Lab & Science'
        verbose_name_plural = 'LexisNexis For Lab & Science'
        db_table = 'lexisnexis4labscience'
        ordering = ['company_name']

class LexisNexisFlashlights(LexisNexisBase):
    class Meta:
        verbose_name = 'LexisNexis For Flashlights'
        verbose_name_plural = 'LexisNexis Companies For Flashlights'
        db_table = 'lexisnexis4flashlights'
        ordering = ['company_name']
