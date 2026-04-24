from django.contrib import admin
from ecomstore.heartwoodbeyond.models import *
from django_object_actions import DjangoObjectActions
from ckeditor.widgets import CKEditorWidget
from ecomstore.catalog.models import RichTextField
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from django.http import HttpResponse
import csv

class CorrespondenceEntryInline(admin.StackedInline):
    model = CorrespondenceEntry
    readonly_fields = ('customer_contact_date','customer_comment',)
    fieldsets = (
                 ('Customer Message', {'fields': (('customer_contact_date','subject',),('customer_comment','customer_attachment_1','customer_attachment_2',))}),
                 ('Our response', {'fields': (('admin_contact_date','has_response_been_sent',),('admin_comment','our_attachment_1','our_attachment_2',),)}),
                 )
    readonly_fields = ('has_response_been_sent',)

    extra = 0

class CustomerRelationshipAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('customer_name','email', 'is_business','phone', 'status', 'device', 'last_updated')
    list_per_page = 10
    list_filter = ('status','is_business',)
    ordering = ['-last_updated']
    search_fields = ['user__username', 'email', 'first_name', 'last_name', 'business_name',]
    actions = ['send_email',]
    readonly_fields = ('status',)

    #readonly_fields = ('last_offer','bin_price','sale_price','status','user_email',)

    fieldsets = (
                 ('Basics', {'fields': (('user','status',),('first_name','last_name','email','phone',),('address','city','state',),('is_current_customer','sign_up_for_newsletter',))}),
                 ('Is A Business ?', {'fields': ('is_business', ('business_type', 'business_name',))}),
                 ('Initial Message from the customer', {'fields': ('comments',)}),
                 )

    inlines = [CorrespondenceEntryInline, ]

    def customer_name(self, obj):
        try:
            return obj.first_name + " " + obj.last_name
        except:
            try:
                return obj.first_name
            except:
                return "Missing First Name"

    def send_email(self, request, obj):

        customer_email = obj.email
        seller_email = request.user.email
        cc_email = "sales@heartwoodandbeyond.com"
        replyto_email = obj.email
        recipient_list = []
        recipient_list.append(customer_email)
        recipient_list.append(seller_email)


        correspondencehistories = obj.correspondenceentry_set.all().order_by('-customer_contact_date')

        newmessage = False
        if len(correspondencehistories) == 1 and obj.status == 'WAIT4ADMIN':
            newmessage = True

        curr_message = correspondencehistories[0]

        files = []
        if curr_message.our_attachment_1:
            files.append(curr_message.our_attachment_1)
        if curr_message.our_attachment_2:
            files.append(curr_message.our_attachment_2)


        message = "From Customer:\t{} {}\temail: {} ".format(obj.first_name, obj.last_name, obj.email)

        message += "\n\nOur response: \t{}".format(curr_message.admin_comment)

        subject = curr_message.subject


        from django.contrib.sites.models import Site
        from django.utils.encoding import smart_str
        message += smart_str("\n\nPlease visit back our web store http://" + Site.objects.get_current().domain)

        #from django.core.mail import EmailMessage
        from ecomstore.utils.email import send_mail_with_attachment

        send_mail_with_attachment(subject, message, seller_email, replyto_email, recipient_list, files)
        curr_message.has_response_been_sent = True
        obj.save()


        self.message_user(request, "Response with the Subject {} sent to the customer".format(subject))




    change_actions = ('send_email',)

admin.site.register(CustomerRelationship, CustomerRelationshipAdmin)




class CallLogsInline(admin.StackedInline):
    model = CallLogs
    extra = 0
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
    }

class CustomerLeadResource(resources.ModelResource):

    customer_name = fields.Field(column_name='Customer', attribute='customer_name')
    company = fields.Field(column_name='Company', attribute='company')
    address = fields.Field(column_name='Street Address', attribute='address')
    city = fields.Field(column_name='City', attribute='city')
    state = fields.Field(column_name='State', attribute='state')
    country = fields.Field(column_name='Country', attribute='country')
    zip = fields.Field(column_name='Zip', attribute='zip')
    phone = fields.Field(column_name='Phone', attribute='phone')
    email = fields.Field(column_name='Email', attribute='email')
    business_type = fields.Field(column_name='Customer Type', attribute='business_type')
    open_balance = fields.Field(column_name='Open Balance', attribute='open_balance')
    notes = fields.Field(column_name='Notes', attribute='notes')


    class Meta:
        model = CustomerLead
        import_id_fields = ('customer_name','phone',)
        export_order = ('customer_name', 'address', 'city', 'state', 'zip')



class CustomerLeadExportImportAdmin(ImportExportModelAdmin):
    list_display = ('customer_name','email', 'is_business','phone', 'followup_required', 'date_to_follow','open_balance','last_updated')
    list_per_page = 10
    list_filter = ('followup_required','converted_to_orders','is_business','business_type',)
    ordering = ['-open_balance']
    search_fields = ['customer_name', 'email', 'company',]

    #readonly_fields = ('last_offer','bin_price','sale_price','status','user_email',)

    fieldsets = (
                 ('Lead Status', {'fields': ('followup_required','date_to_follow','converted_to_orders','open_balance')}),
                 ('Customer Information', {'fields': ('customer_name','email','phone','address','city','state','country','zip',)}),
                 ('Is the Customer A Business ?', {'fields': ('is_business', ('business_type', 'company',))}),
                 ('Internal Notes', {'fields': ('notes',)}),
                 )

    inlines = [CallLogsInline, ]
    resource_class = CustomerLeadResource
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
    }


admin.site.register(CustomerLead, CustomerLeadExportImportAdmin)


import csv
from io import StringIO

from django.http import StreamingHttpResponse


def keyset_pagination_iterator(input_queryset, batch_size=500):
    all_queryset = input_queryset.order_by("pk")
    last_pk = None
    while True:
        queryset = all_queryset
        if last_pk is not None:
            queryset = all_queryset.filter(pk__gt=last_pk)
        queryset = queryset[:batch_size]
        for row in queryset:
            last_pk = row.pk
            yield row
        if not queryset:
            break


def export_as_csv_action(description="Export selected rows to CSV"):
    def export_as_csv(modeladmin, request, queryset):
        def rows(queryset):

            csvfile = StringIO()
            csvwriter = csv.writer(csvfile)
            columns = [field.name for field in modeladmin.model._meta.fields]

            def read_and_flush():
                csvfile.seek(0)
                data = csvfile.read()
                csvfile.seek(0)
                csvfile.truncate()
                return data

            header = False

            if not header:
                header = True
                csvwriter.writerow(columns)
                yield read_and_flush()

            for row in keyset_pagination_iterator(queryset):
                if not row.email_sent:
                    csvwriter.writerow(getattr(row, column) for column in columns)
                    yield read_and_flush()
                    row.email_sent = True
                    row.save()

        response = StreamingHttpResponse(rows(queryset), content_type="text/csv")
        response["Content-Disposition"] = (
            "attachment; filename=%s.csv" % modeladmin.model.__name__
        )

        return response

    export_as_csv.short_description = description
    return export_as_csv


class LeadsPurchasedResource(resources.ModelResource):

    first_name = fields.Field(column_name='First Name', attribute='first_name')
    middle_name = fields.Field(column_name='Middle Name', attribute='middle_name')
    last_name = fields.Field(column_name='Last Name', attribute='last_name')
    executive_title = fields.Field(column_name='Executive Title', attribute='executive_title')

    company_name = fields.Field(column_name='Company Name', attribute='company_name')
    address_line_1 = fields.Field(column_name='Address Line 1', attribute='address_line_1')
    address_line_2 = fields.Field(column_name='Address Line 2', attribute='address_line_2')

    city = fields.Field(column_name='City', attribute='city')
    state = fields.Field(column_name='State Or Province', attribute='state')
    country = fields.Field(column_name='Country/Region', attribute='country')
    postal_code = fields.Field(column_name='Postal Code', attribute='postal_code')
    phone_number = fields.Field(column_name='Phone Number', attribute='phone_number')
    email_address = fields.Field(column_name='Email Address', attribute='email_address')
    url = fields.Field(column_name='URL', attribute='url')
    revenue = fields.Field(column_name='Revenue', attribute='revenue')
    employees_size = fields.Field(column_name='Employees Size', attribute='employees_size')
    industry = fields.Field(column_name='Industry', attribute='industry')

    class Meta:
        model = Leads_Purchased
        import_id_fields = ('email_address','phone_number',)




class LeadsPurchasedExportImportAdmin(ImportExportModelAdmin):
    list_display = ('company_name','email_sent','first_name','last_name','email_address','executive_title','phone_number', 'industry','city','state','address_line_1','address_line_2','postal_code','url','revenue','employees_size','last_updated','email_sent',)
    list_per_page = 1000
    list_filter = ('email_sent','industry','state',)
    list_editable = ('first_name','last_name','email_address','email_sent',)
    ordering = ['-first_name','-last_name']
    search_fields = ['first_name', 'last_name', 'phone_number', 'email_address', 'company_name',]
    actions = [export_as_csv_action("Export selected and at most 500 leads, mark as email sent"),]

    resource_class = LeadsPurchasedResource
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
    }


admin.site.register(Leads_Purchased, LeadsPurchasedExportImportAdmin)


class Reclaimed_BlogAdmin(admin.ModelAdmin):
    list_display = ('name','last_updated','ready_to_publish','ranking')
    list_display_links = ('name',)
    list_filter = ('ready_to_publish',)
    list_editable = ('ready_to_publish','ranking',)

    list_per_page = 20
    ordering = ['last_updated']
    search_fields = ['name', ]

    fieldsets = (
                 ('Required', {'fields': (('ready_to_publish','ranking'), ('name','slug',),('content'))}),
                 ('Optional', {'fields': ('title','subtitle','summary',)}),
                 )


    prepopulated_fields = {'slug' : ('name',),}

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
    }
    class Meta:
        model = Reclaimed_Blog

admin.site.register(Reclaimed_Blog, Reclaimed_BlogAdmin)
