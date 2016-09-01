from django.contrib import admin

# Register your models here.
from .models import Field, Speciality, Country, Province, City, University, Faculty, Member

admin.site.register(Field)
admin.site.register(Speciality)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(University)
admin.site.register(Faculty)
admin.site.register(Member)