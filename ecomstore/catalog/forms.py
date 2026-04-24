from django import forms
from ecomstore.catalog.models import Product, Category, ProductReview, ProductQuestion, AdditionalImages
from tagging.models import Tag
from django.contrib import messages


from django import forms
from django.forms.widgets import ClearableFileInput
from .models import AdditionalImages


class BulkImageUploadWidget(ClearableFileInput):
    template_name = 'bulk_image_upload.html'

    def __init__(self, attrs=None):
        # Ensure the 'multiple' attribute is added correctly
        if attrs is None:
            attrs = {}
        attrs.update({'multiple': 'multiple', 'accept': 'image/*'})  # Add 'multiple' attribute correctly
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['accept'] = 'image/*'  # Force accept attribute for images only
        return super().render(name, value, attrs, renderer)

class AdditionalImagesForm(forms.ModelForm):
    class Meta:
        model = AdditionalImages
        fields = ['a_image', 'image_caption', 'product']
        widgets = {
            'a_image': BulkImageUploadWidget(),  # Use custom widget to allow multiple uploads
        }

    def save(self, commit=True):

        instance = super().save(commit=False)


        if not instance.pk:
            # Loop over all files in self.files, focusing on those with 'a_image'
            for key in self.files:
                if key.startswith('additionalimages_set') and 'a_image' in key:
                    files = self.files.getlist(key)
                    print(f"**********Files for field {key}: {files}")  # Debugging output

                    if len(files) > 0:
                        for file in files:
                            # Save each file as an instance of AdditionalImages
                            image_instance = AdditionalImages(
                                product=self.instance.product,
                                image_caption=self.cleaned_data.get('image_caption'),
                                a_image=file
                            )
                            print(f"**********File for field {key}: {file}")  # Debugging output

                            image_instance.save()
        # Handling updated images and captions for an existing instance
        # Check if 'image_caption' is present in cleaned_data
        if instance.pk and 'image_caption' in self.cleaned_data:
            image_caption = self.cleaned_data['image_caption']
            print(f"********** Image caption before save: '{image_caption}'")  # Debugging output

            # Explicitly set the image_caption field
            instance.image_caption = image_caption if image_caption != '' else ''  # Handle empty string case


            instance.save()

        return instance



class TestImageForm(forms.Form):
    a_image = forms.ImageField(widget=BulkImageUploadWidget())


class ProductAdminForm(forms.ModelForm):
    """ ModelForm class to validate product instance data before saving from admin interface """
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        if self.cleaned_data['price'] < 0:
            raise forms.ValidationError('Price supplied must be greater than zero.')
        return self.cleaned_data['price']

class ProductAddToCartForm(forms.Form):
    """ form class to add items to the shopping cart """
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity'}),
                                  error_messages={'invalid':'Please enter a valid quantity.'},
                                  min_value=1)
    product_slug = forms.CharField(widget=forms.HiddenInput())

    def __init__(self, request=None, *args, **kwargs):
        """ override the default so we can set the request """
        self.request = request
        super(ProductAddToCartForm, self).__init__(*args, **kwargs)

    def clean(self):
        """ custom validation to check for presence of cookies in customer's browser """
        if self.request:
            if not self.request.session.test_cookie_worked():
                raise forms.ValidationError("Cookies must be enabled.")
        return self.cleaned_data

class ProductReviewForm(forms.ModelForm):
    """ Form class to submit a new ProductReview instance """
    class Meta:
        model = ProductReview
        exclude = ('user','product', 'is_approved')

class ProductQuestionForm(forms.ModelForm):
    """ Form class to submit a new ProductReview instance """
    class Meta:
        model = ProductQuestion
        exclude = ('user','product', 'is_answered')


class InventoryForm(forms.Form):

    def __init__(self, *args, **kwargs):
        products = kwargs.pop('products', None)

        super(InventoryForm, self).__init__(*args, **kwargs)

        if not products:
            products = Product.objects.filter(is_active=True).order_by('brand')

        for product in products:

            kw = {
            'label' : product.slug,
            'help_text' : product.name,
            'initial' : product.quantity,
            'widget' : forms.TextInput(attrs={'size':'10'}) }

            qty = forms.DecimalField(**kw)
            self.fields['qty__%s' % product.slug] = qty
            qty.slug = product.slug
            qty.product_id = product.id

            initial_cost_price = product.inventory_price

            kw['initial'] = initial_cost_price
            kw['required'] = False
            kw['widget'] = forms.TextInput(attrs={'size':'10'})
            cost_price = forms.DecimalField(**kw)
            cost_price.slug = product.slug
            self.fields['cost_price__%s' % product.slug] = cost_price

            initial_price = product.price

            kw['initial'] = initial_price
            kw['required'] = False
            kw['widget'] = forms.TextInput(attrs={'size':'10'})
            price = forms.DecimalField(**kw)
            price.slug = product.slug
            self.fields['price__%s' % product.slug] = price

            kw['initial'] = product.is_active
            kw['widget'] = forms.CheckboxInput(attrs={'class': "checkbox active"})
            active = forms.BooleanField(**kw)
            active.slug = product.slug
            self.fields['active__%s' % product.slug] = active

            kw['initial'] = product.is_featured
            kw['widget'] = forms.CheckboxInput(attrs={'class': "checkbox featured"})
            featured = forms.BooleanField(**kw)
            featured.slug = product.slug
            self.fields['featured__%s' % product.slug] = featured

            kw['initial'] = product.is_new_arrival
            kw['widget'] = forms.CheckboxInput(attrs={'class': "checkbox new_arrival"})
            new_arrival = forms.BooleanField(**kw)
            new_arrival.slug = product.slug
            self.fields['new_arrival__%s' % product.slug] = new_arrival


    def save(self, request):
        self.full_clean()
        for name, value in self.cleaned_data.items():
            opt, key = name.split('__')

            prod = Product.objects.get(slug__exact=key)

            if opt=='qty':
                if value != prod.quantity:
                    request.user.message_set.create(message='Updated %s stock to %s' % (key, value))
                    #log.debug('Saving new qty=%d for %s' % (value, key))
                    prod.quantity = value
                    prod.save()

            elif opt=='cost_price':
                if value != prod.inventory_price:
                    request.user.message_set.create(message='Updated %s cost price to %s' % (key, value))
                    #log.debug('Saving new price %s for %s' % (value, key))
                    prod.inventory_price = value
                    prod.save()

            elif opt=='price':
                if value != prod.price:
                    request.user.message_set.create(message='Updated %s unit price to %s' % (key, value))
                    #log.debug('Saving new price %s for %s' % (value, key))
                    prod.price = value
                    prod.save()


            elif opt=="active":
                if value != prod.is_active:
                    if value:
                        note = "Activated %s"
                    else:
                        note = "Deactivated %s"
                    messages.success(request,message=note % (key))

                    prod.is_active = value
                    prod.save()

            elif opt=="featured":
                if value != prod.is_featured:
                    if value:
                        note = "%s is now featured"
                    else:
                        note = "%s is no longer featured"
                    messages.success(request,message=note % (key))

                    prod.is_featured = value
                    prod.save()

            elif opt=="new_arrival":
                if value != prod.is_new_arrival:
                    if value:
                        note = "%s is now new arrival"
                    else:
                        note = "%s is no longer new arrival"
                    messages.success(request,message=note % (key))

                    prod.is_new_arrival = value
                    prod.save()
