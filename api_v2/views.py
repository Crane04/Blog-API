from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.models import Post
from api.serializers import PostSerializer
from django.views import View
from .JavaScript.header import header
from .JavaScript import preloader
from .JavaScript import convertdatetime, striptags
from .JavaScript.FetchData.fetchdata import fetch_data
from rest_framework import status
from app.models import UserConfig
# Create your views here.

def GetUserPosts_(request):

    category = request.GET.get("category")

    if category is not None:
        print(category)
        posts =Post.objects.filter(creator = request.user, categories = category)
    else:
        # If category is None, fetch all posts by the user
        posts = Post.objects.filter(creator = request.user)

    serializer = PostSerializer(posts, many=True)

    return Response({"posts":serializer.data, "type" : "all", "detail": "okay"}, status = status.HTTP_200_OK)

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
        current_url = "all posts"
        print(request.user)

        if current_url == "all posts":
            return GetUserPosts_(request)
        elif current_url == "one post":
            
            return GetPost_(request)
        else:
            return Response({"details":"error occured!"}, status = status.HTTP_400_BAD_REQUEST)



def generate_html(title, body_content, script):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{title}</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
        <!-- Add other head elements (meta tags, styles, scripts, etc.) here -->
    </head>
    <body>
        {body_content}

    <script>{script}</script>
    </body>
    </html>
    """
    return html_content

class TestHeader(View):
    def get(self, request):

        user_conf = header("Mayowa", [("Home", "/home" ), ("About", "/about")])
        html_content = generate_html("My Page", user_conf)
        return HttpResponse(html_content)

class TestPreloader(View):
    def get(self, request):
        get_preloader = preloader.loda()
        return HttpResponse(get_preloader)
    
class TestFetchData(View):
    def get(self, request):

        test_data = fetch_data()

        html_content = generate_html("MY Page", "Hey there", test_data)

        return HttpResponse(html_content)

class GenerateScript(View):
    
    def get(self, request):
        userconfig = get_object_or_404(UserConfig, user = request.user)
        token = get_object_or_404(Token, user = request.user).key
        brandname = userconfig.brand_name
        p_loader = userconfig.preloader
        cont_rend = userconfig.cont_rend
        have_header = userconfig.have_header
        header_type = userconfig.header_type
        header_links = userconfig.header_links

        result = "let bloggit_data = null"
        if have_header:
            result += """const bloggit_header = document.getElementById("bloggit-header")"""

        if p_loader:
            result += """const bloggit_preloader = document.getElementById("bloggit-preloader")"""
        
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
            print("ok")
            render_content = fetch_data(token, "no_render")

            result += render_content

        return HttpResponse(result, content_type="text/html")