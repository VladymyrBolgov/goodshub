from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView
from custom_user.models import CustomUser
from custom_user.forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.


class RegistrationNewUser(CreateView):
    """
    View for registration of new user page.
    """
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('marketplace:login')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs

    # def form_invalid(self, form):
    #     return HttpResponseRedirect('user/registration/')
