from django.urls import path
from favorites.views import FavoritesCreateView, FavoritesListView, FavoritesDeleteView

app_name = 'favorites'

urlpatterns = [
    path('create/<slug:product_slug>/', FavoritesCreateView.as_view(), name="create_favorites"),
    path('list/', FavoritesListView.as_view(), name="list_favorites"),
    path('delete/<int:pk>/', FavoritesDeleteView.as_view(), name="delete_favorites"),
]

