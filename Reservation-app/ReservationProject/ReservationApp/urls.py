# -*- coding: utf-8 -*-
from django.urls import path
from .views import revstart, revsuccess, index, course_search, payment


urlpatterns = [
    path('', index, name='index'),
    path('revstart/', revstart, name='revstart'),
    #path('revstart/schedule', schedule, name='schedule'),
    path('revsuccess/', revsuccess, name='revsuccess'),
    path('course_search/', course_search, name='course_search'),
    path('payment/', payment, name='payment'),
]
