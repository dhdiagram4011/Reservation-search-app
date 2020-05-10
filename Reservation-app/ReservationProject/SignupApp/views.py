# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from .forms import registrationForm, loginForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate
from django.contrib import auth


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
        return redirect('registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'SignupApp/registration_success.html', {'userlists': userlists})


def already_exists(request):
    return render(request, 'SignupApp/already_exists.html')


def login(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'SignupApp/login.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        print(username)
        password = request.POST['password']
        print(password)

    res_data = {}
    if not (username and password):
        res_data['error'] = "아이디/패스워드를 정확히 입력하여 주세요"
    else:
        fuser = request.GET['username']
        print("0 :" + fuser)

        if fuser.password == request.GET['password']:
            request.GET['username'] = fuser
            res = request.GET['username']
            print(res)
            return redirect('loginSuccess')
        else:
            return render(request, 'SignupApp/login_failed.html')



def loginSuccess(request):
    user_pk = MyUser.objects.get(username=request.POST['username'], password=request.POST['password'])

    if user_pk:
        return render(request, 'SignupApp/login_success.html', {'user_pk': user_pk})
    else:
        return render(request, 'SignupApp/login_failed.html')


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')


def myinfo(request):
    myprofile_pk = request.GET['username']
    print("1 :" + myprofile_pk)

    if myprofile_pk:
        #myprofile = MyUser.objects.get(pk=myprofile_pk)
        return render(request, 'SignupApp/myinfo.html', {'myprofile_pk': myprofile_pk})
        #return HttpResponse(
        #    "아이디 : " + myprofile.username + '<br/>',
        #    "이메일 : " + myprofile.email + '<br/>', 
        #    "주소 : " + myprofile.address + '<br/>',
        #    "상세주소 : " + myprofile.detailAddress + '<br/>',
        #    "가입일 : " + myprofile.created_date + '<br/>',  
        #    '<a href="/auth/unregister/"><strong>회원탈퇴</strong></a>',
    #)


def unregister(request):
    pass
