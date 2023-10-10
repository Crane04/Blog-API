from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Post as Blog
from .serializers import BlogSerializer

@api_view(['GET'])
def index(request):

    return Response({
        "success": "Created Successfully",
        "a": "g"
    })

@api_view(["GET"])
def get_posts(request):

    blog = Blog.objects.all()
    blog_serializer = BlogSerializer(blog, many = True)
    return Response(
        blog_serializer.data
    )

@api_view(['GET', 'POST'])
def create_post(request):

    data = request.data

    serializer = BlogSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": "Your Post has successfully been created"
        }, status=201)

    else:
        return Response({
            serializer.errors
        }, status = 400)

@api_view(["DELETE"])
def delete_post(request):

    id = request.data.get("id")

    try:
        blog = Blog.objects.get(id = id)
        blog.delete()

        return Response({
            "Success": f"This Blog with id {id} has been deleted"
        })

    except Blog.DoesNotExist:
        return Response({
            "Error": f"The Blog with id {id} wasn't found."
        }, status=404)

@api_view(["GET"])
def get_one_post(request, pk):

    # id = request.data.get("id")
    id = pk
    try:
        blog = Blog.objects.get(id = id)
        serializer = BlogSerializer(blog)

        return Response(serializer.data, status = 201)

    except Blog.DoesNotExist:

        return Response({
            "Error": "This Blog doesn't exist"
        }, status=404)

@api_view(["PUT"])
def update_post(request):

    id = request.data.get("id")
    title = request.data.get("title")
    body = request.data.get("body")

    try:
        blog = Blog.objects.get(id = id)

        blog.title, blog.body = title, body
        blog.save()

        return Response({
            "Success":f"Your Post with id {id} has been successfully updated."
        }, status=201)

    except Blog.DoesNotExist:

        return Response({
            "status": f"Sorry, the post with id {id} doesn't exist"
        }, status=201)