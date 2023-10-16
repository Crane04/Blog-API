from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
# Create your models here.

def upload_image_path(instance, filename):
    # Define the upload path for images
    return f"descriptions/{filename}"

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete = models.Case)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = upload_image_path, blank = True, null = True)
    body = models.TextField()
    time = models.DateTimeField(default = datetime.now())

    custom_id = models.CharField(primary_key = True, max_length=100, unique=True, editable=False)

    def save(self, *args, **kwargs):
        # Generate a custom ID based on title and a portion of UUID
        self.custom_id = self.title + str(uuid.uuid4()).replace("-", "")[8:]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




