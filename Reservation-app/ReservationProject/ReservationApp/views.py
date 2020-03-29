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
    #courses = flightSection.objects.filter(request.GET[flightSection.starting_point,flightSection.arrival,flightSection.flight_time,flightSection.daytogo,flightSection.comingDay
    #])  # 도착지 기준 조회
    courses = flightSection.objects.all()  # 전체 리스트 조회
    #courses = flightSection.objects.filter(arrival='부산')  # 웹 화면에서 도착지 선택 기준 조회(하드코딩 기준)
    #courses = flightSection.objects.filter(arrival=request.GET[flightSection.arrival])  # 웹 화면에서 도착지 선택 기준 조회
    #courses = flightSection.objects.filter(arrival=flightSection.arrival)
    return render(request, 'ReservationApp/course_list.html', {
        'courses': courses,
    })
