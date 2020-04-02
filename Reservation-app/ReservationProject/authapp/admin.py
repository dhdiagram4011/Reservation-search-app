# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import skyuser


class skyuserAdmin(admin.ModelAdmin):
    list_display = ['id','koreanLastname', 'koreanFirstname', 'englishLastname',
                    'englishFirstname', 'birthday', 'email',
                    'email', 'address', 'detailAddress', 'phoneNumber',
                    'companyName', 'department', 'position', 'fixedlineTelephone']


admin.site.register(skyuser, skyuserAdmin)



