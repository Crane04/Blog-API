from django.urls import path
from .api_views import MainApiView
from .views import DocumentationViewV2, ApiPageView

# api paths
urlpatterns = [
    path("main", MainApiView.as_view()),
    path("", DocumentationViewV2.as_view()),
    path("api-v2", ApiPageView.as_view())
]