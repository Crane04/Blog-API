# Import Dependencies

from django.shortcuts import render, get_object_or_404, get_list_or_404, HttpResponse
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer#, GetPostSerializer
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, BasePermission, SAFE_METHODS, IsAuthenticated
from userprofile.models import Token
from app.models import Scripts, CSS, UserSites
from comments.models import Comment
from comments.serializers import CommentSerializer


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

        requesting_url = request.GET.get("url")
        cont_rend = request.GET.get("cont_rend")
        header_type = request.GET.get("header_type")


        try:
            script = get_object_or_404(Scripts, name = cont_rend)
            if CSS.objects.filter(name = cont_rend).exists():
                css_render = CSS.objects.get(name = cont_rend)
        except:pass

        try:
            header_type = get_object_or_404(Scripts, name = header_type)
            if CSS.objects.filter(name = header_type).exists():
                css_header = CSS.objects.get(name = header_type)
            else:
                css_header = "undefined"
        except: header_type = "undefined"

        user_urls = get_object_or_404(UserSites, user = token.user)

        # Remove queries from requesting_url in home or blog page

        requesting_url_homeblog = requesting_url.split("?")[0]


        # Filter Posts
        if  user_urls.blog_page.replace("%20", " ") in requesting_url_homeblog.replace("\\", "/"):
            # All Posts
            category = request.GET.get("category")

            if category != "null":

                data = Post.objects.filter(creator = user, publish = True, categories = category).order_by("-time")
                if data.exists():
                    data = data
                else:
                    data = Post.objects.filter(creator = user, publish = True).order_by("-time")
            elif category == "null":
                data = Post.objects.filter(creator = user, publish = True).order_by("-time")

            serialized_data = PostSerializer(data = data,  many = True)
            serialized_data.is_valid()

            response_data = {
                "posts": serialized_data.data,
                "individual_page": user_urls.individual_blog_post,
                "home_page": user_urls.blog_page
            }
            try:
                response_data["script"] = script.script
            except: pass

            try:
                response_data["css_render"] = css_render.css_file
            except: pass

            try:
                response_data["header_type"] = header_type.script
            except: pass

            try:
                response_data["css_header"] = css_header.css_file
            except: pass

            return Response(
                response_data, status = status.HTTP_200_OK
            )


        elif user_urls.individual_blog_post.replace("%20", " ") in requesting_url.split("?id=")[0].replace("\\", "/"):
            # The Id in the Post will be gotten and used here

            try:
                data = get_list_or_404(Post, custom_id = requesting_url.split("?id=")[1])

                post = Post.objects.get(custom_id = requesting_url.split("?id=")[1])

                comments = Comment.objects.filter(post = post.pk)

                comments_serailizer = CommentSerializer(data = comments, many = True)


                serialized_data = PostSerializer(data = data, many = True)
                serialized_data.is_valid()

                try:
                    post.views = post.views + 1
                    post.save()
                except: pass
                
                comments_serailizer.is_valid()

                response_data = {
                    "post": serialized_data.data,
                    "home_page": user_urls.blog_page
                }
                if cont_rend:
                    response_data["script"] = Scripts.objects.get(name = "cappuccino").script

                if header_type != "undefined":
                    response_data["header_type"] = header_type.script
                elif header_type == "undefined":
                    pass
                

                comment_data = request.GET.get("comment")

                if comment_data:
                    comment_rf = request.GET.get("comment_rf")
                    comment_rc = request.GET.get("comment_rc")
                    response_data["comments"] = comments_serailizer.data
                    response_data["sendcomment"] = Scripts.objects.get(name = "send comment").script

                    if comment_rc.lower() == "true":
                        response_data["comment_rc"] = Scripts.objects.get(name = "render comments").script

                    if comment_rf.lower()== 'true':
                        response_data['comment_rf'] = Scripts.objects.get(name = "render form").script

                return Response(
                    response_data, status = status.HTTP_200_OK
                )


            except:
                data = None
                response_data = {
                    "not_found_details": "Not Found",
                }
                try:
                    response_data["header_type"] = header_type.script
                except: pass

                try:
                    response_data["css_header"] = css_header.css_file
                except: pass

                return Response(response_data, status = status.HTTP_404_NOT_FOUND)

        else:
            response_data = {
                "unregistered_site_url": "Not Found",
                "home_page": user_urls.blog_page
            }
            return Response(response_data, status = status.HTTP_401_UNAUTHORIZED)

        return self.list(request, *args, **kwargs)


class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, RestrictAccess]
    queryset = Post.objects.all()
    lookup_field = "custom_id"
