# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    koreanLastname = models.CharField(max_length=5, help_text='국문 이름을 입력해 주세요')
    koreanFirstname = models.CharField(max_length=5, help_text='국문 성을 입력해 주세요')
    englishLastname = models.CharField(max_length=10, help_text='영문 이름을 입력해 주세요')
    englishFirstname = models.CharField(max_length=50, help_text='영문 성을 입력해 주세요')
    address = models.CharField(max_length=200)
    detailAddress = models.CharField(max_length=200, help_text='상세 주소를 입력해 주세요')
    phoneNumber = models.CharField(max_length=15, help_text='핸드폰 번호를 입력해 주세요')
