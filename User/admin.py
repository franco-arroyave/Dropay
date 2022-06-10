from django.contrib import admin
from .models import User, Profile, TypeID

# Register your models here.

admin.site.register(Profile)
admin.site.register(TypeID)
