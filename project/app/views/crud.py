from django.shortcuts import render,redirect
from app.models import User
import random

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
        phone=request.POST['phone']
        password=request.POST['password']
        # password=make_password(row_password)
       
        try:
           
            user=User.object.get(phone=phone) 
            otp=random.randint(1000,9999)
            mail(user.first_name,user.email,otp)
            
            context={
                'otp':otp,
                'phone':phone,
                'password':password

            }

            messages.info(request, "Otp Sent Your Email Id Please Check.")
            return render(request,'otp/verify_password_otp.html',context)


        
        except:

            messages.info(request, "Incorrect Phone Number .")
            redirect('update_password')
    
    return render(request,'dasboard/update_profile/update_password.html')





# def update_password(request):
    
#     if request.method == 'POST':
#         phone=request.POST['phone']
#         password=request.POST['password']
#         # password=make_password(row_password)

#         try:
#             user=User.object.get(phone=phone) 
#             otp=random.randint(1000,9999)
#             # mail(user.first_name,user.email,otp)
#             context={
#                 'otp':otp,
#                 'phone':phone,
#                 'password':password

#             }
        
#             messages.info(request, "Otp Sent Your Email Id Please Check.")
#             return render(request,'otp/verify_password_otp',context)

            

#         except:
#             messages.error(request, "Incorrect Register Phone Number .")
#             return redirect('update_password')

#     return render(request,'dasboard/update_profile/update_password.html')





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
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']

        us=request.user
        us.first_name=first_name
        us.last_name=last_name
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
