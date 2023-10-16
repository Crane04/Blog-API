from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserSites(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sites = models.JSONField()

    def __str__(self):
        return str(self.user)