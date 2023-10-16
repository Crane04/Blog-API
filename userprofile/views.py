from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import *
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your views here.

class LoginView(APIView):
    
    serializer = UserSerializer
    def post(self, request:Request, *args, **kwargs):

        user = get_object_or_404(User, username = request.data["username"])
        if not user.check_password(request.data["password"]):
            return Response({
                "detail": "Not found."
            }, status = status.HTTP_400_BAD_REQUEST)
        token, created = Token.objects.get_or_create(user = user)

        return Response({
            "token": token.key,
            "user": self.serializer(user).data
        }, status = status.HTTP_201_CREATED)


class signup(APIView):

    serializer_class = UserSerializer

    def get(self, request:Request, *args, **kwargs):
        return Response({})
    def post(self, request:Request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()

            user = get_object_or_404(User, username = request.data["username"])
            user.set_password(request.data["password"])
            user.save()

            token = Token.objects.create(user = user)

            return Response({
                "token": token.key,
                "user": self.serializer_class(user).data
            }, status = status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status = status.HTTP_400_BAD_REQUEST
            )

class test_token(APIView):

    def get(self, request:Request, *args, **kwargs):
        return Response({
            
        })