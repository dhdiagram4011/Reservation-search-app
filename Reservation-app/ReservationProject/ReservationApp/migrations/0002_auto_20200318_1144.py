# -*- coding: utf-8 -*-
# Generated by Django 2.2.1 on 2020-03-18 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flight_number',
            old_name='nubmer',
            new_name='number',
        ),
    ]
