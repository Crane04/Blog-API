from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = ["title", "body", "image", "featured", "publish", "time", "custom_id"]

# class GetPostSerializer(ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ["title", "body", "image", "time"]
    