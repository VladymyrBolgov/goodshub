from django import forms
from django.contrib import messages
from product.models import Product
from main_app.models import Category
from custom_user.models import CustomUser
from main_app.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['category', 'title', 'model', 'image', 'quantity', 'description', 'price']

    def __init__(self, *args, **kwargs):
        if 'request' in kwargs:
            self.request = kwargs.pop('request')
        if 'slug' in kwargs:
            self.category_id = kwargs.pop('slug')
        return super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        try:
            ## валидация модели и количества !!!!!
            if not cleaned_data.get('category'):
                self.add_error('category', "The category field Error!")
                messages.error(self.request, 'You must type the category!')
                raise forms.ValidationError('This field is required!')
            if not cleaned_data.get('title'):
                self.add_error('title', "The title field Error!")
                messages.error(self.request, 'You must type the title!')
                raise forms.ValidationError('This field is required!')
            if not cleaned_data.get('description'):
                self.add_error('description', "The description field Error!")
                messages.error(self.request, 'You must type the description!')
                raise forms.ValidationError('This field is required!')
            if not cleaned_data.get('price'):
                self.add_error('price', "The price field Error!")
                messages.error(self.request, 'You must type the price!')
                raise forms.ValidationError('This field is required!')

            title = self.cleaned_data.get('title')
            description = self.cleaned_data.get('description')
            price = self.cleaned_data.get('price')

            if len(title) <= 5:
                self.add_error('title', 'The title field Error!')
                messages.error(self.request, 'The title field must be more then 5 symbol!')
            if len(description) <= 8:
                self.add_error('description', 'The description field Error!')
                messages.error(self.request, 'The description must be more then 8 symbol!')
            if price < 1:
                self.add_error('price', 'The price field Error!')
                messages.error(self.request, 'The price must be more then 0!')

        except Category.DoesNotExist:
            self.add_error(None, 'The object existing Error!')
            messages.error(self.request, 'This category does not exist!')
        except CustomUser.DoesNotExist:
            self.add_error(None, 'The object existing Error!')
            messages.error(self.request, 'This user does not exist!')














