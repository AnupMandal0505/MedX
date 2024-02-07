from django.shortcuts import render,redirect
import random
from app.models import Patient,Appointment,Department
from django.contrib import messages


def about_us(request):

    return render(request,'home/about_us.html')


 