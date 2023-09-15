from django.shortcuts import render,redirect
from app.models import User,Appointment,Patient
import random
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMultiAlternatives


from django.contrib import messages

def mail(user_name,email,otp):

    User_name=user_name
    otp=otp
    subject='otp verify'
    form_email='mastikipathshala828109@gmail.com'
    msg=(f'<p>Hii, <b>{User_name}</b><br>otp : <b> {otp}</b> </p>')
    # to='anupmandal828109@gmail.com'
    to=email
    msg=EmailMultiAlternatives(subject,msg,form_email,[to])
    msg.content_subtype='html'
    msg.send()



def update_password(request):
    
    if request.method == 'POST':
        user_id=request.POST['user_id']
        password=request.POST['password']
        # password=make_password(row_password)

        try:
            user=User.object.get(user_id=user_id) 
            otp=random.randint(1000,9999)
            mail(user.name,user.email,otp)
            context={
                'otp':otp,
                'user_id':user_id,
                'password':password

            }
            messages.info(request, "Otp Sent Your Email Id Please Check.")
            return render(request,'dasboard/verify_otp/verify_otp.html',context)
        
        except:
            messages.info(request, "Incorrect UserId .")
            redirect('dasboard')
    
    return render(request,'dasboard/update_profile/update_password.html')

@login_required(login_url='signin')
def add_member(request,slug):

    context={
        'user_type':slug,
    }
    
    return render(request,'dasboard/technician/add_member.html',context)

@login_required(login_url='signin')
def profile(request):
       
    return render(request,'dasboard/update_profile/profile.html')


@login_required(login_url='signin')
def edit_profile(request):
   
    if request.method == 'POST':
        email=request.POST['email']
        city=request.POST['city']
        name=request.POST['name']

        us=request.user
        us.name=name
        us.email=email
        us.city = city
        try:
            profile=request.FILES['profile']
            us.profile=profile
        except:
            pass
        
        us.save()
        return redirect('dasboard')

    return render(request,'dasboard/update_profile/edit_profile.html')
