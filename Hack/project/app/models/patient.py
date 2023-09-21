from django.db import models
from .appointment import Appointment
from autoslug import AutoSlugField

class Patient(models.Model):
    patient_ref = models.OneToOneField(Appointment, on_delete=models.CASCADE) 
    patient_id=models.CharField(max_length=25,unique=True)
    symptoms = models.TextField(default="NULL")
    suggestion_test = models.TextField(default="NULL")
    advice = models.TextField(default="NULL")
    rx = models.TextField(default="NULL")
    patient_id_slug=AutoSlugField(populate_from='patient_id',
                         unique=True,null=True,default=None)
    def __str__(self):
        return self.patient_id
    