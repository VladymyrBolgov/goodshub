from django.urls import path
from comment.views import CommentCreateView

app_name = 'comment'

urlpatterns = [
    path('create/<int:product_id>/', CommentCreateView.as_view(), name="create_comment"),
    #path('change/<int:pk>/', CommentUpdateView.as_view(), name="change_product"),
    #path('delete/<int:pk>/', CommentDeleteView.as_view(), name="detail_product"),

]

