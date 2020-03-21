# -*- coding: utf-8 -*-
from django.urls import path
from .views import login, logout, registration, registrationSuccess


urlpatterns = [
    path('login/', login.as_view(), name='login'),
    path('logout/', logout.as_view(), name='logout'),
    path('registration/', registration.as_view(), name='registration'),
    path('registrationSuccess/', registrationSuccess.as_view(), name='registrationSuccess'),
]
