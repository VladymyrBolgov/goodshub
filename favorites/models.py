from django.db import models
from django.urls import reverse

from custom_user.models import CustomUser
from product.models import Product

# Create your models here.


class Favorites(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

