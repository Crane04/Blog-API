from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserSites(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    home_page = models.CharField(max_length = 100,  blank=True, null=True)
    blog_page = models.CharField(max_length = 100,  blank=True, null=True)
    individual_blog_post = models.CharField(max_length = 100,  blank=True, null=True)
    admin_page = models.CharField(max_length = 100,  blank=True, null=True) #Posts, delete and edit can be made from admin Page

    def __str__(self):
        return str(self.user)