from django.conf.urls import url
from . import views

app_name = 'manager'
urlpatterns = [
	# /manager/
    url(r'^$', views.IndexView.as_view(), name="index"),
    # /manager/field/1/
    url(r'^field/(?P<pk>[0-9]+)/$', views.FieldView.as_view(), name="field"),
    # /manager/field/1/specialities/
    url(r'^speciality/(?P<pk>[0-9]+)/$', views.SpecialityView.as_view(), name="speciality")
]
