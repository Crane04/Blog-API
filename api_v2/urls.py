from django.urls import path
from .views import MainApiView, GenerateScript

# api paths
urlpatterns = [
    path("main", MainApiView.as_view()),
    path("gn", GenerateScript.as_view())
]