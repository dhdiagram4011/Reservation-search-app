# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import reservationForm, datesearchForm
from .models import flightSection, seatClass
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import datetime


def index(request):
    return render(request, 'ReservationApp/index.html')


def schedule(request):
    pass


def date_search(request):
    if request.method == 'POST':
        form = datesearchForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/course_list.html', {'courses': courses}) 
    else:
        form = datesearchForm()
    return render(request, 'ReservationApp/date_search.html', {'form': form})


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
    course_select_result = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'])
    return render(request, 'ReservationApp/payment.html', {
        'course_select_result': course_select_result,
    })


# 티켓조회 및 해당 일자에 티켓이 없을 시 별도 안내 페이지 요청
def course_search(request):
    if flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay']).exists():
        courses = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'])
        return render(request, 'ReservationApp/course_list.html', {'courses': courses})
    else:
        return render(request, 'ReservationApp/sch_does_not_exist.html')


#def course_search(request):
#    try:
#        courses = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'])
#    except 60:
#        raise Http404("해당 출발일에 예약 가능한 항공권이 없습니다")
#    return render(request, 'ReservationApp/course_list.html', {
#        'courses': courses,
#    })


def date_search_result(request):
    try:
        courses = flightSection.objects.filter(daytogo=request.GET['daytogo'])
    except courses.DoesNotExist:
        raise Http404("해당 출발일에 항공 여정이 없습니다")
    return render(request, 'ReservationApp/date_list.html', {
        'courses': courses,
    })


#def course_search(request):
#    course_pk = request.GET['arrival']

#    if course_pk:
#        course = flightSection.objects.get(pk=course_pk)
#        return HttpResponse(
#            "출발지 :  " + str(course.starting_point) + '<br/>'
#            "도착지 :  " + str(course.arrival) + '<br/>'
#            "비행시간 :  " + course.flight_time + '<br/>'
#            "가는날 :  " + course.daytogo + '<br/>'
#            "오는날 :  " + course.comingDay + '<br/>'
#        )