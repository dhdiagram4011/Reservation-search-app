# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import TemplateView


class registration(TemplateView):
    template_name = 'authapp/registration.html'


class login(TemplateView):
    template_name = 'authapp/login.html'


class logout(TemplateView):
    template_name = 'authapp/logout.html'


class registrationSuccess(TemplateView):
    template_name = 'authapp/registration_success.html'



