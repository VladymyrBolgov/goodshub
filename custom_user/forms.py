from django import forms
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.utils.translation import gettext_lazy as _
from custom_user.models import CustomUser
from main_app.exceptions import ValidationError


class CustomUserCreationForm(UserCreationForm):
    """
    A form for user registration.

    Extends Django's built-in "UserCreationForm".
    The form takes the user's username, email, password and password confirmation as input.
    """

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, strip=False,)

    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput, strip=False,)

    phone_number = PhoneNumberField(widget=forms.TextInput(attrs={'placeholder': _('+380123456789')}),
                                    label=_("Phone number"))

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'phone_number']
        help_texts = {'username': None,
                      'email': None}

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request', None)
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('username'):
            # self.add_error('username', "The username Error!")
            # messages.error(self.request, 'You must type the Username!')
            raise forms.ValidationError('This field is required!')
        if not cleaned_data.get('first_name'):
            # self.add_error('first_name', "The first name Error!")
            # messages.error(self.request, 'You must type the first name!')
            raise forms.ValidationError('This field is required!')
        if not cleaned_data.get('last_name'):
            # self.add_error('last_name', "The last name Error!")
            # messages.error(self.request, 'You must type the last name!')
            raise forms.ValidationError('This field is required!')
        if not cleaned_data.get('email'):
            # self.add_error('email', "The email Error!")
            # messages.error(self.request, 'You must type the email!')
            raise forms.ValidationError('This field is required!')
        if not cleaned_data.get('phone_number'):
            # self.add_error('phone_number', "The phone number Error!")
            # messages.error(self.request, 'You must type the phone number!')
            raise forms.ValidationError('This field is required!')

        username = self.cleaned_data.get('username')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        phone_number = self.cleaned_data.get('phone_number')

        if len(username) <= 3:
            # self.add_error('username', 'The username Error!')
            # messages.error(self.request, 'The username must be more then 3 symbol!')
            raise forms.ValidationError('The username must be more then 3 symbol!')
        if len(first_name) <= 3:
            # self.add_error('first_name', 'The username Error!')
            # messages.error(self.request, 'The first_name must be more then 3 symbol!')
            raise forms.ValidationError('The first_name must be more then 3 symbol!')
        if len(last_name) <= 3:
            # self.add_error('last_name', 'The last_name Error!')
            # messages.error(self.request, 'The last_name must be more then 3 symbol!')
            raise forms.ValidationError('The last_name must be more then 3 symbol!')

        try:
            if CustomUser.objects.filter(username__iexact=username).exists():
                raise forms.ValidationError('User with this name already exists!')
                #self.add_error('username', 'User with this name already exists!')
            if CustomUser.objects.filter(email__iexact=email).exists():
                raise forms.ValidationError('Email is already registered!')
                #self.add_error('email', 'Email is already registered!')
            if CustomUser.objects.filter(phone_number__iexact=phone_number).exists():
                raise forms.ValidationError('Phone_number is already registered!')
                #self.add_error('phone_number', 'Phone_number is already registered!')

        except KeyError:
            raise ValidationError("Required fild is absence!")




