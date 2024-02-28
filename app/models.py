from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserSites(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_page = models.CharField(max_length = 10000,  blank=True, null=True)
    individual_blog_post = models.CharField(max_length = 10000,  blank=True, null=True)

    def __str__(self):
        return str(self.user)

def upload_script_path(instance, filename):
    # Define the upload path for js
    return f"js/{filename}"

def upload_css_path(instance, filename):
    # Define the upload path for css
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

def upload_user_script(instance, filename):

    return f"script/{filename}"
class UserConfig(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length = 100)
    preloader = models.CharField(max_length = 15)
    cont_rend = models.CharField(max_length = 15, blank = True, null = True)
    have_header = models.BooleanField(default = False)
    header_type = models.CharField(max_length = 15)
    header_links = models.JSONField()

    def  __str__(self):
        return self.brand_name

class UserScript(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    script = models.FileField(upload_to=upload_user_script)

    def __str__(self):
        return str(self.user)