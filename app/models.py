from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserSites(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # home_page = models.CharField(max_length = 100,  blank=True, null=True)
    blog_page = models.CharField(max_length = 100,  blank=True, null=True)
    individual_blog_post = models.CharField(max_length = 100,  blank=True, null=True)

    def __str__(self):
        return str(self.user)

def upload_script_path(instance, filename):
    # Define the upload path for images
    return f"js/{filename}"

def upload_css_path(instance, filename):
    # Define the upload path for images
    return f"css/{filename}"

class Scripts(models.Model):
    name = models.CharField(max_length=100)
    script = models.FileField(upload_to = upload_script_path)
    def __str__(self):
        return self.name

class CSS(models.Model):
    name = models.CharField(max_length=100)
    css_file = models.FileField(upload_to = upload_css_path)

    def __str__(self):
        return self.name