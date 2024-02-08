from django.urls import path
from .views import TestHeader, TestPreloader, TestFetchData, MainApiView, GenerateScript

# api paths
urlpatterns = [
    path("test", TestHeader.as_view()),
    path("test2", TestPreloader.as_view()),
    path("test3", TestFetchData.as_view()),
    path("main", MainApiView.as_view()),
    path("gn", GenerateScript.as_view())
]