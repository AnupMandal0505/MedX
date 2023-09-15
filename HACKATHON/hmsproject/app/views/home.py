from django.shortcuts import render,redirect
import random
from app.models import Patient,Appointment,Department
from django.contrib import messages


# def unique_number(name):
    # uq=random.randint(1,8)
    # uq=name+str(uq)
    # # print("gn:",uq)
    # try:
    #     n=User.object.get(city=uq)
    #     # print("match")
    #     unique_number(name)
        
    # except:
    #     # print("uq:",uq)
    #     return uq

    # **************************************************
    # name=name
    # while(True):  
    #     uq=random.randint(1,5)
    #     uq=name+str(uq)
    #     try:
    #         n=User.object.get(city=uq)
    #     except:
    #         return uq


        


def home(request):
    
    if request.method == 'POST':
        photos=request.FILES['file']
        print("photo :",photos)

        users=Department.objects.get(dept_id='dept3195')
        users.signature=photos
        users.save()
        redirect('home')


        

    # n=unique_number("user")
    # print(n)
    # t=True
    # while(t==True):  
    #     gn=unique_number()
    #     print("gn:",gn)
    #     gn=str(gn)
    #     try:
    #         n=User.object.get(city=gn)
    #         print("match")
    #     except:
    #         print(gn)
    #         t=False
    return render(request,'home/index.html')
