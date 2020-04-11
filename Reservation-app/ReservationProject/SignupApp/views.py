# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


# 회원가입 후 가입정보 이메일 발송
def usermail(request):
    #userlists = MyUser.objects.filter(date_joined__lte=timezone.now()).order_by('-id')[:1]
    userlists = MyUser.objects.all().order_by('-id')[:1]
    title = "[KOREANAIR]회원가입을 환영합니다"
    html_messsage = render_to_string('SignupApp/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=[skyuser.email])
    email.content_subtype = "html"
    return email.send()


# 회원가입
def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_date['password'])
            new_user.save()
        return redirect('registrationSuccess')
    else:
        form = registrationForm()
        return render(request, 'SignupApp/registration.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/index.html')
    else:
        form = loginForm()
        return render(request, 'SignupApp/login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')


def registrationSuccess(request):
    if request.method == 'GET':
        userlists = MyUser.objects.all().order_by('-id')[:1]
        form = registrationForm(request.POST)
        return render(request, 'SignUpApp/registration_success.html', {'userlists': userlists})
    else:
        form = registrationForm()
    return render(request, 'SignUpApp/registration.html', {'form': form})