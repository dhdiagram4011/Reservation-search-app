# -*- coding: utf-8 -*-
from django.urls import path
from .views import revstart, revsuccess, index, course_search, payment, date_search_result, date_search, intro


urlpatterns = [
    path('', index, name='index'),
    path('revstart/', revstart, name='revstart'),
    path('intro/', intro, name='intro'),  ##회원가입 or 예매페이지이동
    #path('revstart/schedule', schedule, name='schedule'),
    path('revsuccess/', revsuccess, name='revsuccess'),
    path('course_search/', course_search, name='course_search'),
    path('payment/', payment, name='payment'),
    path('date_search/', date_search, name='date_search'),
    path('date_search_result/', date_search_result, name='date_search_result'),
]
