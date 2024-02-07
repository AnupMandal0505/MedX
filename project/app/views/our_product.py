from django.shortcuts import render,redirect
from app.models import User

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages
# Create your views here.

def our_product(request):
   
    return render(request,'home/our_product.html')

