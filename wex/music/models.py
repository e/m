from __future__ import unicode_literals

from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True, null=True)
    styles = models.CharField(max_length=255, blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    audio_file = models.FileField(upload_to='music', null=True, blank=True)
    video_file = models.FileField(upload_to='music', null=True, blank=True)
    order = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    template = models.CharField(max_length=255, blank=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    song = models.ForeignKey(Song)
