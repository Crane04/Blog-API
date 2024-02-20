from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.models import Post
from api.serializers import PostSerializer
from django.views import View
from .JavaScript.header import header
from .JavaScript import preloader
from .JavaScript import convertdatetime, striptags
from .JavaScript.FetchData.fetchdata import fetch_data
from rest_framework import status
from app.models import UserConfig, UserSites, UserScript
from django.core.files.base import ContentFile
# Create your views here.

def GetUserPosts_(request):

    category = request.GET.get("category")
    user_sites = get_object_or_404(UserSites, user = request.user)
    ind = user_sites.individual_blog_post

    if category is not None:
        posts =Post.objects.filter(creator = request.user, categories = category)
    else:
        # If category is None, fetch all posts by the user
        posts = Post.objects.filter(creator = request.user)

    serializer = PostSerializer(posts, many=True)

    return Response({"posts":serializer.data,
                     "ind": ind,
                     "type" : "all",
                     "detail": "okay"}, status = status.HTTP_200_OK)

def GetPost_(request):
    custom_id = request.GET.get("id")

    if custom_id is None:
        return Response({"detail":"No id was provided"}, status= status.HTTP_404_NOT_FOUND)

    post = get_object_or_404(Post, custom_id = custom_id)

    serializer = PostSerializer(post)
    post.views += 1
    post.save()
    
    return Response({"post":serializer.data, "type" : "one", "detail": "okay"}, status = status.HTTP_200_OK)

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


class GenerateScript(View):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    def get(self, request):
        userconfig = get_object_or_404(UserConfig, user = request.user)
        user_script, created = UserScript.objects.get_or_create(user=request.user)
        token = get_object_or_404(Token, user = request.user).key
        brandname = userconfig.brand_name
        p_loader = userconfig.preloader
        cont_rend = userconfig.cont_rend
        have_header = userconfig.have_header
        header_links = userconfig.header_links

        result = """let bloggit_data = null \n
        const current_url = window.location.href
        const url_parameters = window.location.search;
        const post_id = new URLSearchParams(url_parameters).get("id");
        """
        if have_header:
            result += """const bloggit_header = document.getElementById("bloggit-header") \n"""

        if p_loader:
            result += """const bloggit_preloader = document.getElementById("bloggit-preloader") \n"""
        
        if cont_rend:
            result += """const bloggit = document.getElementById("bloggit-container")"""

        if have_header:
            header_text = header(brandname, header_links)

            result += header_text

        if p_loader:
            preloader_text = preloader.pre_loader(p_loader)

            result += preloader_text
        
        if cont_rend:
            conv_dt = convertdatetime.convert_datetime()
            strip_tgs = striptags.strip_tags()
            render_content = conv_dt + strip_tgs + fetch_data(token, cont_rend)

            result += render_content
        elif cont_rend == None:
            render_content = fetch_data(token, "no_render")

            result += render_content

        user_script.script.save(f'/{token}.js', ContentFile(result), save=True)
        return HttpResponse(result, content_type = "")