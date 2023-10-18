from django.urls import path
from custom_user.views import RegistrationNewUser

app_name = 'user'

urlpatterns = [
    path('registration/', RegistrationNewUser.as_view(), name="registration"),
    #path('registration/', RegistrationNewUser.as_view(), name="registration"),

]
