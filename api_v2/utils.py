
from app.models import UserConfig, UserSites, UserScript
from django.shortcuts import get_object_or_404
from api.models import Post
from api.serializers import PostSerializer
from comments.models import Comment
from comments.serializers import CommentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .JavaScript.header import header
from .JavaScript import preloader
from .JavaScript import convertdatetime, striptags
from .JavaScript.FetchData.fetchdata import fetch_data
from django.core.files.base import ContentFile

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
    comments = Comment.objects.filter(post = post.pk)

    comments_serializer = CommentSerializer(comments, many = True)
    post.views += 1
    post.save()
    
    return Response({"post":serializer.data, "comments": comments_serializer.data, "type" : "one", "detail": "okay"}, status = status.HTTP_200_OK)


def generate_script(request):
    userconfig = get_object_or_404(UserConfig, user = request.user)
    user_script, created = UserScript.objects.get_or_create(user=request.user)
    token = get_object_or_404(Token, user = request.user).key
    brandname = userconfig.brand_name
    p_loader = userconfig.preloader
    cont_rend = userconfig.cont_rend
    have_header = userconfig.have_header
    header_links = userconfig.header_links

    print("on it")

    result = """let bloggit_data = null \n
    const current_url = window.location.href \n
    const url_parameters = window.location.search; \n
    const post_id = new URLSearchParams(url_parameters).get("id");\n
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
    elif cont_rend == None or cont_rend.strip() == "":
        render_content = fetch_data(token, "no_render")

        result += render_content

    user_script.script.save(f'/{token}.js', ContentFile(result), save=True)
    return request.user
