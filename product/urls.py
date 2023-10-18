from django.urls import path
from product.views import ProductCreateView, UpdateProductView, ProductDetailView, ProductDeleteView

app_name = 'product'

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('change/<slug:product_slug>/', UpdateProductView.as_view(), name="change_product"),
    path('detail/<slug:product_slug>/', ProductDetailView.as_view(), name="detail_product"),
    path('delete/<slug:product_slug>/', ProductDeleteView.as_view(), name="delete_product"),
]

