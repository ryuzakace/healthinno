from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})

class Sensor(models.Model):
    name = models.CharField(max_length=256, default = 'zero')
    patient = models.ForeignKey(Patient,related_name='sensors')

    def __str__(self):
        return self.patient.name +'-'+ self.name

class Data(models.Model):
    value = models.PositiveIntegerField()
    time = models.PositiveIntegerField()

    sensor = models.ForeignKey(Sensor,related_name='datas')

    def __str__(self):
        return self.sensor.patient.name+'-'+ self.sensor.name + '-'+ str(self.time)
