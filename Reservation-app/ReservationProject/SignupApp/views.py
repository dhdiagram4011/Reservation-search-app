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
    if request.method == 'GET':
        form = registrationForm(request.GET)
        return render(request, 'SignupApp/registration.html' , {'form':form})
    elif request.method == 'POST':
        form = loginForm(request.POST)
        post = form.save()
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        koreanLastname = request.POST["koreanLastname"]
        koreanFirstname = request.POST["koreanFirstname"]
        englishLastname = request.POST["englishLastname"]
        englishFirstname = request.POST["englishFirstname"]
        address = request.POST["address"]
        detailAddress = request.POST["detailAddress"]
        phoneNumber = request.POST["phoneNumber"]
        ###post.published_date = timezone.now()
    return redirect('registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'SignUpApp/registration_success.html', {'userlists': userlists})


def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if MyUser.objects.filter(username=request.GET['username'],password=request.GET['password']).exists():
            return render(request, 'ReservationApp/rev_start.html')
    else:
        form = loginForm()
        return render(request, 'SignupApp/login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')


