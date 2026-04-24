from django.urls import reverse_lazy
from ecomstore.marketing.models import *
from django import forms

def strip_non_numbers(data):
    """ gets rid of all non-number characters """
    non_numbers = re.compile('\D')
    return non_numbers.sub('', data)

class GroupBuyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GroupBuyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['size'] = '30'

        self.fields['state'].widget.attrs['size'] = '20'
        self.fields['country'].widget.attrs['size'] = '1'
        self.fields['reason'].label = 'Comment'

        self.fields['state'].widget.attrs['placeholder'] = 'State or Province'
        self.fields['quantity'].widget.attrs['placeholder'] = '1,2,3,4, ...'
        self.fields['quantity'].initial = 1

    class Meta:
        model = GroupBuyParticipant 
        exclude = ('p','email',)

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        stripped_quantity = strip_non_numbers(quantity)
        if len(stripped_quantity) < 1:
            raise forms.ValidationError('Enter a valid integer')
        return self.cleaned_data['quantity']


