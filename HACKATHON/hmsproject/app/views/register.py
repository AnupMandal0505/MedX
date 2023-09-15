from django.shortcuts import render,redirect
from django.views import View
from app.models import User,Department
import random

from datetime import datetime

from django.contrib.auth.hashers import make_password

from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def mail(user_id,password,email):
    User_id=user_id
    Password=password
    subject='MedX'
    form_email='mastikipathshala828109@gmail.com'
    msg=(f'<p>welcome Medx <br>User Id : <b>{User_id}</b> <br>Password : {Password}<b></b> </p>')
    to=email
    msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    msg.content_subtype='html'
    msg.send()


def mailOTP(name,otp,email):
    name=name
    otp=otp
    subject='Verify OTP'
    form_email='mastikipathshala828109@gmail.com'
    msg=(f'<p>welcome HMS <br>Hii,<b>{name}</b> <br>otp : {otp}<b></b> </p>')
    to=email
    msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    msg.content_subtype='html'
    msg.send()

# Unique Id........................................
def user_unique_number(name):
    name=name
    while(True):  
        uq=random.randint(1000,9999)
        uq=name+str(uq)
        try:
            n=User.object.get(user_id=uq)
        except:
            return uq

def dept_unique_number(name):
    name=name
    while(True):  
        uq=random.randint(1000,9999)
        uq=name+str(uq)
        try:
            n=Department.objects.get(dept_id=uq)
        except:
            return uq
        
class register(View):
    def get(self, request):
        return render(request,'home/signup.html')
    
    def post(self, request):
        if request.method == 'POST':
            print(12)
            email=request.POST['email']
            name=request.POST['name']
            city=request.POST['city']

            try:
                user=User.object.get(email=email)
                messages.warning(request, 'Already Register !')
                return redirect('signin')
            except:
                try:
                    user_type=request.POST['user_type']
                    if 'user' == user_type :
                        user_id=user_unique_number(user_type)
                        password=user_id
                        print(15)
                        mail(user_id,password,email)
                        password=make_password(password)
                        ab = User.object.create(user_id=user_id,email=email, password=password, name=name,user_type=user_type, city=city,status=0)
                    
                        messages.success(request, f'{user_type} saved Successfully')
                        return redirect('dasboard')
                    else:
                        position=request.POST['position']
                        qualification=request.POST['qualification']
                        pan=request.POST['pan']
                        salary=request.POST['salary']
                        profile=request.FILES['profile']
                        signature=request.FILES['signature']
                        user_id=user_unique_number(user_type)
                        dept_id=dept_unique_number("dept")
                        password=user_id
                        mail(user_id,password,email)
                        password=make_password(password)
                        ab = User.object.create(user_id=user_id,email=email, password=password, name=name,user_type=user_type,city=city,profile=profile,status=0)
                
                        ba = Department.objects.create(dept_ref=ab,dept_id=dept_id,position=position,qualification=qualification,pan=pan,salary=salary,signature=signature)
                    
                        messages.success(request, f'{user_type} saved Successfully')
                        return redirect('dasboard')
                except:
                    user_type="user"
                    user_id=user_unique_number(user_type)
                    password=request.POST['password']
                    otp=random.randint(100000,999999)
                    context={
                        'otp':otp,
                        'user_id':user_id,
                        'email':email,
                        'name':name,
                        'city':city,
                        'user_type':user_type,
                        'password':password

                    }
                    mailOTP(name,otp,email)

                    messages.info(request, "Otp Sent Your Email Id Please Check.")
                    return render(request,'home/verifyuser/verifyuser.html',context)
        





@csrf_exempt
def verify_user(request):
    if request.method == 'POST':
        user_id=request.POST['user_id']
        email=request.POST['email']
        name=request.POST['name']
        city=request.POST['city']
        user_type=request.POST['user_type']
        row_password=request.POST['password']
        password=make_password(row_password)
        
        ab = User.object.create(user_id=user_id,email=email, password=password, name=name,user_type=user_type,city=city,status=1,delete=0)
        mail(user_id,row_password,email)    
        
