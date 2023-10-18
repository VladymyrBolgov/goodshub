from django.db.models import Count
from main_app.models import Category

menu = [{'title': "Main page", 'url_name': 'main_page'},
        {'title': "Registration", 'url_name': 'user:registration'},
        {'title': "Favorites", 'url_name': 'favorites:list_favorites'},
        {'title': "Add product", 'url_name': 'product:create_product'},
        #{'title': "Account", 'url_name': 'create_product'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.all()
        context['menu'] = menu
        context['categories'] = categories
        if 'category_selected' not in context:
            context['category_selected'] = 0
        return context

