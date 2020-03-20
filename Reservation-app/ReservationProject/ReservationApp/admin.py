# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *

class Flight_aircraftOption(admin.ModelAdmin):
    list_display = ['id', 'aircraft_name','aircraft_number']
admin.site.register(Flight_aircraft, Flight_aircraftOption)



class Flight_numberOption(admin.ModelAdmin):
    list_display = ['id','number']
admin.site.register(Flight_number,Flight_numberOption)



class Flight_sectionOption(admin.ModelAdmin):
    list_display = ['id','starting_point','arrival','flight_time']
admin.site.register(Flight_section,Flight_sectionOption)



class PriceOption(admin.ModelAdmin):
    list_display = ['id','peak_season_price','low_season_price']
admin.site.register(Price,PriceOption)



class Seat_classOption(admin.ModelAdmin):
    list_display = ['id','ranking']
admin.site.register(Seat_class,Seat_classOption)



class Email_ticketOption(admin.ModelAdmin):
    list_display = ['id','method_of_payment','price','ranking','starting_point','arrival','flight_time','seat_number','aircraft_name','number']
admin.site.register(Email_ticket,Email_ticketOption)
