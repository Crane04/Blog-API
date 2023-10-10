from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    unique_id = models.CharField(primary_key = True, editable=True, max_length = 100)
    creator = models.ForeignKey(User, on_delete = models.Case)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = "descriptions/")
    body = models.TextField()
    time = models.DateTimeField(default = datetime.now())


    def __str__(self):
        return self.title