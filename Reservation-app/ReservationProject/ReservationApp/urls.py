# -*- coding: utf-8 -*-
from django.urls import path
from .views import revstart, revsuccess, index


urlpatterns = [
    path('', index, name='index'),
    path('revstart/', revstart, name='revstart'),
    #path('revstart/schedule', schedule, name='schedule'),
    path('revsuccess/', revsuccess, name='revsuccess'),
]
