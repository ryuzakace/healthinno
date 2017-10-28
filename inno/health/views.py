from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from django.views.generic import (View,TemplateView,
                                ListView,DetailView,
                                CreateView,DeleteView,
                                UpdateView)

# Create your views here.
from . import models
class basicView(TemplateView):

    template_name = 'index.html'

    def get(self, request):
        return HttpResponse("CLLL")

class PatientListView(ListView):
    # If you don't pass in this attribute,
    # Django will auto create a context name
    # for you with object_list!
    # Default would be 'school_list'

    # Example of making your own:
    # context_object_name = 'schools'
    model = models.Patient

class SensorListView(ListView):
    model = models.Sensor

class PatientDetailView(DetailView):
    context_object_name = 'patient_details'
    model = models.Patient
    template_name = 'health/patient_detail.html'

class SensorDetailView(DetailView):
    context_object_name = 'sensor_details'
    model = models.Sensor
    template_name = 'health/sensor_detail.html'

"""class PatientCreateView(CreateView):
    fields = ("name","age","location")
    model = models.Patient

class SensorCreateView(CreateView):
    fields = ("name","patient")
    model = models.Sensor"""
