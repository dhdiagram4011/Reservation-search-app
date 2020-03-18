# -*- coding: utf-8 -*-
from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('revstart/', revstart , name='revstart'),
    path('revsuccess/', revsuccess, name='revsuccess'),
]
