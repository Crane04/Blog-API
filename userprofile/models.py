from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Token(models.Model):

    key = models.CharField(max_length=100, editable = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    created = models.DateTimeField(default = datetime.now(), editable=False)


    def save(self, *args, **kwargs):
        if not self.key:
            self.key = str(uuid.uuid4()).replace("-","")
        super().save(*args, **kwargs)


    def __str__(self):
        return self.key