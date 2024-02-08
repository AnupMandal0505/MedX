from django.shortcuts import render,redirect
from app.models import Appointment
import random

from django.contrib.auth.decorators import login_required



@login_required(login_url='signin')
def history(request):
    user_id = request.user
    print(user_id)
    user_appointment_history = Appointment.objects.filter(appointment_ref = user_id)
    context = {
        'user_appointment_history' :user_appointment_history
    }
    return render(request,'dasboard/user/history.html',context)
