# Generated by Django 2.2.1 on 2020-04-15 07:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SignupApp', '0002_auto_20200413_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='published_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]