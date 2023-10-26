from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User
class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ["title", "body", "image", "featured", "publish", "time", "custom_id"]

# class GetPostSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ["title", "body", "image", "time"]
    
class GetUser(ModelSerializer):
    class Meta:
        model = User

        fields = "__all__"