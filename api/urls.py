from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("get-posts", get_posts),
    path("create-post", create_post),
    path("delete-post", delete_post),
    path("get_one_post/<str:pk>", get_one_post),
    path("update_post", update_post)
]