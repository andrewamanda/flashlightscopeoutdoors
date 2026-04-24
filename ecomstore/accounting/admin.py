from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

# Register your models here.



from ecomstore.catalog.models import RichTextField
from ckeditor.widgets import CKEditorWidget
from ecomstore.accounting.models import TaxDue, QuartlyFiling, InventoryOrdering, ShipmentTracking, ExpenseBookkeeping, BusinessEntity, AllAccounts

class AllAccountsAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'account_type', 'account_number',)
    search_fields = ('bank_name',)
    ordering = ['bank_name']
admin.site.register(AllAccounts, AllAccountsAdmin)


class BusinessEntityAdmin(admin.ModelAdmin):
    list_display = ('business_name','federal_tax_id',)
    search_fields = ('business_name',)
    ordering = ['business_name']

admin.site.register(BusinessEntity, BusinessEntityAdmin)

class TaxDueAdmin(admin.ModelAdmin):
    list_display = ('tax_type','tax_period','tax_year','due_date','payment_date','deposit_form')
    search_fields = ('tax_type',)
    ordering = ['payment_date']
    fieldsets = (
                 ('Basics', {'fields': (('tax_type','tax_period','tax_year',),)}),
                 ('Dates', {'fields': (('due_date','payment_date',),)}),
                 ('Details', {'fields': (('deposit_form','details',),)}),
                )
    list_filter = ['tax_year']


    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

admin.site.register(TaxDue, TaxDueAdmin)

class QuartlyFilingAdmin(admin.ModelAdmin):
    list_display = ('tax_type','tax_period','tax_year','due_date','filed_date','tax_form')
    search_fields = ('tax_type',)
    ordering = ['filed_date']
    fieldsets = (
                 ('Basics', {'fields': (('tax_type','tax_period','tax_year',),)}),
                 ('Dates', {'fields': (('due_date','filed_date',),)}),
                 ('Details', {'fields': (('tax_form','details',),)}),
                )
    list_filter = ['tax_year']

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

admin.site.register(QuartlyFiling, QuartlyFilingAdmin)

class ShipmentTrackingInline(admin.StackedInline):
    model = ShipmentTracking
    extra = 0
    fieldsets = (
                 ('Basics', {'fields': (('tracking_number','status','packing_list','duty_amount','payment_by','commercial_invoice','payment_stub','details',),)}),
                )
    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

class InventoryOrderingAdmin(admin.ModelAdmin):
    list_display = ('brand','order_id','order_date','order_total','status','yet_to_receive','all_trackings',)
    search_fields = ('order_id',)
    ordering = ['-order_date']

    list_filter = ['brand']

    inlines = [ShipmentTrackingInline, ]

    fieldsets = (
                 ('Basics', {'fields': (('brand','status','order_date','paid_date','order_id','order_total'),('pi','yet_to_receive','payment_receipt',),)}),
                )

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

admin.site.register(InventoryOrdering, InventoryOrderingAdmin)


class ExpenseBookkeepingAdmin(admin.ModelAdmin):
    list_display = ('business_entity', 'expense_type','expense_date','expense_place','expense_total','receipt',)
    search_fields = ('expense_name',)
    ordering = ['expense_date']

    list_filter = ['expense_type', 'business_entity']


    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

#admin.site.register(ExpenseBookkeeping, ExpenseBookkeepingAdmin)

class ExpenseBookkeepingResource(resources.ModelResource):

    category = fields.Field(column_name='Category', attribute='category')
    expense_date = fields.Field(column_name='Transaction Date', attribute='expense_date')
    expense_total = fields.Field(column_name='Debit', attribute='expense_total')
    expense_place = fields.Field(column_name='Description', attribute='expense_place')


    class Meta:
        model = ExpenseBookkeeping
        #import_id_fields = (b'expense_date',)

class ExpenseBookkeepingExportImportAdmin(ImportExportModelAdmin):
    list_display = ('category','expense_type','expense_date','expense_place','expense_total','receipt',)
    search_fields = ('expense_name',)
    list_editable = ('expense_type',)
    ordering = ['expense_date']

    list_filter = ['category','expense_type', ]
    resource_class = ExpenseBookkeepingResource

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }
    pass

    def total_in_view(self, request, queryset):
        sum_a = sum([item.expense_total for item in queryset])
        return u'%s' % sum_ao


admin.site.register(ExpenseBookkeeping, ExpenseBookkeepingExportImportAdmin)
