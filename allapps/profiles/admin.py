from django.contrib import admin
from .models import UserProfile


# Register your models here.
class InlineUserProfile(admin.StackedInline):
    model = UserProfile
    extra = 0


# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#     pass
