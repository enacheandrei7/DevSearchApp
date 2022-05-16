from django.contrib import admin

# Register your models here.

from .models import Profile, Skill

# It shows up in the Admin pannel just after we register it here
admin.site.register(Profile)
admin.site.register(Skill)