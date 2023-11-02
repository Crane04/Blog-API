from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("dashboard/admin/", login_required(AdminPageView.as_view()), name = "admin-page"),
    path("dashboard/admin/edit/<str:post_id>", PostEditView.as_view(), name = "edit-page"),
    path("documentation", DocumentationView.as_view(), name = "documentaion-page"),
    path("", DocumentationView.as_view()),
    path("dashboard/api", login_required(ApiPageView.as_view())),
    path("mn", rest)
]