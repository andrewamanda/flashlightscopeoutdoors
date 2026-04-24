from django.db import models
from django.contrib import admin
from tinymce.widgets import TinyMCE
from ecomstore.newsletter.models import *
from django.http import HttpResponse
from datetime import datetime, timedelta, date
import csv
import copy
from ckeditor.widgets import CKEditorWidget
from tinymce.widgets import TinyMCE
from ecomstore.catalog.models import RichTextField
from ckeditor.widgets import CKEditorWidget

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None, header=True):

    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        field_names = set([field.name for field in opts.fields])
        if fields:
            fieldset = set(fields)
            field_names = field_names & fieldset
        elif exclude:
            excludeset = set(exclude)
            field_names = field_names - excludeset

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')

        writer = csv.writer(response)
        if header:
            writer.writerow(list(field_names))
        for obj in queryset:
            writer.writerow([unicode(getattr(obj, field)).encode("utf-8","replace") for field in field_names])
        return response
    export_as_csv.short_description = description
    return export_as_csv


class ProductsToIncludeInline(admin.StackedInline):
    model = ProductsToInclude
    extra = 0
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass


class EventsToAnnounceInline(admin.TabularInline):
    model = EventsToAnnounce
    extra = 0

class NewClearanceToAnnounceInline(admin.TabularInline):
    model = NewClearanceToAnnounce
    extra = 0

class ConfigNewsletterAdmin(admin.ModelAdmin):
    list_display = ('id','sender_name','subject','sender_test_name','subject_test')
    list_editable = ('sender_name','subject','sender_test_name','subject_test')

class UnsubscribeTextAdmin(admin.ModelAdmin):
    list_display = ('id','text',)
    list_editable = ('text',)
    max_num = 1
    pass


class NewsLetterPageAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('title','date', 'sent','sent_test','send_unsubscribe_text')
    list_editable = ('sent','sent_test','send_unsubscribe_text',)
    inlines = [ProductsToIncludeInline, EventsToAnnounceInline, NewClearanceToAnnounceInline,]
    date_hierarchy = 'date'
    formfield_overrides = {
        #models.TextField: { 'widget': TinyMCE() },
        models.TextField: { 'widget': CKEditorWidget() },
        }
    pass

    actions = ['duplicate_newsletter',]
    def get_actions(self, request):
        actions = super(NewsLetterPageAdmin, self).get_actions(request)
        return actions

    def duplicate_newsletter(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd_copy = copy.copy(sd) # (2) django copy object
            sd_copy.id = None   # (3) set 'id' to None to create new object
            sd_copy.title = "xxx"   # (3) set 'id' to None to create new object
            sd_copy.sent = False
            sd_copy.sent_test = False

            sd_copy.save()    # initial save

    duplicate_newsletter.short_description = "Duplicate a newsletter"



    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce.js',
            '/static/js/tiny_mce/tiny_mce_popup.js',
            '/static/js/tiny_mce/tiny_mce_src.js',
            '/static/js/tiny_mce/utils/editable_selects.js',
            '/static/js/tiny_mce/utils/form_utils.js',
            '/static/js/tiny_mce/utils/mctabs.js',
            '/static/js/tiny_mce/utils/validate.js',
            '/static/js/django_tinymce/init_tinymce.js',
            '/static/js/admin_pages.js'
        )

class NewsLetterUserAdmin(admin.ModelAdmin):
    list_display = ('mail',)
    actions = [export_as_csv_action("CSV Export", fields=['mail'])]
    pass

"""
class NewsLetterTestUserAdmin(admin.ModelAdmin):
    list_display = ('test_mail',)
    actions = [export_as_csv_action("CSV Export", fields=['test_mail'])]
    pass
"""
class NewsLetterUserAdmin(admin.ModelAdmin):
    list_display = ('email','name','imported_at')
    search_fields = ('email','name')
    ordering = ['email']
    list_per_page = 1000
    actions = [export_as_csv_action("CSV Export", fields=['email'])]


class NewsLetterTestUserAdmin(admin.ModelAdmin):
    list_display = ('email','name','imported_at')
    search_fields = ('email',)
    ordering = ['email']
    actions = [export_as_csv_action("CSV Export", fields=['email','name'])]

from import_export import resources
from ecomstore.newsletter.models import NewsLetterUser

from import_export.admin import ImportExportModelAdmin



class NewsLetterUserResource(resources.ModelResource):

    class Meta:
        model = NewsLetterUser
        fields = ('name', 'email','imported_at',)
        import_id_fields = ['email']

class NewsLetterUserExportImportAdmin(ImportExportModelAdmin):
    list_display = ('email','name','imported_at')
    search_fields = ('email','name')
    ordering = ['email']
    actions = [export_as_csv_action("CSV Export", fields=['email'])]
    resource_class = NewsLetterUserResource
    pass

class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email','name','interestedProducts', 'created_at')
    search_fields = ('email',)
    ordering = ['email']

admin.site.register(EmailSubscription, EmailSubscriptionAdmin)

class EmailSubscription_ExcludedAdmin(admin.ModelAdmin):
    list_display = ('email','name','why','created_at')
    search_fields = ('email',)
    ordering = ['email']

class EmailSubscription_ExcludedResource(resources.ModelResource):
    class Meta:
            model = EmailSubscription_Excluded
            fields =('id', 'name', 'email', 'why', 'created_at',)
            import_id_fields = ['email']

class EmailSubscription_ExcludedImportExportAdmin(ImportExportModelAdmin):
    list_display = ('email','name','why','created_at')
    search_fields = ('email',)
    ordering = ['email']

    resource_class = EmailSubscription_ExcludedResource
    pass

admin.site.register(EmailSubscription_Excluded, EmailSubscription_ExcludedImportExportAdmin)

admin.site.register(NewsLetterPage, NewsLetterPageAdmin)
admin.site.register(NewsLetterUser, NewsLetterUserExportImportAdmin)
#admin.site.register(NewsLetterUser, NewsLetterUserAdmin)
admin.site.register(NewsLetterTestUser, NewsLetterTestUserAdmin)
admin.site.register(UnsubscribeText, UnsubscribeTextAdmin)
admin.site.register(ConfigNewsletter, ConfigNewsletterAdmin)


class NewsLetter4ReferenceUSAAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('title','date', 'sent','sent_test','target_industry')
    list_editable = ('sent','sent_test',)
    date_hierarchy = 'date'
    formfield_overrides = {
        #models.TextField: { 'widget': TinyMCE() },
        models.TextField: { 'widget': CKEditorWidget() },
        }
    pass

    actions = ['duplicate_newsletter',]
    def get_actions(self, request):
        actions = super(NewsLetter4ReferenceUSAAdmin, self).get_actions(request)
        return actions

    def duplicate_newsletter(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd_copy = copy.copy(sd) # (2) django copy object
            sd_copy.id = None   # (3) set 'id' to None to create new object
            sd_copy.title = "xxx"   # (3) set 'id' to None to create new object
            sd_copy.sent = False
            sd_copy.sent_test = False

            sd_copy.save()    # initial save

    duplicate_newsletter.short_description = "Duplicate a newsletter"



    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce.js',
            '/static/js/tiny_mce/tiny_mce_popup.js',
            '/static/js/tiny_mce/tiny_mce_src.js',
            '/static/js/tiny_mce/utils/editable_selects.js',
            '/static/js/tiny_mce/utils/form_utils.js',
            '/static/js/tiny_mce/utils/mctabs.js',
            '/static/js/tiny_mce/utils/validate.js',
            '/static/js/django_tinymce/init_tinymce.js',
            '/static/js/admin_pages.js'
        )
admin.site.register(NewsLetter4ReferenceUSA, NewsLetter4ReferenceUSAAdmin)

class NewsLetter4LexisNexisAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('title','date', 'sent','sent_test','target_industry')
    list_editable = ('sent','sent_test',)
    date_hierarchy = 'date'
    formfield_overrides = {
        #models.TextField: { 'widget': TinyMCE() },
        models.TextField: { 'widget': CKEditorWidget() },
        }
    pass

    actions = ['duplicate_newsletter',]
    def get_actions(self, request):
        actions = super(NewsLetter4LexisNexisAdmin, self).get_actions(request)
        return actions

    def duplicate_newsletter(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd_copy = copy.copy(sd) # (2) django copy object
            sd_copy.id = None   # (3) set 'id' to None to create new object
            sd_copy.title = "xxx"   # (3) set 'id' to None to create new object
            sd_copy.sent = False
            sd_copy.sent_test = False

            sd_copy.save()    # initial save

    duplicate_newsletter.short_description = "Duplicate a newsletter"



    class Media:
        js = (
            '/static/js/tiny_mce/tiny_mce.js',
            '/static/js/tiny_mce/tiny_mce_popup.js',
            '/static/js/tiny_mce/tiny_mce_src.js',
            '/static/js/tiny_mce/utils/editable_selects.js',
            '/static/js/tiny_mce/utils/form_utils.js',
            '/static/js/tiny_mce/utils/mctabs.js',
            '/static/js/tiny_mce/utils/validate.js',
            '/static/js/django_tinymce/init_tinymce.js',
            '/static/js/admin_pages.js'
        )
admin.site.register(NewsLetter4LexisNexis, NewsLetter4LexisNexisAdmin)
