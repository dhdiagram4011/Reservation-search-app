# -*- coding: utf-8 -*-
from django.shortcuts import render
from .forms import registrationForm
from django.views.generic import TemplateView


def registration(request):
    if request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            return render(request, 'authapp/registration_success.html')
    else:
        form = registrationForm()
        return render(request, 'authapp/registration.html', {'form': form})


class login(TemplateView):
    template_name = 'authapp/login.html'


class logout(TemplateView):
    template_name = 'authapp/logout.html'


class registrationSuccess(TemplateView):
    template_name = 'authapp/registration_success.html'



