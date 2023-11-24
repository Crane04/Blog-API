from django.urls import path
from .views import *

urlpatterns = [
    path("comment/<str:api_key>/<str:id>", CommentView.as_view(), name = "comments")
]