from django.shortcuts import render,redirect
import random
from app.models import Patient,Appointment,Department
from django.contrib import messages

       


def some_disease(request):
   
    return render(request,'home/common_diseases.html')
