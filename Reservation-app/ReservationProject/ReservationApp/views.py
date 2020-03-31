# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import reservationForm
from .models import flightSection, seatClass
from django.http import HttpResponse
from datetime import datetime
#  from django.db.models import Q



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
    #  courses = flightSection.objects.all()
    #  courses = flightSection.objects.filter(Q(starting_point=str(flightSection.starting_point) | Q(arrival=str(flightSection.arrival)) | Q(daytogo=str(flightSection.daytogo)) | Q(comingDay=str(flightSection.comingDay))))
    #  courses = flightSection.objects.filter(arrival=request.GET[flightSection.arrival])
    courses = flightSection.objects.filter(starting_point=str(flightSection.starting_point), arrival=str(flightSection.arrival), daytogo=str(flightSection.daytogo), comingDay=str(flightSection.comingDay))
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