# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


class flightAircraftAdmin(admin.ModelAdmin):
    list_display = ['id', 'aircraft_name', 'aircraft_number']


class flightNumberAdmin(admin.ModelAdmin):
    list_display = ['id','number']


class flightSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'starting_point','arrival','flight_time', 'daytogo', 'comingDay']
    #list_display = ['arrival', 'starting_point','flight_time', 'daytogo', 'comingDay']


class priceAdmin(admin.ModelAdmin):
    list_display = ['id','peak_season_price','low_season_price']


class seatClassAdmin(admin.ModelAdmin):
    list_display = ['id','ranking']


class emailTicketAdmin(admin.ModelAdmin):
    list_display = ['id','method_of_payment','price','ranking','starting_point','arrival','flight_time','seat_number','aircraft_name','number']


admin.site.register(flightAircraft, flightAircraftAdmin)
admin.site.register(flightNumber, flightNumberAdmin)
admin.site.register(flightSection, flightSectionAdmin)
admin.site.register(price, priceAdmin)
admin.site.register(seatClass, seatClassAdmin)
admin.site.register(emailTicket, emailTicketAdmin)
