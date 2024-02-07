from django.shortcuts import render,redirect
from app.models import Payment
import random

from django.contrib.auth.decorators import login_required

from django.contrib import messages

def order_unique_number(name):
    name=name
    while(True):  
        uq=random.randint(1000,9999)
        uq=name+str(uq)
        try:
            n=Payment.objects.get(order_id=uq)
        except:
            return uq
        
@login_required(login_url='signin')
def payment(request):
    data=Payment.objects.all()
    context={
        'data':data,
    }

    return render(request,'dasboard/technician/payment.html',context)
