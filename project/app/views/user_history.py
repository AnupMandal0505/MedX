from django.shortcuts import render,redirect
from app.models import Appointment,Payment,User
import random

from django.contrib.auth.decorators import login_required



@login_required(login_url='signin')
def appointment_history(request):
    user_id = request.user
    user_history = Appointment.objects.filter(appointment_ref = user_id)
    context = {
        'user_history' :user_history
    }
    return render(request,'dasboard/user/appointment_history.html',context)


@login_required(login_url='signin')
def payment_history(request):
    user_id = request.user
    
    user_history = Payment.objects.filter(user = user_id)
    context = {
        'user_history' :user_history
    }
    return render(request,'dasboard/user/payment_history.html',context)


@login_required(login_url='signin')
def user_data(request):
    user_data = User.object.all()
    context = {
        'user_data' :user_data
    }
    return render(request,'dasboard/technician/user_data.html',context)

