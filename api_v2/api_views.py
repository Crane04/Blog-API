from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.views import View
from rest_framework import status
from app.models import UserConfig, UserSites, UserScript
from .utils import GetUserPosts_, GetPost_
# Create your views here.


class MainApiView(GenericAPIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        user_sites = get_object_or_404(UserSites, user = request.user)

        current_url = request.GET.get("location")
        if user_sites.blog_page in current_url:
            return GetUserPosts_(request)

        elif user_sites.individual_blog_post in current_url:
            
            return GetPost_(request)
        else:
            return Response({"details":"error occured!"}, status = status.HTTP_400_BAD_REQUEST)


