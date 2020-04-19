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
    email = forms.EmailField(label="이메일")
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput())


    def clean_username(self):
        username = self.cleaned_data['username']
        if MyUser.objects.filter(username=username).exists():
            raise forms.ValidationError('이미 해당 아이디는 존재합니다')


class loginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        # fields = "__all__"

    username = forms.CharField(label="아이디", help_text="가입시 입력하신 아이디를 입력하여 주세요")
    password = forms.CharField(label="패스워드", help_text="가입시 입력하신 패스워드를 입력하여 주세요", widget=forms.PasswordInput())

