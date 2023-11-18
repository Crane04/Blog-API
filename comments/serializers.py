from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework.validators import ValidationError

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate_comment(self, value):
        if value.strip() == "":
            raise ValidationError("Comment can't be empty!")
        return value