from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def val_email(value):
    c = 'йцукенгшщзхъфывапролджэячсмитьбю'
    for i in value:
        if i in c:
            raise ValidationError(
                _('%(value)s is not an email'),
                params={'value': value},
            )


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    field_order = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': 'Email address', 'type': "email", 'name': 'popup_input'}))
    code = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'b-popup_input_code', 'placeholder': 'Code', 'type': "text", 'disabled': 'true'}))


class OrderingForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': 'name (optional)', 'type': "text"}))
    tel = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': '88005553535', 'type': "tel"}))
    city = forms.ChoiceField(required=True, choices=((1, 'Moscow'), (2, 'St. Petersburg'),))
    street = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': 'street', 'type': "text"}))
    home = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': 'home', 'type': "text"}))
    flat = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': 'flat', 'type': "text"}))
    notes = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'b-popup_input', 'placeholder': 'notes (optional)', 'type': "text"}))


