from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseForbidden


class SuperUserRequiredMixin(UserPassesTestMixin):
    """
    A view that checks if the user is a superuser before allowing them to access a protected
    web page. If the user is not a superuser, they will receive a message error.
    """

    def test_func(self):
        """
        A method that checks whether the user is a superuser or not.
        Returns: bool: True if the user is a superuser, False otherwise.
        """
        return self.request.user.is_superuser

    def handle_no_permission(self):
        """
        A method is required for redirecting in case of an attempt to access certain pages without permission
        :return: redirect to login page
        """
        messages.error(self.request, "You don't have permission to do this!")
        return HttpResponseRedirect('/marketplace/login/')


class UserLoginRequiredMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        """
        A method is required for redirecting in case of an attempt to access certain pages without authentication
        :return: redirect to login page
        """
        messages.error(self.request, "You are not login")
        return HttpResponseRedirect('/marketplace/login/')


# class OwnerRequiredMixin(object):
#     def dispatch(self, request, *args, **kwargs):
#         if self.object.author != self.request.user:
#             return HttpResponseForbidden()
#         return super(OwnerRequiredMixin, self).dispatch(request, *args, **kwargs)

