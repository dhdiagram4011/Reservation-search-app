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


def course_search(request):
    #courses = flightSection.objects.filter(request.GET[flightSection.arrival])  # 도착지 기준 조회
    #courses = flightSection.objects.all(filter=request.GET[flightSection.arrival])
    courses = flightSection.objects.all()  # 전체 리스트 조회
    return render(request, 'ReservationApp/course_list.html', {
        'courses': courses,
    })



#    context = {
#        'courses' : courses,
#    }
#    return HttpResponse(template.render(context, request))