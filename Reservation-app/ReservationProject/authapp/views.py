# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import skyuser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


def registrationSuccess(request):
    #userlists = joinmembership.objects.all().order_by('-id')[:1]
    userlists = skyuser.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:1]
    return render(request, 'authapp/registration_success.html', {'userlists': userlists})


# 회원가입 후 가입정보 이메일 발송
def usermail(request):
    userlists = skyuser.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[:1]
    title = "[KOREANAIR]회원가입을 환영합니다"
    html_messsage = render_to_string('authapp/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=[skyuser.email])
    email.content_subtype = "html"
    return email.send()


# 회원가입
def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            posts = form.save()
            koreanLastname = request.POST.get('koreanLastname', None)
            koreanFirstname = request.POST.get('koreanFirstname', None)
            englishLastname = request.POST.get('englishLastname', None)
            englishFirstname = request.POST.get('englishFirstname', None)
            birthday = request.POST.get('birthday', None)
            email = request.POST.get('email', None)
            password = request.POST.get('password', None)
            address = request.POST.get('address', None)
            detailAddress = request.POST.get('detailAddress', None)
            phoneNumber = request.POST.get('phoneNumber', None)
            companyName = request.POST.get('companyName', None)
            department = request.POST.get('department', None)
            position = request.POST.get('position', None)
            fixedlineTelephone = request.POST.get('fixedlineTelephone', None)
            created_date = request.POST.get('created_date', None)
            published_date = request.POST.get('published_date', None)
            usermail()
        return redirect('registrationSuccess')
    else:
        form = registrationForm()
        return render(request, 'authapp/registration.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/index.html')
    else:
        form = loginForm()
        return render(request, 'authapp/login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')








#def registrationSuccess(request):
#    if request.method == 'POST':
#        members = joinMembership.objects.all()
#        form = registrationForm(request.POST)
#        return render(request, 'authapp/registration_success.html', {'members': members})
#    else:
#        form = registrationForm()
#    return render(request, 'authapp/registration.html', {'form': form})
