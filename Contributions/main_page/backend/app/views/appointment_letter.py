from django.shortcuts import render
from app.models import Appointment
import random

from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def user_appointment_letter(request,slug):
    data = Appointment.objects.get(appointment_id=slug)
    context = {
        'data':data,
    }
    return render(request,'dasboard/user/appointment_letter.html',context)
