# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse


# 회원가입 후 가입정보 이메일 발송
def usermail():
    #userlists = MyUser.objects.filter(date_joined__lte=timezone.now()).order_by('-id')[:1]
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    title = "[KOREANAIR]회원가입을 환영합니다"
    html_messsage = render_to_string('SignupApp/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=['dhdiagram@gmail.com'])
    email.content_subtype = "html"
    return email.send()


# 회원가입
def registration(request):
    if request.method == 'GET':
        form = registrationForm(request.GET)
        return render(request, 'SignupApp/registration.html' , {'form':form})
    elif request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
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
            print(request.POST["username"])
            print(request.POST["email"])
            print(request.POST["password"])
            print(request.POST["koreanLastname"])
            print(request.POST["koreanFirstname"])
            print(request.POST["englishLastname"])
            print(request.POST["englishFirstname"])
            print(request.POST["address"])
            print(request.POST["detailAddress"])
            print(request.POST["phoneNumber"])
            usermail()
        ###post.published_date = timezone.now()
        return redirect('registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'SignUpApp/registration_success.html', {'userlists': userlists})


# koreanLastname, koreanFirstname, englishLastname, englishFirstname, address, detailAddress , phoneNumber
# 로그인 시 아이디 존재여부 확인
def login(request):
    if MyUser.objects.filter(username = request.GET['username'],password = request.GET['password']).exists():
        customer = MyUser.objects.filter(username = request.GET['username'],password = request.GET['password'])
        return render(request, 'ReservationApp/rev_start.html', {'customer': customer})
    else:
        form = loginForm()
        return render(request, 'SignupApp/login.html', {'form': form})


#def login(request):
#    if MyUser.objects.filter(username=request.GET['username'], password=request.GET['password']).exists():
#        customer = MyUser.objects.filter(username=request.GET['username'], password=request.GET['password'])
#        print(request.GET['username'])
#        print(request.GET['password'])
#        return render(request, 'ReservationApp/rev_start.html')
#    else:
#        form = loginForm()
#        return render(request, 'SignupApp/login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')


