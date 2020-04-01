# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import joinmembership


def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            members = joinmembership.objects.all().order_by('-id')[:1]
        return render(request, 'authapp/registration_success.html', {'members': members})
        #return redirect('registrationSuccess')
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


def registrationSuccess(request):
    members = joinmembership.objects.all().order_by('-id')[:1]
    return render(request, 'authapp/registration_success.html', {'members': members})


