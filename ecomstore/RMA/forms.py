from django import forms
from tagging.models import Tag
from django.contrib import messages


from django import forms
from django.forms.widgets import ClearableFileInput
from .models import *


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

class RMAImagesForm(forms.ModelForm):
    class Meta:
        model = RMAImages
        fields = ['a_image', 'image_caption', 'return_authorization']
        widgets = {
            'a_image': BulkImageUploadWidget(),  # Use custom widget to allow multiple uploads
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Loop over all files in self.files, focusing on those with 'a_image'
        if not instance.pk:
            for key in self.files:
                if key.startswith('rmaimages_set') and 'a_image' in key:
                    files = self.files.getlist(key)
                    print(f"Files for field {key}: {files}")  # Debugging output

                    if len(files) > 0:
                        for file in files:
                            # Save each file as an instance of AdditionalImages
                            image_instance = RMAImages(
                                return_authorization=self.instance.return_authorization,
                                image_caption=self.cleaned_data.get('image_caption'),
                                a_image=file
                            )
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

class ActionsTakenForm(forms.ModelForm):
    class Meta:
        model = actions_taken
        fields = ['last_updated','a_image', 'image_caption', 'return_authorization']
        widgets = {
            'a_image': BulkImageUploadWidget(),  # Use custom widget to allow multiple uploads
        }

    def save(self, commit=True):

        instance = super().save(commit=False)

        # Print out all elements in self.files for debugging
        if not instance.pk:
            print("********** Printing all elements in self.files **********")
            for key, value in self.files.items():
                print(f"Key: {key}, Value: {value}")

            # Loop over all files in self.files, focusing on those with 'a_image'
            for key in self.files:
                if key.startswith('actions_taken_set') and 'a_image' in key:
                    files = self.files.getlist(key)
                    print(f"Files for field {key}: {files}")  # Debugging output

                    if len(files) > 0:
                        for file in files:
                            # Save each file as an instance of AdditionalImages
                            image_instance = actions_taken(
                                return_authorization=self.instance.return_authorization,
                                image_caption=self.cleaned_data.get('image_caption'),
                                a_image=file
                            )
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
