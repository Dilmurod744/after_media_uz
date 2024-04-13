from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.models import User, Video, Photo


# Register your models here.
@admin.register(User)
class UserAdmin(ModelAdmin):
    pass


@admin.register(Video)
class VideoAdmin(ModelAdmin):
    pass


@admin.register(Photo)
class PhotoAdmin(ModelAdmin):
    pass
