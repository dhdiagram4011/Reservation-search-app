# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import joinMembership


class joinMembershipAdmin(admin.ModelAdmin):
    list_display = ['koreanLastname', 'koreanFirstname', 'englishLastname',
                    'englishFirstname', 'birthday', 'email',
                    'email', 'address', 'detailAddress', 'phoneNumber',
                    'companyName', 'department', 'position', 'fixedlineTelephone']


admin.site.register(joinMembership, joinMembershipAdmin)



