from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin

# Register your models here.

admin.site.site_header = "E-Commerce"
admin.site.site_title = "E-Commerce"


admin.site.register(CustomUser, UserAdmin)
