# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import reservationForm, datesearchForm
from .models import flightSection, seatClass
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import datetime
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'ReservationApp/index.html')


def intro(request):
    return render(request, 'ReservationApp/intro.html')


# @login_required
def date_search(request):
    if request.method == 'POST':
        form = datesearchForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/course_list.html', {'courses': courses}) 
    else:
        form = datesearchForm()
    return render(request, 'ReservationApp/date_search.html', {'form': form})


@login_required
def revstart(request):
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/rev_success.html') 
    else:
        form = reservationForm()
    return render(request, 'ReservationApp/rev_start.html', {'form': form})


def revsuccess(request):
    return render(request, 'ReservationApp/rev_success.html')


def payment(request):
    courses = flightSection.objects.get(id=request.POST['course_choice'])
    #courses = flightSection.objects.get(id=7)
    print("=======console_msg======")
    print(courses)
    print(courses.id)
    print(courses.starting_point)
    print(courses.arrival)
    print(courses.daytogo)
    print(courses.comingDay)
    return render(request, 'ReservationApp/payment.html', {
        'courses': courses,
    })


# 티켓조회 및 해당 일자에 티켓이 없을 시 별도 안내 페이지 요청
# @login_required
def course_search(request):
    if flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay']).exists():
        courses = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'])
        print(request.GET['starting_point'])
        print(request.GET['arrival'])
        print(request.GET['daytogo'])
        print(request.GET['comingDay'])
        return render(request, 'ReservationApp/course_list.html', {'courses': courses})
    else:
        return render(request, 'ReservationApp/sch_does_not_exist.html')


def date_search_result(request):
    try:
        courses = flightSection.objects.filter(daytogo=request.GET['daytogo'])
    except courses.DoesNotExist:
        raise Http404("해당 출발일에 항공 여정이 없습니다")
    return render(request, 'ReservationApp/date_list.html', {
        'courses': courses,
    })

