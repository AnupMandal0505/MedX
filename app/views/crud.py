from django.shortcuts import render,redirect
from app.models import User
import random

from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail,EmailMultiAlternatives

from urllib.parse import urlparse

from django.contrib import messages
from django.template.loader import render_to_string
import cloudinary
import cloudinary.uploader


def mail_Forget_Password(first_name,email,otp):
    try:
        subject = 'Password OTP'
        from_email = 'mastikipathshala828109@gmail.com'

        # Correct template_path and render the HTML template with the provided data
        template_path = 'mail_templates/otp_ForgetPassword.html'
        pin=random.randint(9999,99999)
        context = {
                    'first_name': first_name,
                'otp':otp,
                }
        message = render_to_string(template_path, context)

        to = email

        msg = EmailMultiAlternatives(subject, '', from_email, [to])
        msg.attach_alternative(message, 'text/html')
        msg.send()
    except Exception as e:
            print("smg errr:",e)
            raise Exception("Prob")




def update_password(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            user = User.objects.get(phone=phone)
            otp = random.randint(1000, 9999)
            mail_Forget_Password(user.first_name, user.email, otp)  # Assuming you have a function to send OTP via email
            context = {'otp': otp, 'phone': phone, 'password': password}
            messages.info(request, "OTP Sent to Your Email. Please Check.")
            return render(request, 'dasboard/verify_otp/verify_otp.html', context)
        except User.DoesNotExist:
            messages.error(request, "Incorrect Phone Number. Please try again.")
            return redirect('signin')
    else:
        return render(request, 'dasboard/update_profile/update_password.html')
    



@login_required(login_url='signin')
def add_member(request,slug):

    context={
        'user_type':slug,
    }
    
    return render(request,'dasboard/technician/add_member.html',context)

@login_required(login_url='signin')
def profile(request):
       
    return render(request,'dasboard/update_profile/profile.html')

from django.http import HttpResponseBadRequest

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

        if request.method == 'POST' and request.FILES.get('profile'):
            # Get the old profile picture URL from the user object or wherever it's stored
            # old_profile_url = request.user.profile
            
            # # Extract the public ID from the old profile picture URL
            # old_public_id = urlparse(old_profile_url).path.split('/')[-1].split('.')[0]
            
            # try:
            #     # Delete the old profile picture from Cloudinary
            #     cloudinary.uploader.destroy(old_public_id, invalidate=True)
            # except cloudinary.api.Error as e:
            #     # Handle any errors that may occur during deletion
            #     return HttpResponseBadRequest("Failed to delete old profile picture: {}".format(str(e)))

            # Upload the new profile picture to Cloudinary
            profile = request.FILES['profile']
            result = cloudinary.uploader.upload(profile, folder='MedX/profile')
                # Get the URL of the newly uploaded profile picture
            url_cloudinary = result['url']
                
                # Save the URL to the user object or wherever it needs to be stored
            request.user.profile = url_cloudinary
            request.user.save()
        us.save()
                # return redirect('dasboard')

                
    


        return redirect('dasboard')
    else:

        return render(request,'dasboard/update_profile/profile_edit.html')
