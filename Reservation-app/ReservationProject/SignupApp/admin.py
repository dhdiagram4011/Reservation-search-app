from django.contrib import admin
from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password', 'koreanFirstname', 'koreanLastname', 'englishLastname',
                    'englishFirstname', 'address', 'detailAddress', 'phoneNumber']


admin.site.register(MyUser, MyUserAdmin)