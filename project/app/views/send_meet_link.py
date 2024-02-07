from django.shortcuts import render,redirect
from app.models import Appointment
from datetime import datetime

from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def send_meet_link(request,slug):
    if request.method == 'POST':
        meet_link=request.POST['meet_link']
        update=Appointment.objects.get(appointment_id=slug)
        update.meet_link=meet_link
        update.save()
        return redirect('dasboard')


    else:
        context={
            'appointment_id':slug,
        }
            
        return render(request,'dasboard/doctor/send_meet_link.html',context)
    
