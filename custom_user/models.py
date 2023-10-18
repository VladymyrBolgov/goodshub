from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(_("username"),
                                max_length=50,
                                unique=True,
                                help_text=_("Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only."),
                                error_messages={"unique": _("A user with that username already exists.")},
                                blank=False,
                                null=False,)
    first_name = models.CharField(_("first name"), max_length=100, blank=False, null=False,)
    last_name = models.CharField(_("last name"), max_length=150, blank=False, null=False,)
    email = models.EmailField(_("email address"), unique=True, blank=False, null=False,)
    phone_number = PhoneNumberField(_("phone number"), unique=True, null=False, blank=False,)

    class Meta:
        ordering = ['username']
        indexes = [models.Index(fields=['id']),
                   models.Index(fields=['username'])]

    def __str__(self):
        return self.username
