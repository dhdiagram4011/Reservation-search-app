# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import registrationForm, loginForm
from .models import joinMembership


def registersuccess(request):
    members = joinMembership.objects.all().order_byO('-id')[:1]
    return render(request, 'authapp/registration_success.html', {"members": members})


def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            members = joinMembership.objects.all().order_by('-id')[:1]
            #return render(request, 'authapp/registration_success.html')
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


def registrationSuccess(request):
        members = joinMembership.objects.all().order_by('-id')[:1]
        return render(request, 'authapp/registration_success.html', {"members": members})