from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers

class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = "__all__"