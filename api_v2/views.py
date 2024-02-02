from django.shortcuts import render, get_list_or_404, get_object_or_404, HttpResponse
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from api.models import Post
from api.serializers import PostSerializer
from django.views import View
from .JavaScript.header import header
# Create your views here.



class GetUserPosts(GenericAPIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, *args, **kwargs):
        category = request.GET.get("category")

        if category is not None:
            posts =Post.objects.filter(creator = request.user, categories = category)
        else:
            # If category is None, fetch all posts by the user
            posts = Post.objects.filter(creator = request.user)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

class GetPost(GenericAPIView):
    authentication_classes = [TokenAuthentication]

    def get(self, request, id, *args, **kwargs):
        post = get_object_or_404(Post, custom_id = id)

        serializer = PostSerializer(post)
        post.views += 1
        post.save()
        
        return Response(serializer.data)

def generate_html(title, body_content):
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
    </body>
    </html>
    """
    return html_content

class TestHeader(View):
    def get(self, request):

        user_conf = header("Mayowa", [("Home", "/home" ), ("About", "/about")])
        html_content = generate_html("My Page", user_conf)
        return HttpResponse(html_content)
