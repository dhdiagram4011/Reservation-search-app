# -*- coding: utf-8 -*-
# Generated by Django 2.2.1 on 2020-03-18 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0004_auto_20200318_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='price',
            name='low_season_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='price',
            name='peak_season_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
