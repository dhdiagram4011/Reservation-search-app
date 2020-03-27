# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import registrationForm, loginForm


def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            return render(request, 'authapp/registration_success.html')
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
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            return render(request, 'authapp/registration_success.html')
    else:
        form = registrationForm()
        return render(request, 'authapp/registration.html', {"form": form})