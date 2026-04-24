from django import forms
from django.contrib.auth.forms import UserCreationForm
from ecomstore.accounts.models import UserProfile
from django.contrib.auth import authenticate, login

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        
class RegistrationForm(UserCreationForm):
    """ subclass of Django's UserCreationForm, to handle customer registration with a required minimum length
    and password strength. Also contains an additional field for capturing the email on registration.
    
    """
    """
    password1 = forms.RegexField(label="Password", regex=r'^(?=.*\W+).*$', 
                                 help_text='Password must be six characters long and contain at least one non-alphanumeric character.',
                                 widget=forms.PasswordInput, min_length=6)
    password2 = forms.RegexField(label="Password confirmation", regex=r'^(?=.*\W+).*$',
                                 widget=forms.PasswordInput, min_length=6)
    email = forms.EmailField(max_length="50")
    """
    password1 = forms.RegexField(label="Password", regex=r'^[\w.@+-]+$', 
                                 help_text='Password must be six characters long and Letters, digits and @/./+/-/_ only.',
                                 widget=forms.PasswordInput, min_length=6)
    password2 = forms.RegexField(label="Password confirmation", regex=r'^[\w.@+-]+$',
                                 widget=forms.PasswordInput, min_length=6)
    email = forms.EmailField(max_length="50")


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
