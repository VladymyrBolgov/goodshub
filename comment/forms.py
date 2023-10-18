from django import forms
from django.contrib import messages
from comment.models import Comment
from product.models import Product
from custom_user.models import CustomUser
from main_app.exceptions import ValidationError


class CommentCreationForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    # def __init__(self, *args, **kwargs):
    #     if 'request' in kwargs:
    #         self.request = kwargs.pop('request')
    #     if 'pk' in kwargs:
    #         self.product_id = kwargs.pop('pk')
    #     return super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get('content'):
            #self.add_error('category', "The content field Error!")
            #messages.error(self.request, 'You must type the content!')
            raise forms.ValidationError('This field is required!')
        try:
            content = self.cleaned_data.get('content')
            if len(content) < 10:
            #self.add_error('content', 'The title content Error!')
            #messages.error(self.request, 'The content field must be more then 10 symbol!')
                raise forms.ValidationError('This field is required!')
        except Product.DoesNotExist:
            raise ValidationError("Required fild is absence!")
            # self.add_error(None, 'The object existing Error!')
            # messages.error(self.request, 'This category does not exist!')
        except CustomUser.DoesNotExist:
            # self.add_error(None, 'The object existing Error!')
            # messages.error(self.request, 'This user does not exist!')
            raise ValidationError("Required fild is absence!")






