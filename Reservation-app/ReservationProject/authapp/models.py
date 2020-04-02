# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class skyuser(models.Model):
    koreanLastname = models.CharField(max_length=200, help_text='국문 이름을 입력해 주세요')
    koreanFirstname = models.CharField(max_length=200, help_text='국문 성을 입력해 주세요')
    englishLastname = models.CharField(max_length=200, help_text='영문 이름을 입력해 주세요')
    englishFirstname = models.CharField(max_length=200, help_text='영문 성을 입력해 주세요')
    birthday = models.DateField()
    email = models.EmailField(max_length=200, help_text="해당 이메일 주소로 이메일 티켓이 발송됩니다")
    password = models.CharField(max_length=200, help_text="패스워드를 입력하여 주세요")
    address = models.CharField(max_length=200)
    detailAddress = models.CharField(max_length=200, help_text='상세 주소를 입력해 주세요')
    phoneNumber = models.CharField(max_length=200, help_text='핸드폰 번호를 입력해 주세요')
    companyName = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    fixedlineTelephone = models.CharField(max_length=200, help_text='유선전화번호를 입력해 주세요')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

