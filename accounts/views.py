from django.shortcuts import render,redirect
from . import views
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            User.objects.create_user(
                username=cd['username'],
                email=cd['email'],
                password=cd['password'],
                first_name=cd['name'],
                last_name=cd['family'],)
            messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
            return redirect ('hello')
    else:
        form=UserRegisterForm()
    return render (request, 'register.html', {'form':form})


def userlogin(request):
    if request.method=='POST':
        form= UserLoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user= authenticate(request,username= cd['username'],password= cd['password'])
            if user is not None:
                login(request,user) #لاگین میاد یوزر رو داخل ریکوییست میریزه
                messages.success(request, 'خوش آمدید', 'success')
                return redirect('hello')
            else:
                messages.error(request, 'یوزر یا پسورد اشتباه', 'danger')
    else:
        form= UserLoginForm()
    return render (request, 'login.html', {'form':form})


def userlogout(request):
    logout(request)
    messages.success(request, 'شما از حساب کاربری خود خارج شدید', 'success')
    return redirect('hello')
