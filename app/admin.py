from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(UserSites)
admin.site.register(Scripts)
admin.site.register(CSS)

class UserConfigAdmin(admin.ModelAdmin):
    list_display = ["user", "brand_name", "preloader", "cont_rend"]

admin.site.register(UserScript)
admin.site.register(UserConfig, UserConfigAdmin)