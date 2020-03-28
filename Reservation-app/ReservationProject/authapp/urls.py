# -*- coding: utf-8 -*-
from django.urls import path
from .views import login, logout, registration, registrationSuccess


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='registration'),
    path('registrationSuccess/', registrationSuccess, name='registrationSuccess'),
]
