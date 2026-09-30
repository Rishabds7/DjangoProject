from django.contrib import admin
from . import models

# Register your models here.

class LoginSystemAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')

admin.site.register(models.UserDetails, LoginSystemAdmin)