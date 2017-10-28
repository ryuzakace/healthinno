from django.contrib import admin
from health.models import Patient, Sensor, Data
# Register your models here.
admin.site.register(Patient)
admin.site.register(Sensor)
admin.site.register(Data)
