# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import reservationForm
from .models import flightSection, seatClass
from django.http import HttpResponse
from django.db.models import Q


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
    #courses = flightSection.objects.all()
    courses = flightSection.objects.filter(starting_point=str(flightSection.starting_point), arrival=str(flightSection.arrival), daytogo=str(flightSection.daytogo), comingDay=str(flightSection.comingDay))
    return render(request, 'ReservationApp/course_list.html', {
        'courses': courses,
    })
