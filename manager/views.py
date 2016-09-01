from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Field, Speciality

class IndexView(generic.ListView):
	template_name = 'manager/index.html'
	context_object_name = 'fields'
	
	def get_queryset(self):
		return Field.objects.all()

class FieldView(generic.DetailView):
	model = Field
	template_name = 'manager/field.html'

class SpecialityView(generic.DetailView):
	model = Speciality
	template_name = 'manager/speciality.html'

