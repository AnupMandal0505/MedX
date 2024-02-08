from django.shortcuts import render
from app.models import Patient,Appointment

from django.contrib.auth.decorators import login_required

# only read....................
@login_required(login_url='signin')
def user_prescription(request,slug):
     
    appointment_id=Appointment.objects.get(appointment_id=slug)
    data = Patient.objects.get(patient_ref=appointment_id)
    context = {
        'data':data,
    }
    return render(request,'dasboard/user/prescription.html',context)



# #read Write............................................
# @login_required(login_url='signin')
# def doctor_prescription(request,slug):
#     # data = Patient.objects.get(patient_ref=slug)
#     context = {
#         'data':'data',
#     }
#     return render(request,'dasboard/user/prescription.html',context)