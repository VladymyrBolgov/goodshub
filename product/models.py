from django.db import models
from main_app.models import Category
from custom_user.models import CustomUser
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    seller = models.ForeignKey(CustomUser, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    model = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    # ОГРАНИЧИТЬ ДЛИНУ?
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    promotion = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        indexes = [models.Index(fields=['id', 'slug']),
                   models.Index(fields=['title']),
                   models.Index(fields=['-created'])]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:detail_product', kwargs={'product_slug': self.slug})

