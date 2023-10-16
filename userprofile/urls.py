from django.urls import path
from .views import *

urlpatterns = [
    path("signup", signup.as_view()),
    path("login", LoginView.as_view()),
    path("test_token", test_token.as_view())
]