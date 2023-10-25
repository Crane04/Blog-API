from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
from django_quill.fields import QuillField
from tinymce.models import HTMLField
# Create your models here.

def upload_image_path(instance, filename):
    # Define the upload path for images
    return f"descriptions/{filename}"

class Post(models.Model):
    custom_id = models.CharField(primary_key = True, max_length=100, unique=True, editable=False)
    creator = models.ForeignKey(User, on_delete = models.Case)
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to = upload_image_path, blank = True, null = True)
    body = HTMLField(
        
    )
    time = models.DateTimeField(default = datetime.now())
    featured = models.BooleanField(default=False)
    publish = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.custom_id:
            self.custom_id = self.title + str(uuid.uuid4()).replace("-","")[:10]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

        




