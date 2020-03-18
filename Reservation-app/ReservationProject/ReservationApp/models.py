from django.db import models

class Flight_number(models.Model):
    nubmer = models.CharField(max_length=200)


class Flight_aircraft(models.Model):
    aircraft_name = models.CharField(max_lenght=200)
    aircraft_number = models.CharField(max_length=200)


class Flight_section(models.Model):
    starting_point = models.CharField(max_length=200)
    arrival = models.CharField(max_length=200)
    flight_time = models.CharField(max_length=200)


class Seat_class(models.Model):
    ranking = models.CharField(max_length=200)


class Price(models.Model):
    peak_season_price = models.IntegerField(max_length=200)
    low_season_price = models.IntegerField(max_length=200)

