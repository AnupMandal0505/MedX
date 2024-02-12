from django.shortcuts import render,redirect
import random
from app.models import Patient,Appointment,Department
from django.contrib import messages

       


def site_maintenance(request):
   
    return render(request,'Site_Maintenance.html')
