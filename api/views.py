from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework.request import Request

@api_view(['GET'])
def index(request):

    return Response({
        "success": "Created Successfully",
        "a": "g"
    })

@api_view(["GET"])
def get_posts(request):

    post = Post.objects.all()
    post_serializer = PostSerializer(post, many = True)
    return Response(
        post_serializer.data, status = 200
    )

class PostListCreateView(APIView):

    serializer_class = PostSerializer

    def get(self, request:Request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = self.serializer_class(posts, many = True)

        return Response(
            serializer.data, status = 200
        )

    def post(self, request:Request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data = data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "Success": "Your Post has been uploaded",
                "data": serializer.data
            }, status = 201)

        else:
            return Response({
                "Error": "Couldn't save your Post"
            }, status = 400)

class PostRetrieveUpdateDeleteView(APIView):

    serializer_class = PostSerializer

    def get(self, request:Request, unique_id:str):

        post = get_object_or_404(Post, pk = unique_id)
        serializer = self.serializer_class(post)

        return Response(
            serializer.data, status = 200
        )

    def put(self, request:Request, unique_id:str):
        post = get_object_or_404(Post, pk = unique_id)

        data = request.data
        
        serializer = self.serializer_class(post, data = data)


        if serializer.is_valid():
            serializer.save()

            return Response({
                "Success": "Updated",
                "data":serializer.data
            })
        else:
            return Response(
                serializer.errors, status=400
            )
    def delete(self, reqest:Request, unique_id:str):

        post = get_object_or_404(Post, pk = unique_id)

        post.delete()

        return Response({
            "Success": "Post has been deleted"
        }, status = 400)
        