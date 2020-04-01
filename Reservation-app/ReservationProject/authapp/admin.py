# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import joinmembership


class joinmembershipAdmin(admin.ModelAdmin):
    list_display = ['id','koreanLastname', 'koreanFirstname', 'englishLastname',
                    'englishFirstname', 'birthday', 'email',
                    'email', 'address', 'detailAddress', 'phoneNumber',
                    'companyName', 'department', 'position', 'fixedlineTelephone']


admin.site.register(joinmembership, joinmembershipAdmin)



