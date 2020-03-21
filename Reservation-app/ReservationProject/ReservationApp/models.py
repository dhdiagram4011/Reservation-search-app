# -*- coding: utf-8 -*-
from django.db import models


class flightNumber(models.Model):
    number = models.CharField(max_length=200)


class flightAircraft(models.Model):
    aircraft_name = models.CharField(max_length=200)
    aircraft_number = models.CharField(max_length=200)


class flightSection(models.Model):
    starting_point = models.CharField(max_length=200)
    arrival = models.CharField(max_length=200)
    flight_time = models.CharField(max_length=200)


class seatClass(models.Model):
    ranking = models.CharField(max_length=200)


class price(models.Model):
    peak_season_price = models.DecimalField(decimal_places=2, max_digits=8)
    low_season_price = models.DecimalField(decimal_places=2, max_digits=8)


class emailTicket(models.Model):
    method_of_payment = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    ranking = models.CharField(max_length=200)
    starting_point = models.CharField(max_length=200)
    arrival = models.CharField(max_length=200)
    flight_time = models.CharField(max_length=200)
    seat_number = models.CharField(max_length=200)
    aircraft_name = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
