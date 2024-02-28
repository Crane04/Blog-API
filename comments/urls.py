from django.urls import path
from .views import *

urlpatterns = [
    path("comment/<str:api_key>/<str:id>", CommentView.as_view(), name = "comments"),
    path("commentv2/<str:id>", CommentViewV2.as_view(), name = "commentsv2")
]