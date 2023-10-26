# Import Dependencies

from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponse
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
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, SAFE_METHODS, IsAuthenticated
from app.models import *
from userprofile.models import Token


class RestrictAccess(BasePermission):
    
    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
    
        return obj.creator == request.user

class PostListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):


    # permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    

    def get(self, request:Request, api_key, *args, **kwargs):
        # Get user Token
        token = get_object_or_404(Token, key = api_key)

        # Get user associated with the token
        user = get_object_or_404(User, username = token.user)
        # user_ = 
        print(self.request.user)

        requesting_url = request.GET.get("url")
        user_urls = get_object_or_404(UserSites, user = token.user)

        # Remove queries from requesting_url in home or blog page

        if "?" in requesting_url:
            requesting_url_homeblog = requesting_url.split("?")[0]

        # Filter Posts
        if requesting_url_homeblog == user_urls.blog_page:
            # All Posts

            data = Post.objects.filter(creator = user)
            
            serialized_data = PostSerializer(data = data,  many = True)
            serialized_data.is_valid()


            return Response({
               "posts": serialized_data.data,
               "individual_page": user_urls.individual_blog_post
            })

        elif requesting_url_homeblog == user_urls.home_page:
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

            print(self.request.user, token.user, token.key)
            self.queryset = Post.objects.filter(creator = user)

        return self.list(request, *args, **kwargs)

    def post(self, request:Request, api_key,*args, **kwargs):

        # try:
        
        return self.create(request,api_key, *args, **kwargs)
        # except:
        #     return Response({
        #         "Error": "Couldn't update"
        #     }, status=400)

    def create(self, request,api_key, *args, **kwargs):
        # Define Fields
        token = get_object_or_404(Token, key = api_key)
       
        user_ = get_object_or_404(User, username = self.request.user_)
        creator = token.user
        print(user_, creator, self.request.user.is_authenticated)
        if user_ == creator:
        
            title = request.data["title"]
            image = request.data["image"]
            body = request.data["body"]
            publish = request.data["publish"]
            featured = request.data["featured"]

            # Convert js bool
            if publish == "true":
                publish = True
            elif publish == "false":
                publish = False

            if featured == "true":
                featured = True
            elif featured == "false":
                featured = False


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
        else:
            print("Error")


class PostRetrieveUpdateDeleteView(GenericAPIView, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin, RestrictAccess):


    serializer_class = PostSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, RestrictAccess]
    queryset = Post.objects.all()
    lookup_field= "custom_id"

    def get(self, request:Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
   
    def put(self, request:Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request:Request, *args, **kwargs):

        return self.destroy(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        pass


class TestToken(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request:Request, *args, **kwargs):

        return Response({})

from .serializers import GetUser
class NopeView(APIView):
    def get(self, request):
        try:
            # Your code to retrieve user data
            user_data = {"user": request.user.username}
            return Response(user_data)
        except Exception as e:
            # Handle exceptions and return a JSON error response
            return Response({"error": str(e)}, status=500)