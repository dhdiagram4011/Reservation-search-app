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
        if MyUser.objects.filter(username=request.GET['username'],password=request.GET['password']).exists():
            return render(request, 'SignupApp/already_exists.html')
        else:
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
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        res_data = {}
        if not (username and password):
            res_data['error'] = "아이디 패스워드를 모두 채워주세요"
        else:
            customer = MyUser.objects.get(username=username)
            if check_password(password, customer.password):
                request.session['username'] = customer.id
                
                return redirect('loginSuccess')
            else:
                res_data['error'] = "아이디/패스워드가 올바르지 않습니다"
        return render(request, 'SignupApp/login.html', res_data)


def loginSuccess(request):
    userinfo = request.session.get('username')
    print(userinfo)

    if userinfo:
        customer = MyUser.objects.get(pk=userinfo)
        return HttpResponse(customer.username)  
    
    return HttpResponse("로그인이 완료되었습니다")

        #customer = MyUser.objects.filter(username=request.GET['username'])
        #print(customer)
        #return render(request, 'SignupApp/login_success.html')


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')



def unregister(request):
    pass
