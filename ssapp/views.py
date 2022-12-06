from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpReg,LoginReg
from django.contrib import messages
from django.contrib.auth.models import *

def index(request):
    return render(request,'index.html')


def user_signup(request):
    if request.method=="POST":
        form=SignUpReg(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulationz,You have successfully created your account')
            form.save()
        else:
            messages.success(request,'data is invalid')   
    else:
        form=SignUpReg()
    return render(request,'signup.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'Successfully logged out!')
    return HttpResponseRedirect("/")


def user_login(request):
        if request.method=="POST":
            form=LoginReg(request=request,data=request.POST)
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']
                user=authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'You have successfully logged in!')
                    return HttpResponseRedirect('/')
                else:
                    messages.success(request,'Sorry! you have not authorised to access the page!')
        else:
            form=LoginReg()
        return render(request,'login.html',{'form':form})