from django.shortcuts import render,redirect
from app.models import User,Appointment,Patient
import random
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMultiAlternatives

from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages


def mail(user_name,Password,email):

    User_name=user_name
    Password=Password
    subject='Password update successful'
    form_email='mastikipathshala828109@gmail.com'
    msg=(f'<p>Hii, <b>{User_name}</b><br>Password Update Successful <br>Password : {Password}<b></b> </p>')
    # to='anupmandal828109@gmail.com'
    to=email
    msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    msg.content_subtype='html'
    msg.send()



@csrf_exempt
def VerifyPasswordOtp(request):

    if request.method == 'POST':
        user_id=request.POST['user_id']
        row_password=request.POST['password']
        password=make_password(row_password)

        user=User.object.get(user_id=user_id) 
        user.password=password
        user.status=1
        user.save()
        mail(user.name,row_password,user.email)

    return render(request,'home/index.html')


# @csrf_exempt
# def VerifyEmailOtp(request):

#     if request.method == 'POST':
#         user_id=request.POST['user_id']
#         row_password=request.POST['password']
#         password=make_password(row_password)

#         user=User.object.get(user_id=user_id) 
#         user.password=password
#         user.status=1
#         user.save()
#         mail(user.name,row_password,user.email)

#     return render(request,'home/index.html')