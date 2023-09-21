from django.shortcuts import render,redirect
from app.models import Appointment,User
import random
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def doctor_profile(request):
  
    try:
        doctor_data = User.object.filter(user_type = "doctor")
        context = {
            'doctor_data' :doctor_data
        }
    except:
        context = {
            'doctor_data' :"Data Not Found"
        }
    return render(request,'dasboard/user/doctor_profile.html',context)
