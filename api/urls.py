from django.urls import path
from .views import *

urlpatterns = [

    path("action/<str:unique_id>", PostRetrieveUpdateDeleteView.as_view()),
    path("posts", PostListCreateView.as_view()),
]