from django.contrib import admin

from .models import Song, Image


class ImageInline(admin.StackedInline):
    model = Image


class SongAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
admin.site.register(Song, SongAdmin)
