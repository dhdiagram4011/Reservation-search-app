# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from django.contrib.auth import authenticate


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
    username = request.GET.get('username')
    password = request.GET.get('password')
    email = request.GET.get('email')
    address = request.GET.get('address')
    detailAddress = request.GET.get('detailAddress')
    user = authenticate(request, username=username, password=password, email=email, address=address, detailAddress=detailAddress)
    if user is not None:
    #if MyUser.objects.filter(username=request.GET['username'],password=request.GET['password']).exists():
        login(request, user)
        print(username)
        print(password)
        return redirect('loginSuccess')
    else:
        form = loginForm()
        return render(request, 'SignupApp/login.html', {'form':form})



def loginSuccess(request):
    user_pk = MyUser.objects.filter(username=request.GET['username'])
    print(user_pk)

    if MyUser.objects.filter(username=request.GET['username'],password=request.GET['password']).exists():
        username = request.GET['username']
        print(username)
        user_pk = MyUser.objects.get(username=username)
        #return render(request, 'SignupApp/login_success.html')
        return HttpResponse(
            user_pk.username + '님 로그인 되었습니다.<br/>'
            '<br/>'
            '<a href="/reservation/revstart/" style="font-size:15px">항공권 예매 페이지 바로가기</a><br/>'
            '<a href="/auth/myinfo/" style="font-size:15px">내 정보 바로가기</a><br/>'
         )
    else:
        return HttpResponse(
            '아이디 또는 패스워드를 다시 확인해 주세요<br/>'
            '<br/>'
            '<a href="/auth/login/" style="font-size:15px">로그인 페이지로 돌아가기</a>'
            )


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')


def myinfo(request):
    myprofile_pk = MyUser.objects.filter(username=request.GET['username'])

    if myprofile_pk:
        myprofile = MyUser.objects.get(pk=myprofile_pk)
        print(myprofile)
        return HttpResponse(
            "아이디 : " + myprofile.username + '<br/>',
            "이메일 : " + myprofile.email + '<br/>', 
            "주소 : " + myprofile.address + '<br/>',
            "상세주소 : " + myprofile.detailAddress + '<br/>',
            "가입일 : " + myprofile.created_date + '<br/>',  
    )


def unregister(request):
    pass
