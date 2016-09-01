from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
class Field(models.Model):
    class Meta:
        ordering = ['name']

    field_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Speciality(models.Model):
    class Meta:
        ordering = ['field', 'name']
        verbose_name_plural = "Specialities"

    speciality_id = models.AutoField(primary_key=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"

    country_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=100)
    is_iaeste_member = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    @property
    def is_member(self):
        return(bool.is_iaeste_member)

class Province(models.Model):
    class Meta:
        ordering = ['name']

    province_code = models.CharField(max_length=2, default='0')
    name = models.CharField(max_length=50, default='')

    def __unicode__(self):
        return self.name

class City(models.Model):
    class Meta:
        ordering = ['postal_code', 'name']
        verbose_name_plural = "Cities"

    postal_code = models.CharField(max_length=5, default='0')
    name = models.CharField(max_length=100, default='')
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.name

class University(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Universities"

    university_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='')
    university_code = models.CharField(max_length=10, default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, default=1)
    postal_code = models.CharField(max_length=5)
    address = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=100, default='')

    def __unicode__(self):
        return self.name

class Faculty(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Faculties"

    faculty_id = models.AutoField(primary_key=True)
    university = models.ForeignKey(University, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Member(models.Model):
    class Meta:
        ordering = ['last_name', 'name']

    member_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=5)
    mobile_phone = models.CharField(max_length=20, default='')
    has_whatsapp = models.BooleanField(default=False)
    home_phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, default='')
    birthday = models.DateField(default=date.today)
    nationality = models.ForeignKey(Country, on_delete=models.CASCADE)
    passport = models.CharField(max_length=50, default='')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    joined = models.DateField(default=date.today)

    def __unicode__(self):
        return self.last_name + ', ' + self.name
