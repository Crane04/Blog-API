from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from .serializers import *
from .models import *


# Create your views here.
class CommentView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [AllowAny]