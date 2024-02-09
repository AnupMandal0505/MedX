from django.shortcuts import render,redirect
import random
from app.models import Patient,Appointment,Department
from django.contrib import messages


def contact_us(request):

    return render(request,'home/contact_us.html')


 