# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import reservationForm


def index(request):
    return render(request, 'ReservationApp/index.html')


def revstart(request):
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/rev_success.html')
    else:
        form = reservationForm()
    return render(request, 'ReservationApp/rev_start.html', {'form':form})


def revsuccess(request):
    return render(request, 'ReservationApp/rev_success.html')
