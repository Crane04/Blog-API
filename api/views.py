# Import Dependencies

from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer#, GetPostSerializer
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, SAFE_METHODS, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from app.models import *


class RestrictAccess(BasePermission):
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
    
        return obj.creator

class PostListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):


    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    

    def get(self, request:Request, api_key, *args, **kwargs):
        # Get user Token
        token = get_object_or_404(Token, key = api_key)

        # Get user associated with the token
        user = get_object_or_404(User, username = token.user)

        requesting_url = request.GET.get("url")
        user_urls = get_object_or_404(UserSites, user = token.user)

        print(requesting_url)

        # Filter Posts
        if requesting_url == user_urls.blog_page:
            # All Posts

            data = Post.objects.filter(creator = user)
            
            serialized_data = PostSerializer(data = data,  many = True)
            serialized_data.is_valid()


            return Response({
               "posts": serialized_data.data,
               "individual_page": user_urls.individual_blog_post
            })

        elif requesting_url == user_urls.home_page:
            # Only Featured Posts


            data = Post.objects.filter(creator = user, featured = True)
            serialized_data = PostSerializer(data = data,  many = True)
            serialized_data.is_valid()


            return Response({
               "posts": serialized_data.data,
               "individual_page": user_urls.individual_blog_post
            })

        elif requesting_url.split("?id=")[0] == user_urls.individual_blog_post:
            # The Id in the Post will be gotten and used here

            self.queryset = get_list_or_404(Post, custom_id = requesting_url.split("?id=")[1])

        elif requesting_url == user_urls.admin_page:
            self.queryset = Post.objects.filter(creator = user)
        return self.list(request, *args, **kwargs)

    def post(self, request:Request, api_key,*args, **kwargs):
        # self.serializer_class = PostSerializer
        # try:
        
        return self.create(request,api_key, *args, **kwargs)
        # except:
        #     return Response({
        #         "Error": "Couldn't update"
        #     }, status=400)

    def create(self, request,api_key, *args, **kwargs):
        # Define Fields
        token = get_object_or_404(Token, key = api_key)
        
        creator = token.user
        
        title = request.data["title"]
        image = request.data["image"]
        body = request.data["body"]
        publish = request.data["publish"]
        featured = request.data["featured"]

        if publish == "true":
            publish = True
        elif publish == "false":
            publish = False

        if featured == "true":
            featured = True
        elif featured == "false":
            featured = False


        print(publish, featured)

        Post.objects.create(
            creator = creator,
            title = title,
            image = image,
            body = body,
            publish = publish,
            featured = featured
        )

        return Response({
            
            "Success": "Created Successflly"
        }, status = 201)


class PostRetrieveUpdateDeleteView(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin):

    permission_classes = [IsAuthenticatedOrReadOnly, RestrictAccess]
    serializer_class = PostSerializer

    queryset = Post.objects.all()
    lookup_field= "custom_id"

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
   
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class TestToken(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    def get(self, request:Request, *args, **kwargs):

        return Response({})
