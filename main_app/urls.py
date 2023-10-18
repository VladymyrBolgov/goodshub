from django.urls import path
from main_app.views import LoginUser, LogoutUser, ProductCategory

app_name = 'marketplace'

urlpatterns = [
    path('login/', LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name="logout"),
    path('category/<slug:category_slug>/', ProductCategory.as_view(), name='category'),
]
