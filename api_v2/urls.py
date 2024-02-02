from django.urls import path
from .views import GetUserPosts, GetPost, TestHeader

urlpatterns = [
    path("all-posts", GetUserPosts.as_view(), name="all-posts"),
    path("post/<str:id>", GetPost.as_view(), name="post"),
    path("test", TestHeader.as_view())
]