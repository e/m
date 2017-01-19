from django.contrib import admin

from .models import Meme, Paragraph, Image


class ParagraphInline(admin.StackedInline):
    model = Paragraph


class ImageInline(admin.StackedInline):
    model = Image


class MemeAdmin(admin.ModelAdmin):
    inlines = [ParagraphInline, ImageInline]
admin.site.register(Meme, MemeAdmin)
