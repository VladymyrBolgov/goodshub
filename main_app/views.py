from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.urls import reverse_lazy
from django.views.generic import ListView
from main_app.models import Category
from main_app.utils import DataMixin
from product.models import Product
from main_app.forms import UserChoiceFilterForm


# Create your views here.


class LoginUser(LoginView):
    """
    View for user signup.
    """
    template_name = 'marketplace/login.html'
    next_page = '/'


class LogoutUser(LogoutView):
    """
    View for logout.
    """
    next_page = reverse_lazy('marketplace:login')


class MarketplaceListView(DataMixin, ListView):
    """
    A view that displays a list of all available product.
    """
    model = Product
    template_name = 'marketplace/main.html'
    #paginate_by = 14
    queryset = Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        search_text = self.request.GET.get('search_text')
        if search_text:
            object_list = Product.objects.filter(Q(title__icontains=search_text) |
                                                 Q(description__icontains=search_text))
        else:
            object_list = Product.objects.all()
        return object_list


class ProductCategory(ListView):
    model = Product
    template_name = 'marketplace/category.html'
    #context_object_name = 'posts'
    #allow_empty = False
    queryset = Product.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(category__slug=self.kwargs['category_slug'])

    def get_ordering(self):
        filter_by = self.request.GET.get('filter_by')
        if filter_by == 'date':
            self.ordering = ['created']
        elif filter_by == 'price_as':
            self.ordering = ['price']
        elif filter_by == 'price_des':
            self.ordering = ['-price']
        elif filter_by == 'name':
            self.ordering = ['title']
        elif filter_by == 'action':
            self.ordering = ['-promotion']
        return self.ordering

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort'] = UserChoiceFilterForm
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

