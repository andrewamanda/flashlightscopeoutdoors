from django.contrib import admin
from ecomstore.RMA.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from ckeditor.widgets import CKEditorWidget
from ecomstore.catalog.models import RichTextField
from django.http import HttpResponse
import copy

from .forms import *

from datetime import date

class Actions_TakenInline(admin.TabularInline):
    model = actions_taken
    form = ActionsTakenForm
    #form = AdditionalImagesForm  # Use the custom form that allows multiple image uploads
    extra = 0  # Don't display any empty forms by default
    show_change_link = True  # Allow editing existing images
    verbose_name_plural = "Actions Taken"

    fields = ('last_updated','a_image', 'image_thumbnail', 'image_caption', 'return_authorization')  # Fields to display
    readonly_fields = ('image_thumbnail',)  # Make thumbnail and dimensions read-only

    # 1. Display the thumbnail with hover effect for the full-size image
    def image_thumbnail(self, obj):
        if obj.a_image:
            return format_html(
                """
                <style>
                    .thumbnail-wrapper {{
                        position: relative;
                        display: inline-block;
                    }}
                    .thumbnail-wrapper img {{
                        cursor: pointer;
                    }}
                    .thumbnail-wrapper .hover-image {{
                        display: none;
                        position: absolute;
                        top: 0;
                        right: 110%; /* Move to the left by adjusting the right position */
                        z-index: 1;
                        border: 1px solid #ddd;
                    }}
                    .thumbnail-wrapper:hover .hover-image {{
                        display: block;
                    }}
                </style>
                <div class="thumbnail-wrapper">
                    <img src="{}" height="100" />
                    <div class="hover-image">
                        <img src="{}" style="max-width: 400px;" /> <!-- Display at original size -->
                    </div>
                </div>
                """,
                obj.a_image.url, obj.a_image.url
            )
        return "No Image"

    image_thumbnail.short_description = 'Thumbnail'  # Customize the column header

class Return_AuthorizationResource(resources.ModelResource):
    class Meta:
            model = return_authorization
            fields =('product','serial_number', 'problem_description', 'RMA_number', )
            import_id_fields = ['serial_number']


from django.utils.html import format_html
class RMAImagesInline(admin.TabularInline):
    model = RMAImages
    form = RMAImagesForm
    #form = AdditionalImagesForm  # Use the custom form that allows multiple image uploads
    extra = 0  # Don't display any empty forms by default
    show_change_link = True  # Allow editing existing images
    verbose_name_plural = "RMA Images"

    fields = ('a_image', 'image_thumbnail', 'image_caption', 'return_authorization')  # Fields to display
    readonly_fields = ('image_thumbnail',)  # Make thumbnail and dimensions read-only

    # 1. Display the thumbnail with hover effect for the full-size image
    def image_thumbnail(self, obj):
        if obj.a_image:
            return format_html(
                """
                <style>
                    .thumbnail-wrapper {{
                        position: relative;
                        display: inline-block;
                    }}
                    .thumbnail-wrapper img {{
                        cursor: pointer;
                    }}
                    .thumbnail-wrapper .hover-image {{
                        display: none;
                        position: absolute;
                        top: 0;
                        right: 110%; /* Move to the left by adjusting the right position */
                        z-index: 1;
                        border: 1px solid #ddd;
                    }}
                    .thumbnail-wrapper:hover .hover-image {{
                        display: block;
                    }}
                </style>
                <div class="thumbnail-wrapper">
                    <img src="{}" height="100" />
                    <div class="hover-image">
                        <img src="{}" style="max-width: 400px;" /> <!-- Display at original size -->
                    </div>
                </div>
                """,
                obj.a_image.url, obj.a_image.url
            )
        return "No Image"

    image_thumbnail.short_description = 'Thumbnail'  # Customize the column header


class Return_Authorizationdmin(ImportExportModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('RMA_number', 'last_updated', 'Nitecore_to_be_exported','rma_status', 'product', 'serial_number', 'customer_id_or_order_number', 'store_front', 'first_name', 'last_name', 'next_action', 'next_action_date', )
    #list_editable = ('rma_status',)
    #list_editable = ('Nitecore_to_be_exported','rma_status',)
    fieldsets = (
                 ('Auto Generated RMA number', {'fields': (('RMA_number','serial_number', 'created_at',),)}),
                 ('For Factory Export', {'fields': (('Nitecore_to_be_exported', 'problem_description'),)}),
                 ('RMA Status', {'fields': (('rma_status', 'closed_at',),)}),
                 ('Basics', {'fields': ('store_front','customer_id_or_order_number','product',('first_name', 'last_name',), ('original_tracking_number', 'replacement_tracking_number',), ('condition_returned',),)}),
                 ('Next Action', {'fields': (('next_action','next_action_date',),)}),
                 )

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('RMA_number',)
    list_per_page = 50
    ordering = ['-last_updated','-created_at']
    search_fields = ['RMA_number', 'product', 'serial_number','customer_id_or_order_number', 'first_name', 'last_name']
    list_filter = ('rma_status','Nitecore_to_be_exported',)
    inlines = [Actions_TakenInline, RMAImagesInline,]

    #exclude = ('created_at', 'updated_at',)
    exclude = []
    # sets up slug to be generated from product name


    save_as = True
    resource_class = Return_AuthorizationResource

    actions = ['mark_has_exported','clone_rma']
    def get_actions(self, request):
        actions = super(Return_Authorizationdmin, self).get_actions(request)
        return actions

    def mark_has_exported(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd.Nitecore_to_be_exported = False
            now = date.today()
            sd.next_action = "Exported to Nitecore on " + str(now)
            sd.next_action_date = now

            sd.save()    # initial save

    mark_has_exported.short_description = "Mark has exported"

    def clone_rma(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd_copy = copy.copy(sd) # (2) django copy object
            sd_copy.id = None   # (3) set 'id' to None to create new object
            sd_copy.serial_number = None
            sd_copy.RMA_number = sd.RMA_number + "c"
            
            sd_copy.save()    # initial save


            for ta in sd.rmaimages_set.all():
                ta_copy = copy.copy(ta)
                ta_copy.id = None
                ta_copy.return_authorization = sd_copy
                ta_copy.save()

            for ai in sd.actions_taken_set.all():
                ai_copy = copy.copy(ai)
                ai_copy.id = None
                ai_copy.return_authorization = sd_copy
                ai_copy.save()


    clone_rma.short_description = "Clone the RMA"

    def save_model(self, request, obj, form, change):
        # Save the main object first (this saves other fields like image_caption)
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        # This method ensures that all formsets (including multiple images) are saved
        print(f"******save_formset called")
        instances = formset.save(commit=False)
        #print("Form is valid")
        #print("Cleaned data:", form.cleaned_data)  # Inspect the cleaned data

        # Handle deletions
        for obj in formset.deleted_objects:
            obj.delete()
            # Explicitly delete the object if marked for deletion


        for instance in instances:
            # Log the image_caption value being processed
            #print(f"Original image caption: {instance.image_caption}")
            #print(f"Cleaned image caption: {form.cleaned_data.get('image_caption')}")

            # Save the instance (each image object) with the related fields like image_caption
            #instance.image_caption = form.cleaned_data.get('image_caption', instance.image_caption)
            #instance.product = form.cleaned_data.get('product', instance.product)
            #instance.save()
            print(f"Image_caption = {instance.image_caption}")
            if instance.image_caption:
                instance.save()


        formset.save_m2m()

    #class Media:
    #    js = (
    #        '/static/js/tiny_mce/tiny_mce.js',
    #        '/static/js/admin_pages.js'
    #    )



# registers your product model with the admin site
admin.site.register(return_authorization, Return_Authorizationdmin)

class Insurance_ClaimsAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('case_number', 'claim_status', 'product', 'customer_id_or_order_number', 'store_front', 'country', 'reimbursed_amount', )


    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('case_number',)
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['case_number', 'product', 'customer_id_or_order_number']
    list_filter = ('claim_status','is_buyer_refunded')
    exclude = []


# registers your product model with the admin site
admin.site.register(insurance_claims, Insurance_ClaimsAdmin)

class SupportTicketAttachmentInline(admin.StackedInline):
    model = attachment_to_support_ticket
    extra = 0
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
    }


class Support_TicketsAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('case_number', 'ticket_status', 'product', 'customer_id_or_order_number', 'store_front', 'country', 'tracking_number', )


    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('case_number','customer_id_or_order_number')
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['case_number', 'product', 'customer_id_or_order_number', 'tracking_number']
    list_filter = ('ticket_status',)
    exclude = []
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
    }

    inlines = [SupportTicketAttachmentInline, ]

# registers your product model with the admin site
admin.site.register(support_ticket, Support_TicketsAdmin)


from import_export import resources
from ecomstore.marketplaces.models import *
from import_export import fields

from import_export.admin import ImportExportModelAdmin

class AmazonOrderReturnAuditImagesInline(admin.StackedInline):
    model = AmazonOrderReturnAuditImages
    extra = 0


class AmazonOrderReturnAuditResource(resources.ModelResource):
    """
    order_id = fields.Field(column_name='order-id')
    return_date = fields.Field(column_name='return-date')
    sku = fields.Field(column_name='sku')
    asin = fields.Field(column_name='asin')
    fnsku = fields.Field(column_name='fnsku')
    product_name = fields.Field(column_name='product-name')
    quantity = fields.Field(column_name='quantity')
    fulfillment_center_id = fields.Field(column_name='fulfillment-center-id')
    detailed_disposition = fields.Field(column_name='detailed-disposition')
    reason = fields.Field(column_name='reason')
    status = fields.Field(column_name='status')
    lpn = fields.Field(column_name='license-plate-number')
    customer_comments = fields.Field(column_name='customer-comments')
    """

    class Meta:
        model = AmazonOrderReturnAudit
        #fields = ('id','order_id', 'buyer_email',)
        #exclude = ('purchase_date','payments_date')
        import_id_fields = ['lpn']


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




class AmazonOrderReturnAuditExportImportAdmin(ImportExportModelAdmin):
    list_display = ('lpn','order_id','sku','asin','fnsku','product_name','quantity','ticket_id','status','internal_status','last_updated')
    search_fields = ('order_id','lpn','asin')
    list_display_links = ('order_id','lpn',)
    ordering = ['-return_date']
    list_filter = ('status','internal_status','asin')
    list_editable = ('ticket_id','internal_status')
    ordering = ['-last_updated','-created_at']
    actions = [export_as_csv_action("CSV Export", fields=['order_id'])]
    resource_class = AmazonOrderReturnAuditResource
    inlines = [AmazonOrderReturnAuditImagesInline,]


    def get_actions(self, request):
        actions = super(AmazonOrderReturnAuditExportImportAdmin, self).get_actions(request)
        return actions


    pass

admin.site.register(AmazonOrderReturnAudit, AmazonOrderReturnAuditExportImportAdmin)
