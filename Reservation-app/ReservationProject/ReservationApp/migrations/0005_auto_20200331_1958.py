# Generated by Django 2.2.1 on 2020-03-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ReservationApp', '0004_auto_20200330_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='comingDay',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='flightsection',
            name='daytogo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
