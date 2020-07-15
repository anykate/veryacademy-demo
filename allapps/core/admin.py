from django.contrib import admin
from .models import Language, Framework


# Register your models here.
@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
