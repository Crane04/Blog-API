from rest_framework.serializers import ModelSerializer
from .models import Post
from rest_framework import serializers
from django.contrib.auth.models import User
class PostSerializer(ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ["title", "body", "image", "publish", "time", "custom_id", "categories", 'comment_count']

    def get_comment_count(self, obj):
        return obj.post.count()
    
class GetUser(ModelSerializer):
    class Meta:
        model = User

        fields = "__all__"