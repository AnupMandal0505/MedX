from django.shortcuts import render,redirect
from app.models import Appointment
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def history(request):
        ref=request.user
        data=Appointment.objects.get(appointment_ref = ref)
        print(data)
        context = {
            'data':data,
        }
        return render(request,'dasboard/history.html',context)
