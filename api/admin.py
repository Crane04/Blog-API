from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("custom_id", "title","time", "creator")

admin.site.register(Post, PostAdmin)