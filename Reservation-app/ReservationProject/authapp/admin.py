# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'koreanLastname', 'koreanFirstname', 'englishLastname',
                    'englishFirstname', 'address', 'detailAddress', 'phoneNumber']


admin.site.register(MyUser, MyUserAdmin)



