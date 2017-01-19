from __future__ import unicode_literals

from django.db import models


class CV(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)


class Experience(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    company = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True, upload_to='images')
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    style = models.CharField(max_length=255, null=True, blank=True)
    cv = models.ForeignKey(CV, related_name='experiences')
    sector = models.TextField(blank=True, null=True)


class Paragraph(models.Model):
    text = models.TextField()
    experience = models.ForeignKey(Experience, related_name='paragraphs')
    order = models.IntegerField()


class PersonalData(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address_1 = models.CharField(max_length=255, blank=True, null=True)
    address_2 = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    county = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    cv = models.OneToOneField(CV, related_name='personal_data')
    objective = models.TextField(null=True, blank=True)


class Skill(models.Model):
    name = models.CharField(max_length=255)
    person = models.ForeignKey(CV, related_name='skills')


class Technology(models.Model):
    name = models.CharField(max_length=255)
    experience = models.ForeignKey(CV, related_name='technologies')


class Education(models.Model):
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255, blank=True, null=True)
    person = models.ForeignKey(PersonalData, related_name='degrees')
