# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import reservationForm
from .models import flightSection
from django.http import HttpResponse


def index(request):
    return render(request, 'ReservationApp/index.html')


def schedule(request):
    pass


def revstart(request):
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/rev_success.html')  # redirect
    else:
        form = reservationForm()
    return render(request, 'ReservationApp/rev_start.html', {'form': form})


def revsuccess(request):
    return render(request, 'ReservationApp/rev_success.html')


def payment(request):
    return render(request, 'ReservationApp/payment.html')


def course_search(request):
    #courses = flightSection.objects.order_by('arrival')
    #arrival = flightSection.objects.filter(arrival=arrival)
    courses = flightSection.objects.filter(arrival=request.GET[flightSection.arrival])
    return render(request, 'ReservationApp/course_list.html', {
        'courses': courses,
    })
