# -*- coding: utf-8 -*-
from django.shortcuts import render


def index(request):
    return render(request, 'ReservationApp/index.html')


def revstart(request):
    return render(request, 'ReservationApp/rev_start.html')


def revsuccess(request):
    return render(request, 'ReservationApp/rev_success.html')
