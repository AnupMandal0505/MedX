from django.shortcuts import render,redirect
import random
from app.models import Patient,Appointment,Department
from django.contrib import messages


def home(request):
    
    return render(request,'home/index.html')
