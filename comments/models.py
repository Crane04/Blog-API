from django.db import models
from tinymce.models import HTMLField
from api.models import Post

# Create your models here.

class Comment(models.Model):
    post = models.OneToOneField(Post, related_name='post', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = HTMLField()

    def __str__(self):
        return str(self.post)