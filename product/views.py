from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from django.utils.translation import gettext_lazy as _
from comment.models import Comment
from main_app.permission_mixins import UserLoginRequiredMixin
from product.forms import ProductCreationForm
from product.models import Product
from main_app.models import Category
from comment.forms import CommentCreationForm


# Create your views here.


class ProductCreateView(UserLoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductCreationForm
    success_url = '/'
    template_name = 'product/create.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.seller = self.request.user
        obj.slug = slugify(obj.title)
        obj.save()
        return super().form_valid(form=form)

    def form_invalid(self, form):
        return HttpResponseRedirect('/product/create/')


class UpdateProductView(UserLoginRequiredMixin, UpdateView):
    """
    View for changing exists MovieSession object. Subclasses SuperUserRequiredMixin
    to ensure that only superusers can update MovieSession objects.
    """
    model = Product
    form_class = ProductCreationForm
    success_url = '/'
    template_name = 'product/change.html'
    # slug_field = 'url'
    slug_url_kwarg = 'product_slug'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'request': self.request,
            'slug': self.kwargs['product_slug']
        })
        return kwargs

    def get_queryset(self):
        """
        The method is overridden so that the authenticated user receives information only about himself
        :return: filtered by a specific user queryset
        """
        return super().get_queryset().filter(seller=self.request.user)


class ProductDetailView(UserLoginRequiredMixin, DetailView):
    """
    A view that displays the details of a single Product.
    A form with a tickets purchase is also available on the page.
    Subclasses UserLoginRequiredMixin to ensure that only authenticated user has access to the page.
    """
    model = Product
    template_name = 'product/detail.html'
    slug_url_kwarg = 'product_slug'
    extra_context = {"comment_form": CommentCreationForm()}

    def get_object(self, queryset=None):
        """
        The method overridden to get a specific Product object
        :param queryset:
        :return: Product object
        """
        if queryset is None:
            queryset = self.get_queryset()
        product_slug = self.kwargs.get('product_slug') or self.request.GET.get('product_slug')
        queryset = queryset.filter(slug=product_slug)
        obj = queryset.get()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_slug = self.kwargs.get('product_slug') or self.request.GET.get('product_slug')
        get_product = Product.objects.get(slug=product_slug)
        get_comment = Comment.objects.filter(to_product=get_product.id)
        context.update({'comments': get_comment})
        return context


class ProductDeleteView(UserLoginRequiredMixin, DeleteView):
    model = Product
    slug_url_kwarg = 'product_slug'
    template_name = 'product/delete.html'
    success_url = '/'
    queryset = Product.objects.all()

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        product_slug = self.kwargs.get('product_slug') or self.request.GET.get('product_slug')
        queryset = queryset.filter(slug=product_slug)
        obj = queryset.get()
        if obj.seller != self.request.user:
            raise Http404(_("You don't own this object"))
        return obj

