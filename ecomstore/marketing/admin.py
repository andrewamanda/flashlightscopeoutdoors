from django.contrib import admin
from ecomstore.marketing.models import *

class GroupBuyParticipantInline(admin.TabularInline):
    model = GroupBuyParticipant
    #readonly_fields = ('user','email','quantity','reason','country','state','last_updated',)
    list_display = ('user','name','email','quantity','reason','country','state','last_updated',)

    extra = 0

from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

class GroupBuyProductAdmin(AjaxSelectAdmin):
    list_display = ('product_name','status','coupon','discount','min_quantity', 'max_quantity', 'start_date', 'cutoff_date', 'comment')
    list_editable = ('coupon','discount','min_quantity', 'max_quantity', 'comment','status')
    list_per_page = 10
    list_filter = ('status',)
    ordering = ['-cutoff_date']
    search_fields = ['product__name']
    form = make_ajax_form(GroupBuyProduct,{'product':'products'})

    inlines = [GroupBuyParticipantInline,]

    actions = ['send_groupbuy_coupon_emails']

    def product_name(self, obj):
        return obj.product.name

    def get_actions(self, request):
        actions = super(GroupBuyProductAdmin, self).get_actions(request)
        return actions

    def send_groupbuy_coupon_emails(self, request, queryset):
       for obj in queryset:
            if obj.status != 'CLOSED_COUPON_WAITING':
                continue
            allparticipants = obj.groupbuyparticipant_set.all()
            for p in allparticipants:
                emailStatus = p.sendgroupbuycoupon()
                if emailStatus:
                   self.message_user(request, "Coupon was successfully sent to {}.".format(p.email))
                else:
                   self.message_user(request, "Coupon was not sent to {}.".format(p.email))
            obj.status = 'CLOSED_COUPON_SENT'
            obj.save()

    send_groupbuy_coupon_emails.short_description = "Send groupbuy coupon"


    pass

admin.site.register(GroupBuyProduct, GroupBuyProductAdmin)

