# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import reservationForm
from .models import flightSection, seatClass
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import datetime


def index(request):
    return render(request, 'ReservationApp/index.html')


def schedule(request):
    pass


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
    return render(request, 'ReservationApp/payment.html')


# 티켓조회 및 해당 일자에 티켓이 없을 시 예외처리
def course_search(request):
    try:
        #courses = flightSection.objects.filter(daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'],starting_point=request.GET['starting_point'],arrival=request.GET['arrival'])
        courses = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'])
    except courses.DoesNotExist:
        raise Http404("해당 출발일에 예약 가능한 항공권이 없습니다")
    return render(request, 'ReservationApp/course_list.html', {
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