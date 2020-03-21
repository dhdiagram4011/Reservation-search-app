# -*- coding: utf-8 -*-
from django.db import models


class joinMembership(models.Model):
    koreanLastname = models.CharField(max_length=1, help_text='국문 이름을 입력해 주세요')
    koreanFirstname = models.CharField(max_length=3, help_text='국문 성을 입력해 주세요')
    englishLastname = models.CharField(max_length=10, help_text='영문 이름을 입력해 주세요')
    englishFirstname = models.CharField(max_length=3, help_text='영문 성을 입력해 주세요')
    birthday = models.DateField()
    email = models.EmailField(max_length=50, help_text="해당 이메일 주소로 이메일 티켓이 발송됩니다")
    address = models.CharField(max_length=50)
    detailAddress = models.CharField(max_length=50, help_text='상세 주소를 입력해 주세요')
    phoneNumber = models.CharField(max_length=20, help_text='핸드폰 번호를 입력해 주세요')
    companyName = models.CharField(max_length=10)
    department = models.CharField(max_length=10)
    position = models.CharField(max_length=10)
    fixedlineTelephone = models.CharField(max_length=20, help_text='유선전화번호를 입력해 주세요')

