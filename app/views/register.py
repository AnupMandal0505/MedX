from django.shortcuts import render,redirect
from django.views import View
from app.models import User,Department
import random
from django.http import JsonResponse, HttpResponse

from datetime import datetime

from django.contrib.auth.hashers import make_password

from django.core.mail import send_mail,EmailMultiAlternatives
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string


# Create your views here.

# def mail(phone,password,email):
#     phone=phone
#     Password=password
#     subject='MedX'
#     form_email='mastikipathshala828109@gmail.com'
#     msg=(f'<p>welcome Medx <br>User Id : <b>{phone}</b> <br>Password : {Password}<b></b> </p>')
#     to=email
#     msg=EmailMultiAlternatives(subject,msg,form_email,[to])
#     msg.content_subtype='html'
#     msg.send()


    



# def mailOTP(name,otp,email):
#     name=name
#     otp=otp
#     subject='Verify OTP'
#     form_email='mastikipathshala828109@gmail.com'
#     msg=(f'<p>welcome HMS <br>Hii,<b>{name}</b> <br>otp : {otp}<b></b> </p>')
#     to=email
#     msg=EmailMultiAlternatives(subject,msg,form_email,[to])
#     msg.content_subtype='html'
#     msg.send()

def mail_User_Info(first_name,last_name,phone,password,email):
    try:
        subject = 'Account Verification'
        from_email = 'mastikipathshala828109@gmail.com'

        # Correct template_path and render the HTML template with the provided data
        template_path = 'mail_templates/after_register_info.html'
        pin=random.randint(9999,99999)
        context = {
                    'first_name': first_name,
                    'last_name': last_name,
                   'phone': phone,
                'password':password,
                }
        message = render_to_string(template_path, context)

        to = email

        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')
        msg.send()
        return pin
    except Exception as e:
        print("smg errr:",e)
        raise Exception("Prob")


def mailOTP(name,otp,email):
    try:
        subject = 'Account Verification'
        from_email = 'mastikipathshala828109@gmail.com'

        # Correct template_path and render the HTML template with the provided data
        template_path = 'mail_templates/otp_verify.html'
        pin=random.randint(9999,99999)
        context = {'name': name,
                'otp':otp,
                }
        
        message = render_to_string(template_path, context)

        to = email

        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')
        msg.send()
        return pin
    except Exception as e:
        print("smg errr:",e)
        raise Exception("Prob")
# Unique Id........................................
# def user_unique_number(name):
#     name=name
#     while(True):  
#         uq=random.randint(1000,9999)
#         uq=name+str(uq)
#         try:
#             n=User.object.get(phone=uq)
#         except:
#             return uq

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
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            phone=request.POST['phone']
            
            
            try:
                user=User.objects.get(phone=phone)
                messages.warning(request, 'Already Register !')
                return redirect('signin')
            except:
                try:
                    user_type=request.POST['user_type']
                    city=request.POST['city']
                    if 'user' == user_type :
                        
                        password=phone
                        mail_User_Info(first_name,last_name,phone,password,email)
                        password=make_password(password)
                        ab = User.objects.create(phone=phone,email=email, password=password, first_name=first_name,last_name=last_name,city=city, user_type=user_type,status=0)
                    
                        messages.success(request, f'{user_type} saved Successfully')
                        return redirect('dasboard')
                    else:
                        position=request.POST['position']
                        qualification=request.POST['qualification']
                        pan=request.POST['pan']
                        salary=request.POST['salary']
                        profile=request.FILES['profile']
                        signature=request.FILES['signature']
                        dept_id=dept_unique_number("dept")
                        password=phone
                        mail_User_Info(first_name,last_name,phone,password,email)
                        password=make_password(password)
                        ab = User.objects.create(phone=phone,email=email, password=password, first_name=first_name,last_name=last_name,city=city, user_type=user_type,profile=profile,status=0)
                    
                        ba = Department.objects.create(dept_ref=ab,dept_id=dept_id,position=position,qualification=qualification,pan=pan,salary=salary,signature=signature)
                    
                        messages.success(request, f'{user_type} saved Successfully')
                        return redirect('dasboard')
                except:
                    user_type="user"
                    password=request.POST['password']
                    otp=random.randint(1000,9999)
                    context={
                        'phone':phone,
                        'first_name':first_name,
                        'last_name':last_name,
                        'email':email,
                        'user_type':user_type,
                        'password':password,
                        'otp':otp,

                    }
                    mailOTP(first_name,otp,email)

                    messages.info(request, "Otp Sent Your Email Id Please Check.")
                    return render(request,'home/verifyuser/verifyuser.html',context)
        





# @csrf_exempt
# def verify_user(request):
#     if request.method == 'POST':
#         phone=request.POST['phone']
#         email=request.POST['email']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         user_type=request.POST['user_type']
#         row_password=request.POST['password']
#         password=make_password(row_password)
#         ab = User.object.create(phone=phone, first_name=first_name, last_name=last_name, email=email, password=password,user_type=user_type,status=1)
#         mail(phone,row_password,email)    

@csrf_exempt  
def verify_user(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_type = request.POST['user_type']
        row_password = request.POST['password']
        password = make_password(row_password)
        try:
            # Create the user
            new_user = User.objects.create(phone=phone, first_name=first_name, last_name=last_name, email=email, password=password, user_type=user_type, status=1)
            # Send email
            mail_User_Info(first_name,last_name,phone,row_password,email)            
            # Return success response
            return JsonResponse({'success': True, 'message': 'User created successfully'})
        except Exception as e:
            # Return error response
            return JsonResponse({'success': False, 'message': str(e)})