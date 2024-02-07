from django.db import models
from .patient import Patient
from .user import User


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    payment_ref = models.OneToOneField(Patient,on_delete=models.CASCADE) 
    order_id = models.CharField(max_length=50,blank=True,null=True,unique=True) 
    payment_id = models.CharField(max_length=50,blank=True,null=True,unique=True)
    payment_mode = models.CharField(max_length=50,blank=True,null=True)
    amount = models.IntegerField(blank=True,null=True)
    date = models.DateTimeField(blank=True,null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id