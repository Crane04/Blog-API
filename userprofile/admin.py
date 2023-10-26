from django.contrib import admin
from .models import *
# Register your models here.

class TokenAdmin(admin.ModelAdmin):
    list_display = ["key", "user", "created"]
    # readonly_fields = ["key", "created"]

admin.site.register(Token, TokenAdmin)