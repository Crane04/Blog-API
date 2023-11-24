from django.db import models
from tinymce.models import HTMLField
from api.models import Post
from datetime import datetime

# Create your models here.

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(blank = True, null = True)
    comment = HTMLField()
    time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return str(self.post)