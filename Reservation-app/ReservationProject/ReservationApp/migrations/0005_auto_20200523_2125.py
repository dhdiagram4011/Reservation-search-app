# Generated by Django 2.2.1 on 2020-05-23 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0004_auto_20200523_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailticket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 21, 25, 51, 973786)),
        ),
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 21, 25, 51, 972611)),
        ),
    ]
