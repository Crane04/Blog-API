from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.validators import ValidationError
from rest_framework import serializers
class CommentSerializer(ModelSerializer):
    email = serializers.EmailField(write_only = True)
    class Meta:
        model = Comment
        fields = "__all__"
        extra_kwargs = {
            'email': {'write_only': True},
        }

    def validate_comment(self, value):
        if value.strip() == "":
            raise ValidationError("Comment can't be empty!")
        return value