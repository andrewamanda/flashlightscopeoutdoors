from django.contrib import admin
from ecomstore.catalog.models import Department, Product, ProductAssociation, Category, ProductReview, Brand, Series, SubCategory, DealOfTheDay, AdditionalImages, accessory_product, OptionalChoices, IndividualChoice, TopAttributes, PriceRange, BrightnessRange
from ecomstore.catalog.forms import ProductAdminForm, AdditionalImagesForm
from ckeditor.widgets import CKEditorWidget
import copy
from django.utils.html import format_html
from django.contrib.sites.models import Site
from django.shortcuts import redirect
from django.urls import reverse

from ecomstore import settings
from ecomstore.settings import AMZN_SP_REFRESH_TOKEN,AMZN_SP_LWA_APP_ID,AMZN_SP_LWA_CLIENT_SECRET
from django.utils.encoding import smart_str
from django.http import HttpResponse
from django.template.loader import render_to_string

from ecomstore.catalog.models import super_image_url
from ecomstore.utils.images import *

from boto.mws.connection import MWSConnection
import time
from ecomstore.utils.strops import find_between
from ecomstore.utils.walmartapis import *
from django.contrib import messages
from django.urls import path

from django.utils.html import format_html
from django.utils.safestring import mark_safe

from sp_api.api import Feeds
from sp_api.base import Marketplaces, SellingApiException

import re

import random

def is_valid_asin(asin):
    """
    This function checks if the input string is a valid Amazon ASIN.
    An ASIN is valid if it is exactly 10 alphanumeric characters long.

    :param asin: The input string to check.
    :return: True if the string is a valid ASIN, False otherwise.
    """
    # Check if the ASIN is exactly 10 characters long and is alphanumeric
    if isinstance(asin, str) and len(asin) == 10 and re.match(r'^[A-Za-z0-9]+$', asin):
        return True
    return False

class CounterAdmin(admin.ModelAdmin):
    counted_fields = ("features", "full_description")

    #really for textareas
    max_lengths = {'abstract': 400,}

    class Media:
        js = ('http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js',
              '/static/js/admin/jquery.charCount.js',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(CounterAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name in self.counted_fields:
            try:
                len = self.max_lengths[db_field.name]
                field.widget.attrs['maxlength'] = len
            except: pass
            field.widget.attrs['class'] = 'counted ' + field.widget.attrs.get('class','')
        return field


from .forms import AdditionalImagesForm, BulkImageUploadWidget
from django.utils.html import format_html
class AdditionalImagesInline(admin.TabularInline):
    model = AdditionalImages
    form = AdditionalImagesForm
    #form = AdditionalImagesForm  # Use the custom form that allows multiple image uploads
    extra = 0  # Don't display any empty forms by default
    show_change_link = True  # Allow editing existing images
    verbose_name_plural = "Additional Images"

    fields = ('a_image','image_caption', 'image_thumbnail', 'image_dimensions','product')  # Fields to display
    readonly_fields = ('image_thumbnail', 'image_dimensions')  # Make thumbnail and dimensions read-only


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
                        z-index: 9999;
                        border: 1px solid #ddd;
                    }}
                    .thumbnail-wrapper:hover .hover-image {{
                        display: block;
                    }}
                </style>
                <div class="thumbnail-wrapper">
                    <img src="{}" height="100" />
                    <div class="hover-image">
                        <img src="{}" style="max-width: 1000px;" /> <!-- Display at original size -->
                    </div>
                </div>
                """,
                obj.a_image.url, obj.a_image.url
            )
        return "No Image"

    image_thumbnail.short_description = 'Thumbnail'  # Customize the column header



    # 2. Display image dimensions and width/height ratio normalized to height of 600 pixels
    def image_dimensions(self, obj):
        if obj.a_image:
            width, height = obj.a_image.width, obj.a_image.height
            if height > 0:
                ratio = width / height * 600  # Normalize width to height of 600 pixels
                return f"{width} x {height} pixels (ratio: {round(ratio, 2)} x 600)"
            return f"{width} x {height} pixels"
        return "No Image"

    image_dimensions.short_description = 'Image Dimensions'



class TopAttributesInline(admin.TabularInline):
    model = TopAttributes
    extra = 0


class IndividualChoiceInline(admin.TabularInline):
    model = IndividualChoice

class OptionalChoicesInline(admin.StackedInline):
    model = OptionalChoices
    extra = 0

class OptionalChoicesAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'title',)
    list_display_links = ('title',)
    inlines = [IndividualChoiceInline, ]

admin.site.register(OptionalChoices, OptionalChoicesAdmin)

from django.db import models
from tinymce.widgets import TinyMCE
from ecomstore.catalog.models import RichTextField
from django.forms import TextInput

from import_export import resources
from import_export import fields

from import_export.admin import ImportExportModelAdmin

def build_amazon_feed(queryset, marketplace):

        base_template = 'marketplaces/Amazon_Other_Flashlights_base.txt'
        entries = ''
        for sd in queryset:
            not_weapon = True
            allowed = True
            if "remote" in sd.name.lower() or "mount" in sd.name.lower():
                not_weapon = False

            if marketplace == "au" and not not_weapon:
                allowed = False
            if allowed:
                entries += '\n'
                entries += sd.add2amazonfeed(marketplace).decode("utf-8")
        if 'flashlight' in sd.get_department.lower():
            if marketplace == "com":
                base_template = 'marketplaces/Amazon_Other_Flashlights_base.txt'
            if marketplace == "ca":
                base_template = 'marketplaces/Amazon_CA_Other_Flashlights_base.txt'
            if marketplace == "mx":
                base_template = 'marketplaces/amazon_mx_outdoors_template_base.txt'
            if marketplace in ["eu", "uk", "de", "it", "es", "fr", "se", "tr"]:
                base_template = 'marketplaces/amazon_uk_sports_flashlightlatern_20190328_base.txt'
            if marketplace == "jp":
                base_template = 'marketplaces/amazon_uk_sports_flashlightlatern_20190328_base.txt'
            if marketplace == "au":
                base_template = 'marketplaces/amazon_au_FlashlightLanterns_base.txt'
            if marketplace == "sg":
                base_template = 'marketplaces/amazon_sg_flashlight_base.txt'

            if marketplace == "ae":
                base_template = 'marketplaces/amazon_ae_other_flashlight_base.txt'
            if marketplace == "sa":
                base_template = 'marketplaces/amazon_ae_other_flashlight_base.txt'


        if 'science' in sd.get_department.lower():
            base_template = "marketplaces/amazon_labsupplies_template.base.txt"
        feedstr = render_to_string(base_template)
        feedstr += entries
        return feedstr



def build_skuvault_feed(queryset):

        base_template = 'marketplaces/skuvault_product_base.csv'
        entries = ''
        for sd in queryset:
            entries += '\n'
            entries += sd.add2skuvaultfeed().decode("utf-8")

        feedstr = render_to_string(base_template)
        feedstr += entries
        return feedstr


class TopAttributesResource(resources.ModelResource):
    class Meta:
        model = TopAttributes
        import_id_fields = ['id']


class TopAttributesAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories

    resource_class = TopAttributesResource
    #sets up values for how admin site lists categories
    list_display = ('product', )
    list_display_links = ('product',)
    list_per_page = 20
    ordering = ['product']
    search_fields = ['product__name', ]
    list_filter = ('product__brand',)
    exclude = []


admin.site.register(TopAttributes, TopAttributesAdmin)

class AdditionalImagesResource(resources.ModelResource):
    class Meta:
        model = AdditionalImages
        import_id_fields = ['id']


class AdditionalImagesAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories

    resource_class = AdditionalImagesResource
    #sets up values for how admin site lists categories
    list_display = ('product', )
    list_display_links = ('product',)
    list_per_page = 20
    ordering = ['product']
    search_fields = ['product__name', ]
    list_filter = ('product__brand',)
    exclude = []


admin.site.register(AdditionalImages, AdditionalImagesAdmin)

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        import_id_fields = ['slug']
        # below line is only for exporting the iParcel catalog
        fields = ('sku', 'name', 'meta_description', 'price', 'weight',)
        export_order = ('sku', 'weight','price','name', 'meta_description')


class ProductAdmin(ImportExportModelAdmin, CounterAdmin):
    change_form_template = "admin/catalog/product_change_form.html"
    resource_class = ProductResource
    form = ProductAdminForm
    # sets values for how the admin site lists your products
    # list_display = ('name', 'price', 'inventory_price','quantity','is_active','is_new_arrival', 'is_featured','ranking','all_categories',)
    list_display = ('name', 'is_active', 'is_new_arrival','is_combo','modelNumber','sku','price', 'quantity', 'weight', 'is_coming_soon', 'is_featured','clearance','clearance_price','use_18650','use_cr123a','use_aa','view_on_site','ranking','max_lumens',)
    list_editable = ('modelNumber', 'weight', 'sku', 'quantity','is_active','is_combo', 'is_new_arrival', 'is_featured','ranking','clearance','clearance_price','use_18650','use_cr123a','use_aa','is_coming_soon','max_lumens')

    # which of the fields in 'list_display' tuple link to admin product page
    list_display_links = ('name',)
    list_per_page = 100
    ordering = ['-created_at']
    search_fields = ['name', 'sku', 'description', 'meta_keywords', 'meta_description']
    inlines = [TopAttributesInline, OptionalChoicesInline, AdditionalImagesInline,]
    list_filter = ('is_active','categories','brand','is_new_arrival','is_coming_soon', 'is_featured','clearance', 'is_openbox', 'use_18650','use_cr123a','use_aa',)
    #exclude = ('created_at', 'updated_at',)
    #exclude = ['description','features',]
    # sets up slug to be generated from product name
    prepopulated_fields = {'slug' : ('name',),'sku' : ('name',)}


    filter_horizontal = ('categories', 'subcategory',)
    readonly_fields = ('accessory_group_links',)

    fieldsets = (
                 ('Related Products & Accessories', {'fields': ('accessory_group_links',)}),
                 ('SEO Tags', {'fields': (('seo_title'),('seo_meta_description','seo_meta_keyword'),('seo_og_title','seo_og_description'), ('seo_h1_tag'),)}),
                 ('Basics', {'fields': (('name','modelNumber','slug','sku', 'is_combo',),('price','old_price','inventory_price',),('quantity'),('weight'),)}),
                 ('Batteries', {'fields':('use_18650','use_cr123a','use_aa')}),
                 ('Status', {'fields':(('is_active','is_bestseller',
                'is_featured','is_coming_soon','is_new_arrival','is_openbox','ranking',),('clearance','clearance_price'))}),
                 ('Catalog Information', {'fields': ('categories','subcategory','brand','series',)}),
                 ('Product Details', {'fields': ('max_lumens','meta_keywords','meta_description','full_description','description','features','image','image_caption','image_jetbeam')}),
                )

    formfield_overrides = {
        RichTextField: { 'widget': CKEditorWidget() },
        }

    from django.utils.safestring import mark_safe

    def accessory_group_links(self, obj):
        if not obj or not obj.pk:
            return format_html('Save this product first, then configure add-on products.')

        groups = accessory_product.objects.filter(products=obj).distinct().order_by('name')
        add_url = reverse('admin:catalog_accessory_product_add')
        changelist_url = reverse('admin:catalog_accessory_product_changelist')

        parts = [
            f'<p><a class="button" href="{add_url}">Add Products For This Tab</a> &nbsp; '
            f'<a href="{changelist_url}?products__id__exact={obj.pk}">View all tab-product groups for this product</a></p>',

            '<p class="help">Use this for batteries, chargers, holsters, or any other products you want customers to add along with this item. '
            'Group names are not shown on the storefront.</p>',
        ]

        if groups:
            parts.append('<ul>')
            for g in groups:
                change_url = reverse('admin:catalog_accessory_product_change', args=[g.pk])
                parts.append(f'<li><a href="{change_url}">{g.name}</a></li>')
            parts.append('</ul>')
        else:
            parts.append('<p>No add-on product groups configured for this product yet.</p>')

        return mark_safe(''.join(parts))

    accessory_group_links.short_description = 'Products shown in this tab'


    #class Media:
    #    js = (
    #        '/static/js/tiny_mce/tiny_mce.js',
    #        '/static/js/tiny_mce/tiny_mce_popup.js',
    #        '/static/js/tiny_mce/tiny_mce_src.js',
    #        '/static/js/tiny_mce/utils/editable_selects.js',
    #        '/static/js/tiny_mce/utils/form_utils.js',
    #        '/static/js/tiny_mce/utils/mctabs.js',
    #        '/static/js/tiny_mce/utils/validate.js',
    #        '/static/js/django_tinymce/init_tinymce.js',
    #        '/static/js/admin_pages.js'
    #    )

    save_as = True

    #class Media:
    #    js = (
    #        '/static/js/tiny_mce/tiny_mce.js',
    #        '/static/js/admin_pages.js'
    #    )

    actions = ['copy_to_a_new_product', 'export_to_amazon_com_feed', 'export_to_amazon_ca_feed', 'export_to_amazon_mx_feed',
        'export_to_amazon_uk_feed', 'export_to_amazon_jp_feed', 'export_to_amazon_au_feed', 'export_to_amazon_ae_feed', 'export_to_amazon_sa_feed', 'export_to_globalindustrial_feed', 'export_to_jet',
        'get_item_from_walmart','export_to_walmart','get_amazon_product_types', 'get_amazon_submission_status',
        'post_to_all_amazons', 'additem_to_sandbox_ebay', 'additem_to_aa_ebay', 'additem_to_fso_ebay', 'additem_to_both_ebays','export_to_skuvault','create_aplus_content','query_amazon_listing']
    def get_actions(self, request):
        actions = super(ProductAdmin, self).get_actions(request)
        return actions

    def save_model(self, request, obj, form, change):
        # Assuming 'name' format is 'Brand ModelNumber' (e.g., 'Nitecore EDC29')
        if obj.name:
            # Split the name to extract the model number
            parts = obj.name.split()
            if len(parts) > 1:
                # The last part is assumed to be the model number
                obj.modelNumber = parts[1] + ''.join(str(random.randint(0,9)) for _ in range(4))

                bullets = obj.description.splitlines()
                obj.seo_meta_keyword = obj.name + ":"
                for i, bullet in enumerate(bullets):
                    if i == len(bullets) - 1:  # Check if it's the last iteration
                        obj.seo_meta_keyword += " " + bullet  # No semicolon for the last item
                    else:
                        obj.seo_meta_keyword += " " + bullet + ";"

                obj.seo_title = obj.meta_description[:500]
                obj.seo_h1_tag = obj.meta_description[:500]
                obj.seo_meta_description = ("Discover the best rechargeable LED flashlights for camping and searching: " + obj.meta_description)[:500]

                obj.seo_og_title = (obj.name + " - Compact, Durable, Rechargeable High Power Flashlight For Every Day Venture")[:500]
                obj.seo_og_description = ("Discover the " + obj.name + ", a compact and durable flashlight designed for outdoor adventures and daily use. High lumens, waterproof, and rechargeable.")[:500]
                obj.seo_meta_keyword = obj.seo_meta_keyword[:500]

        # Call the original save method to ensure the object is saved
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


    def view_on_site(self, obj):
        return format_html("<a target='_blank' href='{url}'>View</a>", url=obj.get_absolute_url())
    view_on_site.allow_tags = True
    view_on_site.short_description = "View On Site"

    def export_to_newegg_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=newegg_feed.txt'
        entries = ''
        for sd in queryset:
             entries += '\n'
             entries += sd.add2neweggfeed('com')
        if 'flashlight' in sd.get_department.lower():
            base_template = 'marketplaces/newegg/HomeImprovement_BatchItemCreation_Flashlights_tab_base.txt'
        if 'science' in sd.get_department.lower():
            base_template = "marketplaces/amazon_labsupplies_template.base.txt"
        feedstr = render_to_string(base_template)
        feedstr += entries

        response.write(feedstr.encode('utf8'))
        return response
    export_to_newegg_feed.short_description = "Export to Newegg.com Feed"

    from django.utils.safestring import mark_safe
    import textwrap


    def get_amazon_product_types(self, request, queryset):
        from sp_api.api import ProductTypeDefinitions
        from sp_api.base import Marketplaces, SellingApiException
        import json
        import os
        import requests
        from django.utils.safestring import mark_safe
        import textwrap

        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        ptd = ProductTypeDefinitions(credentials=credentials, marketplace=Marketplaces.US)

        try:
            # 1) Get the definition wrapper (contains schema link)
            resp = ptd.get_definitions_product_type(
                productType="FLASHLIGHT",
                marketplaceIds=["ATVPDKIKX0DER"],
                requirements="LISTING"
            )
            payload = resp.payload

            schema_link_obj = payload.get("schema", {})
            schema_url = (schema_link_obj.get("link") or {}).get("resource")

            if not schema_url:
                self.message_user(request, f"No schema link found. Payload keys: {list(payload.keys())}")
                return

            # 2) Download the actual JSON schema from the signed S3 URL
            r = requests.get(schema_url, timeout=30)
            r.raise_for_status()
            schema_json = r.json()

            # 3) Save the full resolved schema
            base_dir = os.getcwd()
            full_schema_path = os.path.join(base_dir, "FLASHLIGHT_schema_resolved.json")
            with open(full_schema_path, "w") as f:
                json.dump(schema_json, f, indent=2)

            # 4) Extract unit_count schema (where enums + required fields are)
            unit_count_schema = None

            # Most product type schemas follow JSON Schema with properties at the top,
            # but some nest under "items" or "definitions". We'll try a few common places.
            if isinstance(schema_json, dict):
                if "properties" in schema_json and "unit_count" in schema_json["properties"]:
                    unit_count_schema = schema_json["properties"]["unit_count"]
                elif "items" in schema_json and isinstance(schema_json["items"], dict):
                    props = schema_json["items"].get("properties", {})
                    unit_count_schema = props.get("unit_count")
                elif "definitions" in schema_json and isinstance(schema_json["definitions"], dict):
                    # fallback: brute search in definitions
                    for k, v in schema_json["definitions"].items():
                        if isinstance(v, dict) and "properties" in v and "unit_count" in v["properties"]:
                            unit_count_schema = v["properties"]["unit_count"]
                            break

                if unit_count_schema:
                    unit_schema_path = os.path.join(base_dir, "FLASHLIGHT_unit_count_schema.json")
                    with open(unit_schema_path, "w") as f:
                        json.dump(unit_count_schema, f, indent=2)
                    self.message_user(
                        request,
                        "Resolved schema downloaded. Files written:\n"
                        f"- {full_schema_path}\n"
                        f"- {unit_schema_path}\n\n"
                        "Open FLASHLIGHT_unit_count_schema.json to see the exact enum tokens and structure required."
                    )
                else:
                    self.message_user(
                        request,
                        "Resolved schema downloaded, but unit_count was not found in common locations.\n"
                        f"File written: {full_schema_path}\n"
                        "Next step: search that file for 'unit_count' to locate its definition."
                    )

                if unit_count_schema:
                    unit_schema_str = json.dumps(unit_count_schema, indent=2)

                    # Django admin messages can't be huge — truncate safely
                    MAX_LEN = 3000
                    if len(unit_schema_str) > MAX_LEN:
                        unit_schema_str = unit_schema_str[:MAX_LEN] + "\n... (truncated)"

                    # Preserve indentation by wrapping in <pre>
                    self.message_user(
                        request,
                        mark_safe(
                            "<pre style='white-space: pre-wrap;'>"
                            + unit_schema_str
                            + "</pre>"
                        )
                    )


        except SellingApiException as e:
            self.message_user(request, f"Amazon SP-API error: {str(e)}")
        except requests.RequestException as e:
            self.message_user(request, f"HTTP error fetching schema URL: {str(e)}")
        except Exception as e:
            self.message_user(request, f"Unexpected error: {str(e)}")

    get_amazon_product_types.short_description = "Download resolved FLASHLIGHT schema (and unit_count schema)"




    def get_amazon_product_types_orig(self, request, queryset):
        from sp_api.api import ProductTypeDefinitions
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import tempfile
        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        # Initialize the ProductTypeDefinitions API client
        product_types = ProductTypeDefinitions(credentials=credentials, marketplace=Marketplaces.US)

        try:
            # Retrieve product types
            response = product_types.search_definitions_product_types()
            payload = response.payload

            import json
            type_flashlight = product_types.get_definitions_product_type("FLASHLIGHT")
            print ("Response str =", str(type_flashlight))
            # Specify the file path where you want to write the JSON data
            file_path = 'flashlight_product_type.json'

            # Write the JSON payload to the file
            with open(file_path, 'w') as json_file:
                json.dump(type_flashlight.payload, json_file, indent=4)

            # Extract the list of product types
            product_types_list = payload.get('productTypes', [])

            # Loop through each product type and print its name
            msg = "Product Types: "
            for product_type in product_types_list:
                name = product_type.get('name')
                msg = msg + "\r" + name
                #print(f"Product Type Name: {name}")
            self.message_user(request, msg)
        except SellingApiException as e:
            print(f"Error submitting feed: {e}")
            self.message_user(request, {e})
    #get_amazon_product_types.short_description = "Get Amazon Product Types"

    def get_amazon_submission_status(self, request, queryset):
        from sp_api.api import Feeds,ProductTypeDefinitions
        from sp_api.api import ListingsItems
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import json

        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )
        # Initialize the ListingsItems API client with credentials
        listings_items = ListingsItems(credentials=credentials, marketplace=Marketplaces.US)

        for sd in queryset:

            try:
                # Create or update the product listing
                response = listings_items.get_listings_item(
                    sellerId="A36D1O15HT30RE",  # Replace with your actual seller ID
                    sku=sd.sku,
                    marketplaceIds=[Marketplaces.US.marketplace_id],
                    includedData=["summaries", "issues"]

                )

                print(f"Feed submitted successfully: {response}")

                self.message_user(request, json.dumps(response.payload, indent=4))

            except SellingApiException as e:
                print(f"Error submitting feed: {e}")
                self.message_user(request, {e})



    get_amazon_submission_status.short_description = "Get Amazon Submission Status"

    def post_to_all_amazons(self, request, queryset):
        from sp_api.api import Feeds,ProductTypeDefinitions
        from sp_api.api import ListingsItems
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import tempfile

        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        # Initialize the ListingsItems API client with credentials
        listings_items = ListingsItems(credentials=credentials, marketplace=Marketplaces.US)



        for sd in queryset:
            prod = sd.productdata4spapi(".com")

            # Print or use the dynamically created product_data object
            import json
            from decimal import Decimal

            # Custom JSON encoder to handle Decimal objects
            def decimal_default(obj):
                if isinstance(obj, Decimal):
                    return float(obj)  # Convert Decimal to float (or use str(obj) to convert to string)
                raise TypeError("Object of type %s is not JSON serializable" % type(obj).__name__)

            print(json.dumps(prod, indent=4, default=decimal_default))

            # Helper function to convert Decimal objects to float in a dictionary
            def convert_decimal_to_float(obj):
                if isinstance(obj, dict):
                    return {k: convert_decimal_to_float(v) for k, v in obj.items()}
                elif isinstance(obj, list):
                    return [convert_decimal_to_float(item) for item in obj]
                elif isinstance(obj, Decimal):
                    return float(obj)  # or str(obj) if you prefer to serialize as strings
                else:
                    return obj

            # Modify the prod dictionary to convert Decimal objects
            prod_converted = convert_decimal_to_float(prod)


            body = {
                "productType": prod_converted['productType'],
                "requirements": "LISTING",
                "attributes": prod_converted['attributes']
            }
            print(json.dumps(body, indent=4, default=decimal_default))
            try:
                # Create or update the product listing
                response = listings_items.put_listings_item(
                    sellerId="A36D1O15HT30RE",  # Replace with your actual seller ID
                    sku=sd.sku,
                    marketplaceIds=[Marketplaces.US.marketplace_id],
                    body = body

                )
                response_dict = json.loads(json.dumps(response.payload))

                # Extract the submissionId
                submission_id = response_dict.get("submissionId")

                # Print the submissionId
                print("Submission ID:", submission_id)
                sd.image_caption = submission_id
                sd.save()
                print(f"Feed submitted successfully: {response}")
                self.message_user(request, json.dumps(response.payload, indent=4))

            except SellingApiException as e:
                print(f"Error submitting feed: {e}")
                self.message_user(request, {e})
    post_to_all_amazons.short_description = "Post To All Amazons"

    # 3. Custom view for the action button on the instance page (handles single object)
    def publish_to_amazon_action(self, request, obj_id):
        # Get the single object by ID and convert it into a queryset
        obj = self.get_object(request, obj_id)
        self.post_to_all_amazons(request, [obj])  # Reuse the shared method for one object
        # Use message_user to show the success message at the top of the page
        #self.message_user(request, f"A+ Content created for {obj.name}.")

        # Redirect back to the same change form page after the action
        return redirect(reverse('admin:catalog_product_change', args=[obj_id]))

    def create_aplus_content(self, request, queryset):
        from sp_api.api import AplusContent
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import tempfile
        from ecomstore.catalog.amazon_api import create_aplus_content_with_images

        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        # Initialize the ProductTypeDefinitions API client
        aplusContent = AplusContent(credentials=credentials, marketplace=Marketplaces.US)

        # search all content documents
        try:

            response = aplusContent.search_content_documents(marketplaceId=Marketplaces.US.marketplace_id)
            payload = response.payload
            # Define the file path to save the payload (as JSON)
            import json
            file_path = f"content_document_all.json"

            # Write the payload to the file
            import json
            with open(file_path, 'w') as file:
                # If payload is a dictionary, write it as JSON
                json.dump(payload, file, indent=4)

            print(f"All Content Document all has been written to {file_path}")

        except SellingApiException as e:
            print(f"Error submitting feed: {e}")
            self.message_user(request, {e})
        #end of search all content contentDocument

        #Retrieve an example content contentDocuments

        try:
            exampleKey = "664248f9-18e9-4743-b1c7-8a07a6468480"
            response = aplusContent.get_content_document(contentReferenceKey=exampleKey, includedDataSet = ["CONTENTS", "METADATA"], marketplaceId=Marketplaces.US.marketplace_id)
            payload = response.payload
            # Define the file path to save the payload (as JSON)
            file_path = f"content_document_{exampleKey}.json"

            # Write the payload to the file
            import json
            with open(file_path, 'w') as file:
                # If payload is a dictionary, write it as JSON
                json.dump(payload, file, indent=4)

            print(f"Content Document for {exampleKey} has been written to {file_path}")

        except SellingApiException as e:
            print(f"Error submitting feed: {e}")
            self.message_user(request, {e})

        #end of  Retrieve an example content contentDocuments

        for sd in queryset:
            more_images = sd.additionalimages_set.all()
            image_urls = []
            asins = []
            for img in more_images:
                if (is_valid_asin(img.image_caption)):
                    imageUrl = "http://" + Site.objects.get_current().domain + super_image_url(img.a_image.url)
                    image_urls.append(imageUrl)
                    if img.image_caption not in asins:
                        asins.append(img.image_caption)
            if len(image_urls) > 0 and len(asins) > 0:
                highlights = [sd.name, sd.seo_title, sd.seo_og_title, sd.seo_meta_keyword]
                descriptions = [sd.seo_meta_description, sd.seo_og_description, sd.seo_h1_tag, sd.seo_title]
                alts = [sd.name, sd.name, sd.name, sd.name]
                try:
                    response = create_aplus_content_with_images(sd.name, highlights, descriptions, alts, sd.full_description, asins, Marketplaces.US.marketplace_id, image_urls)
                    self.message_user(request, f"{sd.name}: {response}")
                except Exception as e:
                    print(f"Error submitting feed: {e}")
                    self.message_user(request, {e})
            else:
                self.message_user(request, f"{sd.name}: Asin or image is not set up correctly",level=messages.ERROR)


    create_aplus_content.short_description = "Create A+ Content"


    # 3. Custom view for the action button on the instance page (handles single object)
    def create_aplus_content_action(self, request, obj_id):
        # Get the single object by ID and convert it into a queryset
        obj = self.get_object(request, obj_id)
        self.create_aplus_content(request, [obj])  # Reuse the shared method for one object
        # Use message_user to show the success message at the top of the page
        #self.message_user(request, f"A+ Content created for {obj.name}.")

        # Redirect back to the same change form page after the action
        return redirect(reverse('admin:catalog_product_change', args=[obj_id]))


    def query_amazon_listing(self, request, queryset):
        from sp_api.api import Feeds, ListingsItems
        from sp_api.base import Marketplaces, SellingApiException, Credentials
        import tempfile

        # Replace these with your actual credentials
        credentials = dict(
            refresh_token=AMZN_SP_REFRESH_TOKEN,
            lwa_app_id=AMZN_SP_LWA_APP_ID,
            lwa_client_secret=AMZN_SP_LWA_CLIENT_SECRET,
        )

        # Initialize the ProductTypeDefinitions API client
        feeds = Feeds(credentials=credentials, marketplace=Marketplaces.US)
        listings = ListingsItems(credentials=credentials, marketplace=Marketplaces.US)

        # search all content documents
        try:
            for sd in queryset:
                submissionId = sd.image_caption
                response = listings.get_listings_item(
                    sellerId="A36D1O15HT30RE",  # Replace with your actual seller ID
                    sku=sd.sku,
                    marketplaceIds=[Marketplaces.US.marketplace_id],
                    includedData=["issues","productTypes","summaries","fulfillmentAvailability","offers"]
                )
                print("Submission Status:", response)

                payload = response.payload
                # Define the file path to save the payload (as JSON)
                import json
                file_path = f"{submissionId}.json"

                # Write the payload to the file
                import json
                with open(file_path, 'w') as file:
                    # If payload is a dictionary, write it as JSON
                    json.dump(payload, file, indent=4)

                self.message_user(request, f"processing status {response.payload}")

        except SellingApiException as e:
            print(f"Error submitting feed: {e}")
            self.message_user(request, {e})


    query_amazon_listing.short_description = "Query Amazon Listing"


    # 3. Custom view for the action button on the instance page (handles single object)
    def query_amazon_listing_action(self, request, obj_id):
        # Get the single object by ID and convert it into a queryset
        obj = self.get_object(request, obj_id)
        self.query_amazon_listing(request, [obj])  # Reuse the shared method for one object
        # Use message_user to show the success message at the top of the page
        #self.message_user(request, f"A+ Content created for {obj.name}.")

        # Redirect back to the same change form page after the action
        return redirect(reverse('admin:catalog_product_change', args=[obj_id]))


    # 4. Add the custom view to the URLs for this model admin
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'create-aplus-content/<int:obj_id>/',
                self.admin_site.admin_view(self.create_aplus_content_action),
                name='create_aplus_content'
            ),
            path(
                'publish_to_amazon/<int:obj_id>/',
                self.admin_site.admin_view(self.publish_to_amazon_action),
                name='publish_to_amazon'
            ),
            path(
                'query_amazon_listing/<int:obj_id>/',
                self.admin_site.admin_view(self.query_amazon_listing_action),
                name='query_amazon_listing'
            ),
            path(
                'publish_to_fso_ebay/<int:obj_id>/',
                self.admin_site.admin_view(self.publish_to_fso_ebay_action),
                name='publish_to_fso_ebay'
            ),
            path(
                'publish_to_aao_ebay/<int:obj_id>/',
                self.admin_site.admin_view(self.publish_to_aao_ebay_action),
                name='publish_to_aao_ebay'
            ),
            path(
                'publish_to_walmart/<int:obj_id>/',
                self.admin_site.admin_view(self.publish_to_walmart_action),
                name='publish_to_walmart'
            ),
        ]
        return custom_urls + urls

    def post_to_all_amazons_oldmws(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        mws = MWSConnection(settings.AMAZON_MWS_NA_AccessKeyID,settings.AMAZON_MWS_NA_SecretKey)
        mws.SellerId = settings.AMAZON_MWS_NA_MerchantID
        mws.Merchant = settings.AMAZON_MWS_NA_MerchantID

        # First iteration: Post to US
        feedstr = build_amazon_feed(queryset, "com")
        feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_US_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

        feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
        res = 'Submitted product feed to Amazon.com: ' + str(feed_info)
        self.message_user(request, res)

        # Second iteration: Post to CA
        try:
            feedstr = build_amazon_feed(queryset, "ca")
            feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_CA_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

            feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
            res = 'Submitted product feed to Amazon.ca: ' + str(feed_info)
            self.message_user(request, res)
        except Exception as ex:
            self.message_user(request, "Submitting Feed to Amazon.ca failed")
            pass

        # Third iteration: Post to MX
        feedstr = build_amazon_feed(queryset, "mx")
        feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_MX_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

        feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
        res = 'Submitted product feed to Amazon.mx: ' + str(feed_info)
        self.message_user(request, res)

        # EU connection
        mws = MWSConnection(settings.AMAZON_MWS_EU_AccessKeyID,settings.AMAZON_MWS_EU_SecretKey, host=settings.AMAZON_MWS_EU_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_EU_MerchantID
        mws.Merchant = settings.AMAZON_MWS_EU_MerchantID

        # Fourth iteration: Post to EU
        eu_list = [settings.AMAZON_MWS_UK_MarketPlaceID,settings.AMAZON_MWS_DE_MarketPlaceID,settings.AMAZON_MWS_IT_MarketPlaceID,settings.AMAZON_MWS_FR_MarketPlaceID,settings.AMAZON_MWS_ES_MarketPlaceID]
        eu = True

        feedstr = build_amazon_feed(queryset, "uk")

        for sd in queryset:
            if "nitecore" in sd.brand.name.lower():
                eu_list = [settings.AMAZON_MWS_DE_MarketPlaceID,settings.AMAZON_MWS_IT_MarketPlaceID,settings.AMAZON_MWS_FR_MarketPlaceID,settings.AMAZON_MWS_ES_MarketPlaceID]
                eu = False
                break
        if eu:
            try:
                feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_UK_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

                feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
                res = 'Submitted product feed to Amazon.uk: ' + str(feed_info)
                self.message_user(request, res)
            except Exception as ex:
                self.message_user(request, "Submitting Feed to Amazon.uk failed")
                pass

            try:
                feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_DE_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

                feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
                res = 'Submitted product feed to Amazon.de: ' + str(feed_info)
                self.message_user(request, res)
            except Exception as ex:
                self.message_user(request, "Submitting Feed to Amazon.de failed")
                pass



            try:
                feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                    PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_IT_MarketPlaceID],
                                    content_type='text/plain',
                                    FeedContent=feedstr.encode('utf8'))

                feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
                res = 'Submitted product feed to Amazon.it: ' + str(feed_info)
                self.message_user(request, res)
            except Exception as ex:
                self.message_user(request, "Submitting Feed to Amazon.it failed")
                pass

            try:
                feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_FR_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

                feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
                res = 'Submitted product feed to Amazon.fr: ' + str(feed_info)
                self.message_user(request, res)
            except Exception as ex:
                self.message_user(request, "Submitting Feed to Amazon.fr failed")
                pass

            try:
                feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_ES_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

                feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
                res = 'Submitted product feed to Amazon.es: ' + str(feed_info)
                self.message_user(request, res)
            except Exception as ex:
                self.message_user(request, "Submitting Feed to Amazon.es failed")
                pass

        # Turkey connection
        mws = MWSConnection(settings.AMAZON_MWS_EU_AccessKeyID,settings.AMAZON_MWS_EU_SecretKey, host=settings.AMAZON_MWS_TR_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_EU_MerchantID
        mws.Merchant = settings.AMAZON_MWS_EU_MerchantID

        # Fifth iteration: Post to JP
        feedstr = build_amazon_feed(queryset, "tr")
        try:
            feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                    PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_TR_MarketPlaceID],
                                    content_type='text/plain',
                                    FeedContent=feedstr.encode('utf8'))

            feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
            res = 'Submitted product feed to Amazon.tr: ' + str(feed_info)
            self.message_user(request, res)
        except Exception as ex:
            self.message_user(request, "Submitting Feed to Amazon.tr failed")
            pass



        # JP connection
        mws = MWSConnection(settings.AMAZON_MWS_JP_AccessKeyID,settings.AMAZON_MWS_JP_SecretKey, host=settings.AMAZON_MWS_JP_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_JP_MerchantID
        mws.Merchant = settings.AMAZON_MWS_JP_MerchantID

        # Fifth iteration: Post to JP
        feedstr = build_amazon_feed(queryset, "jp")
        try:
            feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                    PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_JP_MarketPlaceID],
                                    content_type='text/plain',
                                    FeedContent=feedstr.encode('utf8'))

            feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
            res = 'Submitted product feed to Amazon.jp: ' + str(feed_info)
            self.message_user(request, res)
        except Exception as ex:
            self.message_user(request, "Submitting Feed to Amazon.es failed")
            pass


        # AU connection
        mws = MWSConnection(settings.AMAZON_MWS_AU_AccessKeyID,settings.AMAZON_MWS_AU_SecretKey, host=settings.AMAZON_MWS_AU_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_AU_MerchantID
        mws.Merchant = settings.AMAZON_MWS_AU_MerchantID

        # Fifth iteration: Post to JP
        feedstr = build_amazon_feed(queryset, "au")

        try:
            feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                    PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_AU_MarketPlaceID],
                                    content_type='text/plain',
                                    FeedContent=feedstr.encode('utf8'))

            feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
            res = 'Submitted product feed to Amazon.au: ' + str(feed_info)
            self.message_user(request, res)
        except Exception as ex:
            self.message_user(request, "Submitting Feed to Amazon.es failed")
            pass

        # SG and AU, JP share the same keys
        mws = MWSConnection(settings.AMAZON_MWS_SG_AccessKeyID,settings.AMAZON_MWS_SG_SecretKey, host=settings.AMAZON_MWS_SG_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_SG_MerchantID
        mws.Merchant = settings.AMAZON_MWS_SG_MerchantID

        # First iteration: Post to US
        feedstr = build_amazon_feed(queryset, "sg")
        try:
            feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_SG_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

            feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
            res = 'Submitted product feed to Amazon.sg: ' + str(feed_info)
            self.message_user(request, res)
        except Exception as ex:
            self.message_user(request, "Submitting Feed to Amazon.sg failed")
            pass



        """ do not execute this section for now
        while True:
            submission_list = mws.get_feed_submission_list(
                FeedSubmissionIdList=[feed_info.FeedSubmissionId]
            )
            info =  submission_list.GetFeedSubmissionListResult.FeedSubmissionInfo[0]
            id = info.FeedSubmissionId
            status = info.FeedProcessingStatus
            res = res + 'Submission Id: {}. Current status: {}'.format(id, status)

            if (status in ('_SUBMITTED_', '_IN_PROGRESS_', '_UNCONFIRMED_')):
                print ('Sleeping and check again....')
                time.sleep(60)
            elif (status == '_DONE_'):
                feedResult = mws.get_feed_submission_result(FeedSubmissionId=id)
                res = res + feedResult
                break
            else:
                res = res + "Submission processing error. Quit."
                break
            """
        self.message_user(request, res)


    def post_to_amazon_tr(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        mws = MWSConnection(settings.AMAZON_MWS_EU_AccessKeyID,settings.AMAZON_MWS_EU_SecretKey, host=settings.AMAZON_MWS_TR_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_EU_MerchantID
        mws.Merchant = settings.AMAZON_MWS_EU_MerchantID

        # First iteration: Post to US
        feedstr = build_amazon_feed(queryset, "tr")
        feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_TR_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

        feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
        res = 'Submitted product feed to Amazon.tr: ' + str(feed_info)
        self.message_user(request, res)
    post_to_amazon_tr.short_description = "Post To Amazon Turkey"

    def post_to_amazon_se(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        mws = MWSConnection(settings.AMAZON_MWS_EU_AccessKeyID,settings.AMAZON_MWS_EU_SecretKey, host=settings.AMAZON_MWS_SE_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_EU_MerchantID
        mws.Merchant = settings.AMAZON_MWS_EU_MerchantID

        # First iteration: Post to US
        feedstr = build_amazon_feed(queryset, "au")
        feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_SE_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

        feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
        res = 'Submitted product feed to Amazon.se: ' + str(feed_info)
        self.message_user(request, res)
    post_to_amazon_se.short_description = "Post To Amazon Sweden"

    def post_to_amazon_au(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # North America connection
        mws = MWSConnection(settings.AMAZON_MWS_AU_AccessKeyID,settings.AMAZON_MWS_AU_SecretKey, host=settings.AMAZON_MWS_AU_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_AU_MerchantID
        mws.Merchant = settings.AMAZON_MWS_AU_MerchantID

        # First iteration: Post to US
        feedstr = build_amazon_feed(queryset, "au")
        feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_AU_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

        feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
        res = 'Submitted product feed to Amazon.au: ' + str(feed_info)
        self.message_user(request, res)
    post_to_amazon_au.short_description = "Post To Amazon AU"

    def post_to_amazon_sg(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'

        # SG and AU, JP share the same keys
        mws = MWSConnection(settings.AMAZON_MWS_SG_AccessKeyID,settings.AMAZON_MWS_SG_SecretKey, host=settings.AMAZON_MWS_SG_ENDPOINT)
        mws.SellerId = settings.AMAZON_MWS_SG_MerchantID
        mws.Merchant = settings.AMAZON_MWS_SG_MerchantID

        # First iteration: Post to US
        feedstr = build_amazon_feed(queryset, "sg")
        feed = mws.submit_feed( FeedType='_POST_FLAT_FILE_LISTINGS_DATA_',
                                PurgeAndReplace=False, MarketplaceIdList=[settings.AMAZON_MWS_SG_MarketPlaceID],
                                content_type='text/plain',
                                FeedContent=feedstr.encode('utf8'))

        feed_info = feed.SubmitFeedResult.FeedSubmissionInfo
        res = 'Submitted product feed to Amazon.sg: ' + str(feed_info)
        self.message_user(request, res)
    post_to_amazon_sg.short_description = "Post To Amazon SG"


    def export_to_amazon_com_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "com")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_com_feed.short_description = "Export to Amazon.com Feed"

    def export_to_amazon_ca_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "ca")
        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_ca_feed.short_description = "Export to Amazon.ca Feed"

    def export_to_amazon_mx_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "mx")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_mx_feed.short_description = "Export to Amazon.mx Feed"

    def export_to_amazon_uk_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "eu")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_uk_feed.short_description = "Export to Amazon.co.uk Feed"

    def export_to_amazon_jp_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "jp")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_jp_feed.short_description = "Export to Amazon.JP Feed"

    def export_to_amazon_au_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "au")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_au_feed.short_description = "Export to Amazon.AU Feed"

    def export_to_amazon_ae_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "ae")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_ae_feed.short_description = "Export to Amazon.AE Feed"

    def export_to_amazon_sa_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        feedstr = build_amazon_feed(queryset, "sa")

        response.write(feedstr.encode('utf8'))
        return response
    export_to_amazon_sa_feed.short_description = "Export to Amazon.SA Feed"



    def export_to_skuvault(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=skuvault_feed.csv'
        feedstr = build_skuvault_feed(queryset)

        response.write(feedstr.encode('utf8'))
        return response
    export_to_skuvault.short_description = "Export to Skuvault"


    def export_to_globalindustrial_feed(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=globalindustrial_feed.txt'
        entries = ''
        for sd in queryset:
             entries += '\n'
             entries += sd.add2globalindustrial('com')
        if 'flashlight' in sd.get_department.lower():
            base_template = 'marketplaces/globalindustrial/Flashlight_Template_Base.txt'
        if 'science' in sd.get_department.lower():
            base_template = 'marketplaces/globalindustrial/Lab_Template_Base.txt'
        feedstr = render_to_string(base_template)
        feedstr += entries

        response.write(feedstr.encode('utf8'))
        return response
    export_to_globalindustrial_feed.short_description = "Export to GlobalIndustrial Feed"

    def export_to_jet(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             retStatus = sd.export2jet('com')
             self.message_user(request, sd.name + ": " + retStatus)

    export_to_jet.short_description = "Export to JET"

    def update_jet_price(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             retStatus = sd.updatejetprice('com')
             self.message_user(request, sd.name + ": " + retStatus)

    update_jet_price.short_description = "Update Jet Price"

    def export_to_walmart(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        accessToken = getToken(settings.WM_URL + "token")

        #self.message_user(request, retMsg)

        feedIds = []
        for sd in queryset:
             #retStatus = sd.export2walmart('com')
             retStatus = sd.export2walmart_from_template('com', accessToken)

             self.message_user(request, sd.name + ": " + retStatus)

             feedIds.append(find_between(retStatus, "<ns2:feedId>", "</ns2:feedId>"))
        for feedid in feedIds:
            feedstatus = getfeedstatus(settings.WM_URL, accessToken, feedid)
            self.message_user(request, feedid + ": " + feedstatus)



    export_to_walmart.short_description = "Export to Walmart"

    # 3. Custom view for the action button on the instance page (handles single object)
    def publish_to_walmart_action(self, request, obj_id):
        # Get the single object by ID and convert it into a queryset
        obj = self.get_object(request, obj_id)
        self.export_to_walmart(request, [obj])  # Reuse the shared method for one object
        # Use message_user to show the success message at the top of the page
        #self.message_user(request, f"A+ Content created for {obj.name}.")

        # Redirect back to the same change form page after the action
        return redirect(reverse('admin:catalog_product_change', args=[obj_id]))

    def additem_to_sandbox_ebay(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             #retStatus = sd.export2walmart('com')
             retStatus = sd.additem_to_ebay("debug")

             self.message_user(request, sd.name + ": " + retStatus)

    additem_to_sandbox_ebay.short_description = "Additem to Sandbox ebay"

    def additem_to_aa_ebay(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             #retStatus = sd.export2walmart('com')
             retStatus = sd.additem_to_ebay("aa")

             self.message_user(request, "Andrew-Amanda-Outdoors: " + sd.name + ": " + retStatus)

    additem_to_aa_ebay.short_description = "Additem to Andrew_Amanda_Outdoors ebay"

    # 3. Custom view for the action button on the instance page (handles single object)
    def publish_to_aao_ebay_action(self, request, obj_id):
        # Get the single object by ID and convert it into a queryset
        obj = self.get_object(request, obj_id)
        self.additem_to_aa_ebay(request, [obj])  # Reuse the shared method for one object
        # Use message_user to show the success message at the top of the page
        #self.message_user(request, f"A+ Content created for {obj.name}.")

        # Redirect back to the same change form page after the action
        return redirect(reverse('admin:catalog_product_change', args=[obj_id]))

    def additem_to_fso_ebay(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             #retStatus = sd.export2walmart('com')
             retStatus = sd.additem_to_ebay("fso")

             self.message_user(request, "Flashlight-Scope-Outdoors: " + sd.name + ": " + retStatus)

    additem_to_fso_ebay.short_description = "Additem to Flashlight_Scope_Outdoors ebay"

    # 3. Custom view for the action button on the instance page (handles single object)
    def publish_to_fso_ebay_action(self, request, obj_id):
        # Get the single object by ID and convert it into a queryset
        obj = self.get_object(request, obj_id)
        self.additem_to_fso_ebay(request, [obj])  # Reuse the shared method for one object
        # Use message_user to show the success message at the top of the page
        #self.message_user(request, f"A+ Content created for {obj.name}.")

        # Redirect back to the same change form page after the action
        return redirect(reverse('admin:catalog_product_change', args=[obj_id]))

    def additem_to_both_ebays(self, request, queryset):
        ProductAdmin.additem_to_aa_ebay(self, request, queryset)
        ProductAdmin.additem_to_fso_ebay(self, request, queryset)

    additem_to_both_ebays.short_description = "Additem to Both ebays"

    def get_item_from_walmart(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             #retStatus = sd.export2walmart('com')
             retStatus = sd.walmart_get_item('com')

             self.message_user(request, sd.name + ": " + retStatus)

    get_item_from_walmart.short_description = "Get an Item from Walmart"


    def uploadimages_to_jet(self, request, queryset):
        response = HttpResponse(content_type='text/tab-separated-values')
        response['Content-Disposition'] = 'attachment; filename=amazon_feed.txt'
        for sd in queryset:
             retStatus = sd.uploadimages2jet('com')
             self.message_user(request, sd.name + ": " + retStatus)

    export_to_jet.short_description = "Export to JET"



    def copy_to_a_new_product(self, request, queryset):
       # sd is an instance of SemesterDetails
       for sd in queryset:
            sd_copy = copy.copy(sd) # (2) django copy object
            sd_copy.id = None   # (3) set 'id' to None to create new object

            # zero out enrollment numbers.
            # (6) Use __dict__ to access "regular" attributes (not FK or M2M)
            from django.utils.crypto import get_random_string
            for attr_name in ['name', 'slug', 'sku', 'modelNumber']:
                sd_copy.__dict__.update({ attr_name : "changeme_" + get_random_string(10)})

            sd_copy.save()    # initial save

            # (4) copy M2M relationship: instructors
            for category in sd.categories.all():
                sd_copy.categories.add(category)

            # (5) copy M2M relationship: requirements_met
            for sub in sd.subcategory.all():
                sd_copy.subcategory.add(sub)

            sd_copy.save()  # (7) save the copy to the database for M2M relations

            for ta in sd.topattributes_set.all():
                ta_copy = copy.copy(ta)
                ta_copy.id = None
                ta_copy.product = sd_copy
                ta_copy.save()

            for ai in sd.additionalimages_set.all():
                ai_copy = copy.copy(ai)
                ai_copy.id = None
                ai_copy.product = sd_copy
                ai_copy.save()


    copy_to_a_new_product.short_description = "Copy to a new product"




# registers your product model with the admin site
admin.site.register(Product, ProductAdmin)

class DepartmentResource(resources.ModelResource):
    class Meta:
        model = Department
        import_id_fields = ['slug']

class DepartmentAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories
    resource_class = DepartmentResource
    list_display = ('name', 'created_at', 'updated_at', 'ranking',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = []

    fieldsets = (
                 ('SEO Tags', {'fields': (('seo_title'),('meta_description','meta_keywords'),('seo_og_title','seo_og_description'), ('seo_h1_tag'),)}),
                 ('Basics', {'fields': (('name','slug',),('description'),('is_active','image',),('ranking'))}),
                )


    list_editable = ('ranking',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Department, DepartmentAdmin)

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        import_id_fields = ['slug']


class CategoryAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories
    resource_class = CategoryResource
    list_display = ('name', 'department','ebay_categoryid','created_at', 'updated_at', 'ranking','is_active',)
    list_display_links = ('name',)
    list_per_page = 20
    list_filter = ('department',)
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = []

    fieldsets = (
                 ('SEO Tags', {'fields': (('seo_title'),('meta_description','meta_keywords'),('seo_og_title','seo_og_description'), ('seo_h1_tag'),)}),
                 ('Basics', {'fields': (('name','slug','ebay_categoryid'),('description'),('is_active',),('department', 'ranking'))}),
                )


    list_editable = ('ranking','ebay_categoryid', 'is_active',)

    # sets up slug to be generated from category name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Category, CategoryAdmin)

class SubCategoryResource(resources.ModelResource):
    class Meta:
        model = SubCategory
        import_id_fields = ['slug']


class SubCategoryAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories
    resource_class = SubCategoryResource
    list_display = ('name', 'created_at', 'updated_at', 'category','is_active',)
    list_display_links = ('name',)
    list_filter = ('category',)

    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = []

    fieldsets = (
                 ('SEO Tags', {'fields': (('seo_title'),('meta_description','meta_keywords'),('seo_og_title','seo_og_description'), ('seo_h1_tag'),)}),
                 ('Basics', {'fields': (('name','slug','display_name'),('description'),('is_active','image',),('category', 'ranking'))}),
                )


    # sets up slug to be generated from brand name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(SubCategory, SubCategoryAdmin)


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'title', 'date', 'rating', 'is_approved')
    list_per_page = 20
    list_filter = ('product', 'user', 'is_approved')
    ordering = ['date']
    search_fields = ['user','content','title']

admin.site.register(ProductReview, ProductReviewAdmin)

class BrandResource(resources.ModelResource):
    class Meta:
        model = Brand
        import_id_fields = ['slug']


class BrandAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories

    resource_class = BrandResource
    list_display = ('name', 'created_at', 'updated_at', 'ranking', 'is_active',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = []
    list_editable = ('ranking','is_active',)

    fieldsets = (
                 ('SEO Tags', {'fields': (('seo_title'),('meta_description','meta_keywords'),('seo_og_title','seo_og_description'), ('seo_h1_tag'),)}),
                 ('Basics', {'fields': (('name','slug'),('description'),('image',),('is_active','ranking',),('department', 'department_2','department_3','department_4',))}),
                )


    # sets up slug to be generated from brand name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Brand, BrandAdmin)

class BrandSeriesResource(resources.ModelResource):
    class Meta:
        model = Series
        import_id_fields = ['slug']


class BrandSeriesAdmin(ImportExportModelAdmin):
    #sets up values for how admin site lists categories

    resource_class = BrandSeriesResource
    #sets up values for how admin site lists categories
    list_display = ('name', 'display_name', 'is_active', 'ranking', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_editable = ('display_name', 'is_active', 'ranking',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = []

    fieldsets = (
                 ('SEO Tags', {'fields': (('seo_title'),('meta_description','meta_keywords'),('seo_og_title','seo_og_description'), ('seo_h1_tag'),)}),
                 ('Basics', {'fields': (('name','slug','display_name'),('description'),('is_active','image',),('brand', 'ranking'))}),
                )


    # sets up slug to be generated from brand name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(Series, BrandSeriesAdmin)

class PriceRangeAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'description', 'min_price', 'max_price', 'is_active',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'min_price', 'max_price']
    exclude = []

    # sets up slug to be generated from brand name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(PriceRange, PriceRangeAdmin)

class BrightnessRangeAdmin(admin.ModelAdmin):
    #sets up values for how admin site lists categories
    list_display = ('name', 'description', 'min_lumens', 'max_lumens', 'is_active',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'min_lumens', 'max_lumens']
    exclude = []

    # sets up slug to be generated from brand name
    prepopulated_fields = {'slug' : ('name',)}

admin.site.register(BrightnessRange, BrightnessRangeAdmin)


from django.contrib.admin import DateFieldListFilter
from ajax_select import make_ajax_form
from ajax_select.admin import AjaxSelectAdmin

class DealOfTheDayAdmin(AjaxSelectAdmin):
    #sets up values for how admin site lists categories
    list_display = ('title','start_date', 'end_date', 'original_price', 'deal_price', 'view_on_site', 'sold_date', 'purchased_by',)
    list_editable = ('start_date', 'end_date', 'deal_price',)
    list_display_links = ('title',)
    list_filter = ('brand',('start_date', DateFieldListFilter))
    list_per_page = 20
    ordering = ['-end_date']
    search_fields = ['title', 'description', 'start_date', 'end_date']
    exclude = []

    readonly_fields = ('original_price', 'clearance_price',)

    form = make_ajax_form(DealOfTheDay,{'product':'products'})

    actions = ['post_to_facebook_twitter']

    def get_actions(self, request):
        actions = super(DealOfTheDayAdmin, self).get_actions(request)
        #del actions['delete_selected']
        return actions
    def view_on_site(self, obj):
        return format_html("<a target='_blank' href='{url}'>View</a>", url=obj.product.get_absolute_url())
    view_on_site.allow_tags = True
    view_on_site.short_description = "View On Site"

    def post_to_facebook_twitter(self, request, queryset):
        for obj in queryset:
            twitterStatus = obj.post2twitter()

        if twitterStatus:
           self.message_user(request, "The deal was successfully posted to twitter.")
        else:
           self.message_user(request, "The deal was failed to post to twitter.")

    post_to_facebook_twitter.short_description = "Post to facebook and twitter"

    def original_price(self, obj):
        return obj.product.price

    def clearance_price(self, obj):
        if obj.product.clearance:
            return obj.product.clearance_price
        else:
            return None



admin.site.register(DealOfTheDay, DealOfTheDayAdmin)

class AccessoriesProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'all_accessories', 'all_products',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name']
    exclude = []
    filter_horizontal = ('accessories', 'products',)


admin.site.register(accessory_product, AccessoriesProductAdmin)

class ProductAssociationAdmin(admin.ModelAdmin):
    list_display = ('title', 'all_products',)
    list_display_links = ('title',)
    list_per_page = 20
    ordering = ['title']
    search_fields = ['title']
    exclude = []
    filter_horizontal = ('products',)



admin.site.register(ProductAssociation, ProductAssociationAdmin)
