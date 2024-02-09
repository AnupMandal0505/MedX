from django.db import models
from .user import User

class Department(models.Model):
    dept_ref = models.OneToOneField(User, on_delete=models.CASCADE) 
    dept_id = models.CharField(max_length=50,primary_key=True,null=False)
    position = models.CharField(max_length=50,blank=True)
    qualification = models.CharField(max_length=50,blank=True)
    pan = models.CharField(max_length=50,blank=True)
    salary = models.IntegerField()
    signature = models.URLField(blank=True)
    def __str__(self):
        return self.dept_id