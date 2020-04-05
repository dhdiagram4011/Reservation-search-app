# -*- coding: utf-8 -*-
from django.db import models

STARTINGPOINT = (
    ('김포', '김포'),
    ('제주', '제주'),
    ('부산', '부산'),
    ('울산', '울산'),
    ('대구', '대구'),
    ('청주', '청주'),
    ('원주', '원주'),
    ('군산', '군산'),
    ('진주/사천', '진주/사천'),
    ('여수/순천', '여수/순천'),
    ('무안', '무안'),
    ('포항', '포항'),
)

ARRIVAL = (
    ('김포', '김포'),
    ('제주', '제주'),
    ('부산', '부산'),
    ('울산', '울산'),
    ('대구', '대구'),
    ('청주', '청주'),
    ('원주', '원주'),
    ('군산', '군산'),
    ('진주/사천', '진주/사천'),
    ('여수/순천', '여수/순천'),
    ('무안', '무안'),
    ('포항', '포항'),
)


class flightNumber(models.Model):
    number = models.CharField(max_length=10)


class flightAircraft(models.Model):
    aircraft_name = models.CharField(max_length=10)
    aircraft_number = models.CharField(max_length=10)


class flightSection(models.Model):
    starting_point = models.CharField(max_length=5, choices=STARTINGPOINT, default='김포')
    arrival = models.CharField(max_length=5, choices=ARRIVAL, default='김포')
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
