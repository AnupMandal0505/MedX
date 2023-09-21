from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def dasboard(request):
    return render(request,'dasboard/index.html')