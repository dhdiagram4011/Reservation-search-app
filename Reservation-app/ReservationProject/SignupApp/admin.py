from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'koreanFirstname', 'koreanLastname', 'englishLastname',
                    'englishFirstname', 'address', 'detailAddress', 'phoneNumber']


admin.site.register(MyUser, MyUserAdmin)