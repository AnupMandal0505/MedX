from django.shortcuts import render,redirect
from app.models import Appointment,User
import random

from django.contrib.auth.decorators import login_required

def appointment_unique_number(name):
    name=name
    while(True):  
        uq=random.randint(1000,9999)
        uq=name+str(uq)
        try:
            n=Appointment.objects.get(appointment_id=uq)
        except:
            return uq

@login_required(login_url='signin')
def appointment(request):
    if request.method == 'POST':
        date=request.POST['date']
        time=request.POST['time']
        doctor=request.POST['doctor']
        region=request.POST['region']
        ran = random.randint(999,9999)
        appointment_ref=request.user
        appointment_id=appointment_unique_number("appoint")
        df=Appointment.objects.create(appointment_ref=appointment_ref,appointment_id=appointment_id,date=date,slot_time=time,region=region,doctor=doctor)        
        df.save()
        return redirect('dasboard')
    try:
        doctor_data = User.object.filter(user_type = "doctor")
        context = {
            'doctor_data' :doctor_data
        }
    except:
        context = {
            'doctor_data' :"Data Not Found"
        }
    return render(request,'dasboard/user/appointment.html',context)
