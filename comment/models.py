from django.db import models
from django.urls import reverse

from product.models import Product
from custom_user.models import CustomUser

# Create your models here.


class Comment(models.Model):
    to_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=300, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.author

    # def get_absolute_url(self):
    #     return reverse('comment:comment')

