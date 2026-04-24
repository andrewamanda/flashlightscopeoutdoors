from django.db import models
from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.http import HttpResponse
from datetime import datetime, timedelta, date
import csv
import copy
from ckeditor.widgets import CKEditorWidget
from tinymce.widgets import TinyMCE
from ecomstore.catalog.models import RichTextField

from import_export import resources, fields
from ecomstore.referenceusa.models import *
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from ecomstore.newsletter.models import *
import re
#import dns.resolver


class ReferenceUSADataResource(resources.ModelResource):

    company_name = fields.Field(column_name='Company Name', attribute='company_name')
    website = fields.Field(column_name='Website', attribute='website')
    executive_name = fields.Field(column_name='Executive Name', attribute='executive_name')
    address = fields.Field(column_name='Address', attribute='address')
    city = fields.Field(column_name='City', attribute='city')
    state = fields.Field(column_name='State', attribute='state')
    zip = fields.Field(column_name='ZIP Code', attribute='zip')
    primary_sic_code = fields.Field(column_name='Primary SIC Code', attribute='primary_sic_code')
    primary_sic_description = fields.Field(column_name='Primary SIC Description', attribute='primary_sic_description')
    sic_code_1 = fields.Field(column_name='SIC Code 1', attribute='sic_code_1')
    sic_code_1_description = fields.Field(column_name='SIC Code 1 Description', attribute='sic_code_1_description')
    sic_code_2 = fields.Field(column_name='SIC Code 2', attribute='sic_code_2')
    sic_code_2_description = fields.Field(column_name='SIC Code 2 Description', attribute='sic_code_2_description')
    sic_code_3 = fields.Field(column_name='SIC Code 3', attribute='sic_code_3')
    sic_code_3_description = fields.Field(column_name='SIC Code 3 Description', attribute='sic_code_3_description')
    sic_code_4 = fields.Field(column_name='SIC Code 4', attribute='sic_code_4')
    sic_code_4_description = fields.Field(column_name='SIC Code 4 Description', attribute='sic_code_4_description')
    sic_code_5 = fields.Field(column_name='SIC Code 5', attribute='sic_code_5')
    sic_code_5_description = fields.Field(column_name='SIC Code 5 Description', attribute='sic_code_5_description')
    primary_naics_code = fields.Field(column_name='Primary NAICS', attribute='primary_naics_code')
    primary_naics_description = fields.Field(column_name='Primary NAICS Description', attribute='primary_naics_description')
    naics_code_1 = fields.Field(column_name='NAICS 1', attribute='naics_code_1')
    naics_1_description = fields.Field(column_name='NAICS 1 Description', attribute='naics_1_description')
    naics_code_2 = fields.Field(column_name='NAICS 2', attribute='naics_code_2')
    naics_2_description = fields.Field(column_name='NAICS 2 Description', attribute='naics_2_description')
    naics_code_3 = fields.Field(column_name='NAICS 3', attribute='naics_code_2')
    naics_3_description = fields.Field(column_name='NAICS 3 Description', attribute='naics_2_description')
    naics_code_4 = fields.Field(column_name='NAICS 4', attribute='naics_code_2')
    naics_4_description = fields.Field(column_name='NAICS 4 Description', attribute='naics_2_description')
    naics_code_5 = fields.Field(column_name='NAICS 5', attribute='naics_code_2')
    naics_5_description = fields.Field(column_name='NAICS 5 Description', attribute='naics_2_description')
    location_employee = fields.Field(column_name='Location Employee Size Range', attribute='location_employee')
    googleplus = fields.Field(column_name='Google Plus', attribute='googleplus')
    twitter = fields.Field(column_name='Twitter', attribute='twitter')
    linkedin = fields.Field(column_name='Linked-In', attribute='linkedin')
    facebook = fields.Field(column_name='Facebook', attribute='facebook')
    department = fields.Field(column_name='Department', attribute='department')
    phone = fields.Field(column_name='Phone Number Combined', attribute='phone')
    tollfree = fields.Field(column_name='Toll Free Number Combined', attribute='tollfree')


    class Meta:
        model = ReferenceUSAData
        import_id_fields = (b'company_name',b'state',b'city',)
        export_order = ('company_name', 'address', 'city', 'state', 'zip')

class ReferenceUSADataExportImportAdmin(ImportExportModelAdmin):
    list_display = ('company_name','is_important','website','view_on_site', 'valid_emails','email_addresses','state','has_crawled', 'never_send_email','immported_at','email_sent','phone','tollfree')
    search_fields = ('company_name','website', 'email_addresses')
    list_filter = ('email_sent','has_crawled','never_send_email','department','is_important','primary_sic_description','primary_naics_description')
    list_editable = ('email_sent','never_send_email','website', 'valid_emails','is_important', 'has_crawled')
    ordering = ['immported_at']
    actions = ['email_crawl', 'water_site_crawl', 'export_4_mailers', 'send_email']
    resource_class = ReferenceUSADataResource
    fieldsets = (
                  ('Basics', {'fields': ('company_name', 'executive_name','website','department',('email_sent','never_send_email','has_crawled'),'is_important','email_addresses',)}),
                  ('Contact Info', {'fields': ('address','city','state','zip','phone','tollfree','valid_emails'),}),
                  ('Social Media', {'fields': ('twitter','linkedin','facebook','googleplus',),}),
                  ('SIC', {'fields': (('primary_sic_code','primary_sic_description',),('sic_code_1','sic_code_1_description',),('sic_code_2','sic_code_2_description',),('sic_code_3','sic_code_3_description',),('sic_code_4','sic_code_4_description',),('sic_code_5','sic_code_5_description',),)}),
                  ('NAIC', {'fields': (('primary_naics_code','primary_naics_description',),('naics_code_1','naics_1_description',),('naics_code_2','naics_2_description',),('naics_code_3','naics_3_description',),('naics_code_4','naics_4_description',),('naics_code_5','naics_5_description',),)}),
                )

    pass

    def get_actions(self, request):
        actions = super(ReferenceUSADataExportImportAdmin, self).get_actions(request)
        return actions

    def email_crawl(self, request, queryset):
        depth = 50

        queryset = ReferenceUSAData.objects.all().filter(has_crawled = False, website__isnull = False)
        for obj in queryset:
            if obj.has_crawled:
                continue
            retStatus = obj.crawl_email(depth)
            self.message_user(request, obj.company_name + ":" + retStatus)
        #print "Finished crawling all {} companies".format(len(queryset))

    email_crawl.short_description = "Crawl for emails"

    def water_site_crawl(self, request, queryset):
        depth = 50

        queryset = ReferenceUSAData.objects.all().filter(website__isnull = False)
        for obj in queryset:
            if obj.has_crawled:
                continue
            retStatus = obj.crawl_water_sites(depth)
            self.message_user(request, obj.company_name + ":" + retStatus)
        #print "Finished crawling all {} companies".format(len(queryset))

    water_site_crawl.short_description = "Crawl for water sites"


    def export_4_mailers(self, request, queryset):
        queryset = ReferenceUSAData.objects.all().filter(has_crawled = False)
        for obj in queryset:
            if obj.has_crawled:
                continue
            obj.has_crawled = True
            obj.save()
        #print "Finished crawling all {} companies".format(len(queryset))

    export_4_mailers.short_description = "Mark Entry As Crawled For Mailers"

    def send_email(self, request, queryset):
        for obj in queryset:
            if obj.valid_emails:
                newsletterO = NewsLetter4ReferenceUSA.objects.filter(target_industry='labscience').first()
                msg = newsletterO.body
                msg = '<html><head></head><body>' + msg + '</body></html>'
                fq_sender = "Ecosphere Technologies<sales@eco-sensa.com>"
                replyto = "sales@eco-sensa.com"
                #fq_sender = "Andrew & Amanda Outdoors<sales@andrew-amanda.com>"
                #replyto = "sales@andrew-amanda.com"

                sub = "Your best source for water testing & sampling bottles"

                #print "msg = ", msg

                emails = obj.valid_emails.split(',')
                emails = list(set(emails))
                for email in emails:
                    #match = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

                    #if match == None:
                    #    print('Bad Syntax in ' + email)
                    #    continue

                    if "@" not in email:
                        logging.error("Email %s not valid", str(email))
                        continue
                    logging.error("Sending newsletter to %s", str(email))

                    try:
                        username = str(obj.company_name)
                    except Exception as e:
                        logging.error("In Exc getting user name, error %s", e)
                        username = None
                    subject = sub
                    EmailMsg = EmailMessage(subject,msg,fq_sender,[str(email)],headers={'Reply-To':replyto})
                    EmailMsg.content_subtype = "html"
                    try:
                        # this call starts to create html tags in the content after django1.11
                        #EmailMsg.send()

                        from django.core.mail import EmailMultiAlternatives
                        text_content = subject
                        eMultiAlternative = EmailMultiAlternatives(subject, text_content, fq_sender, [str(email)])
                        eMultiAlternative.attach_alternative(msg, "text/html")
                        eMultiAlternative.send()
                    except Exception as e:
                        logging.error("In Exc sending mail to %s -- Error: %s", email, e)

                    self.message_user(request, "Sent email to " + obj.valid_emails)

    send_email.short_description = "Send email"


    def view_on_site(self, obj):
	#print "obj.website = ", obj.website
        return format_html("<a target='_blank' href='http://{url}'>View</a>", url=obj.website)
    view_on_site.allow_tags = True
    view_on_site.short_description = "View On Site"

admin.site.register(ReferenceUSAData, ReferenceUSADataExportImportAdmin)





class ReferenceUSAData4FlashlightsResource(resources.ModelResource):

    company_name = fields.Field(column_name='Company Name', attribute='company_name')
    website = fields.Field(column_name='Website', attribute='website')
    address = fields.Field(column_name='Address', attribute='address')
    city = fields.Field(column_name='City', attribute='city')
    state = fields.Field(column_name='State', attribute='state')
    zip = fields.Field(column_name='ZIP Code', attribute='zip')
    primary_sic_code = fields.Field(column_name='Primary SIC Code', attribute='primary_sic_code')
    primary_sic_description = fields.Field(column_name='Primary SIC Description', attribute='primary_sic_description')
    sic_code_1 = fields.Field(column_name='SIC Code 1', attribute='sic_code_1')
    sic_code_1_description = fields.Field(column_name='SIC Code 1 Description', attribute='sic_code_1_description')
    sic_code_2 = fields.Field(column_name='SIC Code 2', attribute='sic_code_2')
    sic_code_2_description = fields.Field(column_name='SIC Code 2 Description', attribute='sic_code_2_description')
    sic_code_3 = fields.Field(column_name='SIC Code 3', attribute='sic_code_3')
    sic_code_3_description = fields.Field(column_name='SIC Code 3 Description', attribute='sic_code_3_description')
    sic_code_4 = fields.Field(column_name='SIC Code 4', attribute='sic_code_4')
    sic_code_4_description = fields.Field(column_name='SIC Code 4 Description', attribute='sic_code_4_description')
    sic_code_5 = fields.Field(column_name='SIC Code 5', attribute='sic_code_5')
    sic_code_5_description = fields.Field(column_name='SIC Code 5 Description', attribute='sic_code_5_description')
    primary_naics_code = fields.Field(column_name='Primary NAICS', attribute='primary_naics_code')
    primary_naics_description = fields.Field(column_name='Primary NAICS Description', attribute='primary_naics_description')
    naics_code_1 = fields.Field(column_name='NAICS 1', attribute='naics_code_1')
    naics_1_description = fields.Field(column_name='NAICS 1 Description', attribute='naics_1_description')
    naics_code_2 = fields.Field(column_name='NAICS 2', attribute='naics_code_2')
    naics_2_description = fields.Field(column_name='NAICS 2 Description', attribute='naics_2_description')
    naics_code_3 = fields.Field(column_name='NAICS 3', attribute='naics_code_2')
    naics_3_description = fields.Field(column_name='NAICS 3 Description', attribute='naics_2_description')
    naics_code_4 = fields.Field(column_name='NAICS 4', attribute='naics_code_2')
    naics_4_description = fields.Field(column_name='NAICS 4 Description', attribute='naics_2_description')
    naics_code_5 = fields.Field(column_name='NAICS 5', attribute='naics_code_2')
    naics_5_description = fields.Field(column_name='NAICS 5 Description', attribute='naics_2_description')
    location_employee = fields.Field(column_name='Location Employee Size Range', attribute='location_employee')
    googleplus = fields.Field(column_name='Google Plus', attribute='googleplus')
    twitter = fields.Field(column_name='Twitter', attribute='twitter')
    linkedin = fields.Field(column_name='Linked-In', attribute='linkedin')
    facebook = fields.Field(column_name='Facebook', attribute='facebook')
    department = fields.Field(column_name='Department', attribute='department')
    phone = fields.Field(column_name='Phone Number Combined', attribute='phone')
    tollfree = fields.Field(column_name='Toll Free Number Combined', attribute='tollfree')


    class Meta:
        model = ReferenceUSAData_4_Flashlights
        import_id_fields = (b'company_name',b'state',b'city',)

class ReferenceUSAData4FlashlightsExportImportAdmin(ImportExportModelAdmin):
    list_display = ('company_name','is_important','website','state','has_crawled', 'never_send_email','immported_at','email_sent', 'email_addresses','phone','tollfree')
    search_fields = ('company_name','website', 'email_addresses')
    list_filter = ('email_sent','has_crawled','never_send_email','department','is_important','primary_sic_description','primary_naics_description')
    list_editable = ('email_sent','never_send_email','website', 'is_important')
    ordering = ['immported_at']
    actions = ['email_crawl']
    resource_class = ReferenceUSAData4FlashlightsResource
    pass

    def get_actions(self, request):
        actions = super(ReferenceUSAData4FlashlightsExportImportAdmin, self).get_actions(request)
        return actions

    def email_crawl(self, request, queryset):
        depth = 50

        queryset = ReferenceUSAData_4_Flashlights.objects.all().filter(has_crawled = False, website__isnull = False)
        for obj in queryset:
            if obj.has_crawled:
                continue
            retStatus = obj.crawl_email(depth)
            self.message_user(request, obj.company_name + ":" + retStatus)
        #print "Finished crawling all {} companies".format(len(queryset))


    email_crawl.short_description = "Crawl for emails"

admin.site.register(ReferenceUSAData_4_Flashlights, ReferenceUSAData4FlashlightsExportImportAdmin)



class StateCounty4LabsResource(resources.ModelResource):

    state = fields.Field(column_name='state', attribute='state')
    county = fields.Field(column_name='county', attribute='county')


    class Meta:
        model = StateCounty4Labs
        import_id_fields = (b'county',b'state',)

class StateCounty4LabsExportImportAdmin(ImportExportModelAdmin):
    list_display = ('county','state','urls','email_addresses','email_sent', 'phone','mail_sent','address')
    search_fields = ('county','email_addresses',)
    list_filter = ('state','email_sent','mail_sent',)
    list_editable = ('urls','address','phone', 'email_addresses', 'email_sent','mail_sent',)
    ordering = ['state']
    resource_class = StateCounty4LabsResource

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass


admin.site.register(StateCounty4Labs, StateCounty4LabsExportImportAdmin)

class StateCounty4FlashlightsResource(resources.ModelResource):

    state = fields.Field(column_name='state', attribute='state')
    county = fields.Field(column_name='county', attribute='county')


    class Meta:
        model = StateCounty4Flashlights
        import_id_fields = (b'county',b'state',)


class StateCounty4FlashlightsExportImportAdmin(ImportExportModelAdmin):
    list_display = ('county','state','urls','email_addresses','email_sent', 'phone','mail_sent','address')
    search_fields = ('county','email_addresses',)
    list_filter = ('state','email_sent','mail_sent',)
    list_editable = ('urls','address','phone', 'email_addresses', 'email_sent','mail_sent',)
    ordering = ['state']
    resource_class = StateCounty4FlashlightsResource
    pass


admin.site.register(StateCounty4Flashlights, StateCounty4FlashlightsExportImportAdmin)



class LexisNexisLabScienceResource(resources.ModelResource):

    company_name = fields.Field(column_name='Company Name', attribute='company_name')
    first_name = fields.Field(column_name='First name', attribute='first_name')
    last_name = fields.Field(column_name='Last name', attribute='last_name')
    title = fields.Field(column_name='Title', attribute='title')
    function = fields.Field(column_name='Function', attribute='function')
    specialty = fields.Field(column_name='Specialty', attribute='specialty')
    street_address = fields.Field(column_name='Street Address', attribute='street_address')
    city = fields.Field(column_name='City', attribute='city')
    state = fields.Field(column_name='State/Province', attribute='state')
    zip_code = fields.Field(column_name='ZIP Code', attribute='zip_code')
    country = fields.Field(column_name='Country', attribute='country')
    telephone_number_1 = fields.Field(column_name='Telephone Number 1', attribute='telephone_number_1')
    telephone_number_2 = fields.Field(column_name='Telephone Number 2', attribute='telephone_number_2')
    email_address = fields.Field(column_name='Email Address', attribute='email_address')
    no_of_employees = fields.Field(column_name='No. of Employees', attribute='no_of_employees')
    primary_sic_code = fields.Field(column_name='Primary SIC Code', attribute='primary_sic_code')
    primary_naics_code = fields.Field(column_name='Primary NAICS Code', attribute='primary_naics_code')
    business_description = fields.Field(column_name='Business Description', attribute='business_description')

    class Meta:
        model = LexisNexisLabScience
        import_id_fields = (b'email_address',)
        export_order = ('company_name', 'street_address', 'city', 'state', 'zip_code')

class LexisNexisLabScienceExportImportAdmin(ImportExportModelAdmin):
    list_display = ('company_name','email_address','state','country', 'never_send_email','immported_at','email_sent',)
    search_fields = ('company_name','email_address')
    list_filter = ('email_sent','never_send_email','department','primary_sic_code','primary_naics_code')
    list_editable = ('email_address','email_sent','never_send_email',)
    ordering = ['immported_at']
    actions = ['send_email']
    resource_class = LexisNexisLabScienceResource
    list_per_page = 500


    pass

    def get_actions(self, request):
        actions = super(LexisNexisLabScienceExportImportAdmin, self).get_actions(request)
        return actions

    def send_email(self, request, queryset):
        count = 0
        for obj in queryset:
            if obj.email_address and not obj.email_sent:
                newsletterO = NewsLetter4LexisNexis.objects.filter(target_industry='labscience').first()
                msg = newsletterO.body
                msg = '<html><head></head><body>' + msg + '</body></html>'
                fq_sender = "Ecosphere Technologies<info@eco-sensa.com>"
                replyto = "info@eco-sensa.com"
                #fq_sender = "Andrew & Amanda Outdoors<sales@andrew-amanda.com>"
                #replyto = "sales@andrew-amanda.com"

                sub = "Your best source for coliform water testing bottles"

                #print "msg = ", msg

                emails = obj.email_address.split(',')
                emails = list(set(emails))
                for email in emails:
                    #match = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

                    #if match == None:
                    #    print('Bad Syntax in ' + email)
                    #    continue

                    if "@" not in email:
                        logging.error("Email %s not valid", str(email))
                        continue
                    #logging.error("Sending newsletter to %s", str(email))

                    try:
                        username = str(obj.company_name)
                    except Exception as e:
                        logging.error("In Exc getting user name, error %s", e)
                        username = None
                    subject = sub
                    EmailMsg = EmailMessage(subject,msg,fq_sender,[str(email)],headers={'Reply-To':replyto})
                    EmailMsg.content_subtype = "html"
                    try:
                        # this call starts to create html tags in the content after django1.11
                        #EmailMsg.send()

                        from django.core.mail import EmailMultiAlternatives
                        text_content = subject
                        eMultiAlternative = EmailMultiAlternatives(subject, text_content, fq_sender, [str(email)])
                        eMultiAlternative.attach_alternative(msg, "text/html")
                        eMultiAlternative.send()
                        obj.email_sent = True
                        count = count + 1
                        obj.save()
                    except Exception as e:
                        logging.error("In Exc sending mail to %s -- Error: %s", email, e)

                    self.message_user(request, "Sent email to " + obj.email_address + ", count = " + str(count))

    send_email.short_description = "Send email"



admin.site.register(LexisNexisLabScience, LexisNexisLabScienceExportImportAdmin)

class LexisNexisFlashlightsResource(resources.ModelResource):

    company_name = fields.Field(column_name='Company Name', attribute='company_name')
    first_name = fields.Field(column_name='First name', attribute='first_name')
    last_name = fields.Field(column_name='Last name', attribute='last_name')
    title = fields.Field(column_name='Title', attribute='title')
    function = fields.Field(column_name='Function', attribute='function')
    specialty = fields.Field(column_name='Specialty', attribute='specialty')
    street_address = fields.Field(column_name='Street Address', attribute='street_address')
    city = fields.Field(column_name='City', attribute='city')
    state = fields.Field(column_name='State/Province', attribute='state')
    zip_code = fields.Field(column_name='ZIP Code', attribute='zip_code')
    country = fields.Field(column_name='Country', attribute='country')
    telephone_number_1 = fields.Field(column_name='Telephone Number 1', attribute='telephone_number_1')
    telephone_number_2 = fields.Field(column_name='Telephone Number 2', attribute='telephone_number_2')
    email_address = fields.Field(column_name='Email Address', attribute='email_address')
    no_of_employees = fields.Field(column_name='No. of Employees', attribute='no_of_employees')
    primary_sic_code = fields.Field(column_name='Primary SIC Code', attribute='primary_sic_code')
    primary_naics_code = fields.Field(column_name='Primary NAICS Code', attribute='primary_naics_code')
    business_description = fields.Field(column_name='Business Description', attribute='business_description')
    department = "flashlights"

    class Meta:
        model = LexisNexisFlashlights
        import_id_fields = (b'email_address',)
        export_order = ('company_name', 'street_address', 'city', 'state', 'zip_code')

class LexisNexisFlashlightsExportImportAdmin(ImportExportModelAdmin):
    list_display = ('company_name','email_address','state','country', 'never_send_email','immported_at','email_sent',)
    search_fields = ('company_name','email_address',)
    list_filter = ('email_sent','never_send_email','department','primary_sic_code','primary_naics_code')
    list_editable = ('email_address','email_sent','never_send_email',)
    ordering = ['immported_at']
    actions = ['send_email']
    resource_class = LexisNexisFlashlightsResource

    list_per_page = 500

    pass

    def get_actions(self, request):
        actions = super(LexisNexisFlashlightsExportImportAdmin, self).get_actions(request)
        return actions

    def send_email(self, request, queryset):
        count = 0
        for obj in queryset:
            if obj.email_address and not obj.email_sent:
                newsletterO = NewsLetter4LexisNexis.objects.filter(target_industry='flashlights').first()
                msg = newsletterO.body
                msg = '<html><head></head><body>' + msg + '</body></html>'
                fq_sender = "Andrew & Amanda Outdoors<info@andrewamanda.com>"
                replyto = "info@andrewamanda.com"
                #fq_sender = "Andrew & Amanda Outdoors<sales@andrew-amanda.com>"
                #replyto = "sales@andrew-amanda.com"

                sub = "LED Search & Rescue Flashlights, Tactical Flashlights & EDC Flashlights"

                #print "msg = ", msg

                emails = obj.email_address.split(',')
                emails = list(set(emails))
                for email in emails:
                    #match = re.match('^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,4})$', email)

                    #if match == None:
                    #    print('Bad Syntax in ' + email)
                    #    continue

                    if "@" not in email:
                        logging.error("Email %s not valid", str(email))
                        continue
                    #logging.error("Sending newsletter to %s", str(email))

                    try:
                        username = str(obj.company_name)
                    except Exception as e:
                        logging.error("In Exc getting user name, error %s", e)
                        username = None
                    subject = sub
                    EmailMsg = EmailMessage(subject,msg,fq_sender,[str(email)],headers={'Reply-To':replyto})
                    EmailMsg.content_subtype = "html"
                    try:
                        # this call starts to create html tags in the content after django1.11
                        #EmailMsg.send()

                        from django.core.mail import EmailMultiAlternatives
                        text_content = subject
                        eMultiAlternative = EmailMultiAlternatives(subject, text_content, fq_sender, [str(email)])
                        eMultiAlternative.attach_alternative(msg, "text/html")
                        eMultiAlternative.send()
                        obj.email_sent = True
                        count = count + 1
                        obj.save()
                    except Exception as e:
                        logging.error("In Exc sending mail to %s -- Error: %s", email, e)

                    self.message_user(request, "Sent email to " + obj.email_address + ", count = " + str(count))

    send_email.short_description = "Send email"



admin.site.register(LexisNexisFlashlights, LexisNexisFlashlightsExportImportAdmin)
