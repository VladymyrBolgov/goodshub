from django import forms
from django.contrib import messages
from comment.models import Comment
from favorites.models import Favorites
from product.models import Product
from custom_user.models import CustomUser
from main_app.exceptions import ValidationError


# class FavoritesCreationForm(forms.ModelForm):
#     class Meta:
#         model = Favorites
#         fields = '__all__'
