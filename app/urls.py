from django.urls import path
from .views import *

urlpatterns = [
    path("dashboard/admin", AdminPageView.as_view(), name = "admin-page"),
    path("dashboard/admin/edit/<str:post_id>", PostEditView.as_view(), name = "edit-page")
]