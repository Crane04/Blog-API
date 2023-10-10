from rest_framework.serializers import ModelSerializer
from .models import Post as Blog

class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields  = "__all__"