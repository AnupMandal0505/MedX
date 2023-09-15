from django.shortcuts import render
from app.models import Appointment
from datetime import datetime

from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def appointment(request,template_name):
    template_name=template_name
    user=request.user
    doctor=user.name
    today_date=datetime.now().date()
    today_appointment=Appointment.objects.filter(doctor=doctor,date=today_date,status=False)
    all_appointment=Appointment.objects.filter(doctor=doctor)
    context = {
        'today_appointment':today_appointment,
        'all_appointment':all_appointment,
    }
    return render(request,template_name,context)


def show_appointment(request,slug):
    user=request.user
    doctor=user.name
    data=Appointment.objects.get(appointment_id=slug,doctor=doctor)
    context = {
        'data':data
    }
    return render(request,"dasboard/doctor/show_appointment_letter.html",context)