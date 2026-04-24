from django.db import models
from ecomstore.catalog.models import Product
from ecomstore.catalog import deal_processor
from django.utils.safestring import mark_safe

from django.contrib.auth.models import User




class CartItem(models.Model):
    """ model class containing information each Product instance in the customer's shopping cart """
    cart_id = models.CharField(max_length=50, db_index=True)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, unique=False, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, null=True, blank=True)
    no_abandon_email = models.BooleanField(default=False)
    last_abandon_email_sent = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    @property
    def total(self):
        #return self.quantity * deal_processor.get_effective_price(self.product)
        return self.quantity * self.product.sale_price

    @property
    def name(self):
        return self.product.name

    def product_name(self):
        url = '/admin/catalog/product/' + str(self.product.id)
        return mark_safe(u'<a href="%s">%s</a>' % (url, self.product.name))
    product_name.allow_tags = True


    @property
    def full_name(self):
        cio = self.cartitemoption_set.all()
        extra_desc = ""
        for c in cio:
            extra_desc += c.title
            extra_desc += "-"
            extra_desc += c.option
            if c.price > 0:
                extra_desc += "($"
                extra_desc += str(c.price)
                extra_desc += ")"
            extra_desc += "--"
        return self.product.name + "--" + extra_desc

    @property
    def price(self):
        return self.product.sale_price
        #return deal_processor.get_effective_price(self.product)

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def able_to_ship_quantity(self):
        if self.quantity <= self.product.quantity or self.product.quantity == 0:
            return self.quantity
        else:
            return self.product.quantity


    def augment_quantity(self, quantity):
        """ called when a POST request comes in for a Product instance already in the shopping cart """
        try:
            self.quantity = self.quantity + int(quantity)
            self.save()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    def pre_delete(self):
        self.product.quantity += self.quantity
        self.product.save()

class CartItemOption(models.Model):
    title = models.CharField(max_length=200)
    option = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=9,decimal_places=2, null=True, blank=True)
    availability = models.CharField(max_length=10, null=True, blank=True)
    cartitem = models.ForeignKey(CartItem, unique=False, on_delete=models.CASCADE)

    lucky_email = models.CharField(max_length=30, null=True, blank=True)
    gift_message = models.TextField(null=True, blank=True, help_text='this is for gift certificate only')

    class Meta:
        db_table = 'cartitem_option'

    @property
    def title_normalize(self):
        return self.title.replace(' ', '_')


class WishList(models.Model):
    """ model class containing information each Product instance in the customer's shopping cart """
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, null=True, blank=True)

    class Meta:
        db_table = 'wish_list'


    def __str__(self):
        return 'Wish list for: ' + self.user.username

    def __unicode__(self):
        return 'Wish list for: ' + self.user.username
