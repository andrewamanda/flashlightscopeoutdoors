from django.contrib import admin
from ecomstore.cart.models import CartItem, WishList
from django.template.loader import render_to_string
import logging
from django.core.mail import EmailMessage
from datetime import datetime
from datetime import timedelta


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart_id','email', 'last_abandon_email_sent', 'no_abandon_email', 'product_name','quantity','date_added',)
    list_display_links = ('cart_id',)
    search_fields = ('cart_id','email',)
    list_filter = ('no_abandon_email',)
    list_editable = ('no_abandon_email',)
    ordering = ['date_added']

    actions = ['really_delete_selected', 'send_abandon_cart_email']

    def get_actions(self, request):
        actions = super(CartItemAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def really_delete_selected(self, request, queryset):
        for obj in queryset:
            obj.pre_delete()

        if queryset.count() == 1:
            message_bit = "1 Cart item entry was"
        else:
            message_bit = "%s cart items were" % queryset.count()
        self.message_user(request, "%s successfully deleted." % message_bit)

        queryset.delete()

    really_delete_selected.short_description = "Delete selected entries"

    def send_abandon_cart_email(self, request, queryset):

        today = datetime.today()

        all_cartitems = CartItem.objects.all()
        for obj in all_cartitems:
            create_date = obj.date_added
            waiting_days = today - timedelta(days=30)
            if create_date < waiting_days:
                obj.pre_delete()
                obj.delete()



        all_cartitems = CartItem.objects.exclude(email__isnull=True)

        temp = []
        for obj in all_cartitems:
            temp.append(obj.email)

        all_emails = set(temp)


        count = 0
        for e in all_emails:
            cis = CartItem.objects.filter(email=e)

            should_proceed = True
            for c in cis:
                if c.no_abandon_email == True or c.last_abandon_email_sent:
                    should_proceed = False
                    break
                create_date = c.date_added
                waiting_days = today - timedelta(days=1)
                if create_date > waiting_days:
                    should_proceed = False
                    break

            if should_proceed == False:
                continue


            template = "cart/abandoncart_recover.html"
            from_email = "sales@andrew-amanda.com"

            from django.contrib.sites.models import Site
            msg = render_to_string(template, {'cart_items': cis,'email':e, 'domain': Site.objects.get_current().domain})
            subject = "Your shopping cart is about to expire"

            EmailMsg = EmailMessage(subject,msg,from_email,[e],headers={'Reply-To':from_email})
            EmailMsg.content_subtype = "html"
            try:
                EmailMsg.send()
                count = count + 1
                for c in cis:
                    c.last_abandon_email_sent = today
                    c.save()
                self.message_user(request, "Recovery emails successfully sent to %s." % e)
            except Exception as ex:
                    logging.error("In Exc sending mail to %s -- Error: %s", e, ex)




    send_abandon_cart_email.short_description = "Send Abandon Cart Email"


admin.site.register(CartItem, CartItemAdmin)


class WishListAdmin(admin.ModelAdmin):
    list_display = ('user','date_added',)
    list_display_links = ('user',)
    ordering = ['date_added']
    filter_horizontal = ('products',)


admin.site.register(WishList, WishListAdmin)
