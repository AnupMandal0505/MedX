from django.shortcuts import render,redirect
from app.models import User,Appointment,Patient
import random
from django.contrib.auth.hashers import make_password

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMultiAlternatives

from django.views.decorators.csrf import csrf_exempt

from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse




def mail_Update_Password(first_name,password,email):
    try:
        subject = 'Password update successful'
        from_email = 'mastikipathshala828109@gmail.com'

        # Correct template_path and render the HTML template with the provided data
        template_path = 'mail_templates/Password_Update_Successful.html'
        pin=random.randint(9999,99999)
        context = {
                    'first_name': first_name,
                'password':password,
                }
        message = render_to_string(template_path, context)

        to = email

        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')
        msg.send()
    except Exception as e:
            print("smg errr:",e)
            raise Exception("Prob")



@csrf_exempt
def VerifyPasswordOtp(request):

    if request.method == 'POST':
        phone=request.POST['phone']
        row_password=request.POST['password']
        password=make_password(row_password)

        try:
            user=User.objects.get(phone=phone) 
            user.password=password
            user.status=1
            user.save()
            mail_Update_Password(user.first_name,row_password,user.email)
            # Return success response
            return JsonResponse({'success': True, 'message': 'Password Updated successfully'})
        except Exception as e:
            # Return error response
            return JsonResponse({'success': False, 'message': str(e)})