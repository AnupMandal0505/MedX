from django.db import models
from .appointment import Appointment
from autoslug import AutoSlugField

class Patient(models.Model):
    patient_ref = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    patient_id=models.CharField(max_length=25,primary_key=True,null=False)
    symptoms = models.TextField(default="NULL")
    suggestion_test = models.TextField(default="NULL")
    advice = models.TextField(default="NULL")
    rx = models.TextField(default="NULL")
    # patient_id_slug=AutoSlugField(populate_from='patient_id',unique=True,null=True)
    def __str__(self):
        if self.patient_id is not None:
            return str(self.patient_id)
        else:
            return "N/A"