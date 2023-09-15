from django.db import models
from .user import User


RELATION_CHOICES = (
    ("1", "Self"),
    ("2", "Father"),
    ("3", "Mother"),
    ("4", "Wife"),
    ("5", "Husband"),
    ("6", "Son"),
    ("7", "Daughter"),
    ("8", "Brother"),
)


class Appointment(models.Model):
    appointment_ref = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_id=models.CharField(max_length=25,unique=True)
    date = models.DateField()
    slot_time = models.TimeField()
    relation = models.CharField(max_length = 20,choices = RELATION_CHOICES,default = '1')
    region = models.CharField(max_length=255, blank=True)
    doctor = models.CharField(max_length=255, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.appointment_id