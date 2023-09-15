from django.db import models
from .user import User

class Appointment(models.Model):
    appointment_ref = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_id=models.CharField(max_length=25,unique=True)
    date = models.DateField()
    slot_time = models.TimeField()
    region = models.CharField(max_length=255, blank=True)
    doctor = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.appointment_id