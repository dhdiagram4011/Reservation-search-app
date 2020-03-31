# -*- coding: utf-8 -*-
from django.db import models


class flightNumber(models.Model):
    number = models.CharField(max_length=10)


class flightAircraft(models.Model):
    aircraft_name = models.CharField(max_length=10)
    aircraft_number = models.CharField(max_length=10)


class flightSection(models.Model):
    starting_point = models.CharField(max_length=5)
    arrival = models.CharField(max_length=5)
    flight_time = models.DateTimeField()
    daytogo = models.DateField()
    comingDay = models.DateField()

class seatClass(models.Model):
    ranking = models.CharField(max_length=10)


class price(models.Model):
    peak_season_price = models.DecimalField(decimal_places=2, max_digits=8)
    low_season_price = models.DecimalField(decimal_places=2, max_digits=8)


class emailTicket(models.Model):
    method_of_payment = models.CharField(max_length=10)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    ranking = models.CharField(max_length=10)
    starting_point = models.CharField(max_length=10)
    arrival = models.CharField(max_length=10)
    flight_time = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=5)
    aircraft_name = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
