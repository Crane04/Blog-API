from django.urls import path
from .views import *

urlpatterns = [

    path("posts/<str:custom_id>", PostRetrieveUpdateDeleteView.as_view()),
    path("posts/api/<str:api_key>", PostListCreateView.as_view()),
    path("test", TestToken.as_view()),
    path("testing", TestApi.as_view())
]