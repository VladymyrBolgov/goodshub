from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from product.models import Product
from comment.forms import CommentCreationForm
from comment.models import Comment


# Create your views here.


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    success_url = '/'
    template_name = 'comment/create.html'

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs.update({'request': self.request,
    #                    #'slug': self.kwargs['product_slug'],
    #                    'pk': self.kwargs['product_id']})
    #     return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product = Product.objects.get(id=self.kwargs['product_id'])
        obj.to_product = product
        obj.save()
        return super().form_valid(form=form)

    def form_invalid(self, form):
        return HttpResponseRedirect('/')

    """
    !!!! Нужно подумать как сделать редирект на страницу с которой пришел запрос
    """







