from django.contrib import admin
from product.models import Product
from main_app.models import Category
from comment.models import Comment
from custom_user.models import CustomUser


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'model', 'image', 'description', 'price', 'quantity', 'available', 'created',
                    'updated', 'promotion']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['to_product', 'author', 'content', 'created_at']
    #list_filter = ['author', 'created_at']
    #list_editable = ['price', 'available']


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'phone_number']
    list_filter = ['username', 'email']
    #list_editable = ['price', 'available']
