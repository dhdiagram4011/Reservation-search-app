from django import forms
from .models import MyUser
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect


class registrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'koreanLastname', 'koreanFirstname', 'englishLastname', 'englishFirstname', 'email', 'password', 'address', 'detailAddress', 'phoneNumber']


    username = forms.CharField(label="로그인아이디")
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput())


class loginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        # fields = "__all__"

    username = forms.CharField(label="아이디", help_text="가입시 입력하신 아이디를 입력하여 주세요")
    password = forms.CharField(label="패스워드", help_text="가입시 입력하신 패스워드를 입력하여 주세요", widget=forms.PasswordInput())

