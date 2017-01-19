from __future__ import unicode_literals

from django.db import models


class Meme(models.Model):
    title = models.CharField(max_length=255)
    template = models.CharField(max_length=255)
    order = models.IntegerField(blank=True, null=True)


class Paragraph(models.Model):
    text = models.TextField()
    meme = models.ForeignKey(Meme)
    style = models.CharField(max_length=255, blank=True, null=True)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
    meme = models.ForeignKey(Meme)
