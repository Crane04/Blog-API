from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *
from userprofile.models import Token
from api.models import *

# Create your views here.
class CommentView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]

    def get(self, request, api_key, id, *args, **kwargs):
        token = get_object_or_404(Token, key = api_key)


        user = get_object_or_404(User, username = token.user)

        post = Post.objects.get(custom_id = id)

        comments = Comment.objects.filter(post = post.pk)[::-1]

        serializer = self.serializer_class(comments, many = True)

        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, api_key, id, *args, **kwargs):
        # Get user Token
        token = get_object_or_404(Token, key = api_key)

        # Get user associated with the token
        user = get_object_or_404(User, username = token.user)

        post = Post.objects.get(custom_id = id)

        # Get all comments for this user
        comments = Comment.objects.filter(post = post.pk)
        request.data["post"] = post.pk


        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)