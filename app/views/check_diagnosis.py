from django.shortcuts import render,redirect
from app.models import Appointment
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def check_diagnosis(request):
        
        return render(request,'dasboard/user/check_diagnosis.html')
