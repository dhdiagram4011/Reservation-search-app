# Generated by Django 2.2.1 on 2020-05-23 04:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0003_emailticket_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailticket',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 23, 4, 50, 40, 25048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='emailticket',
            name='flight_time',
            field=models.DateTimeField(),
        ),
    ]
