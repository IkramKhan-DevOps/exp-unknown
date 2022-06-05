from django.contrib import admin

# Register your models here.
from src.accounts.models import User, Profile

admin.site.register(User)
admin.site.register(Profile)