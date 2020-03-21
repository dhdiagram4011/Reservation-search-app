# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView


class registration(TemplateView):
    return render(request, 'authapp/registration.html')


class login(TemplateView):
    return render(request, 'authapp/login.html')


class logout(TemplateView):
    return render(request, 'authapp/logout.html')


class registrationSuccess(DetailView):
    return render(request, 'authapp/registration_success.html')





