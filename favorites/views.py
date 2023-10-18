from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, DeleteView, ListView
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
#from favorites.forms import FavoritesCreationForm
from favorites.models import Favorites
from main_app.permission_mixins import UserLoginRequiredMixin
from product.models import Product


# Create your views here.


class FavoritesCreateView(UserLoginRequiredMixin, View):
    model = Favorites
    slug_url_kwarg = 'product_slug'
    success_url = '/'
    template_name = 'favorites/create.html'

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(slug=self.kwargs['product_slug'])
        if Favorites.objects.filter(Q(user=self.request.user) & Q(product=product)).exists():
            return HttpResponseRedirect('/')
        Favorites(user=self.request.user, product=product).save()
        return HttpResponseRedirect('/')


class FavoritesListView(ListView):
    model = Favorites
    template_name = 'favorites/list.html'
    #paginate_by = 14
    queryset = Favorites.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class FavoritesDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Favorites
    pk_url_kwarg = 'pk'
    template_name = 'favorites/delete.html'
    success_url = '/favorites/list/'
    queryset = Favorites.objects.all()

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        pk = self.kwargs.get('pk') or self.request.GET.get('pk')
        queryset = queryset.filter(id=pk)
        obj = queryset.get()
        if obj.user != self.request.user:
            raise Http404(_("You don't own this object"))
        return obj


