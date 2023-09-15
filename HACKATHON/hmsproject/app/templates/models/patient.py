from django.db import models
from .appointment import Appointment

class Patient(models.Model):
    patient_ref = models.OneToOneField(Appointment, on_delete=models.CASCADE) 
    patient_id=models.CharField(max_length=25,unique=True)
    problem = models.CharField(max_length=255, blank=True)
    suggestion_test = models.CharField(max_length=255, blank=True)
    medicine = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.patient_id