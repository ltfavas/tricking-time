from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CostumUser

admin.site.register(CostumUser, UserAdmin)
