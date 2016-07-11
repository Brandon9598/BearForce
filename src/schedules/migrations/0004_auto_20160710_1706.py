# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20160710_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='month',
        ),
        migrations.AlterField(
            model_name='shift',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='shift',
            name='time',
            field=models.CharField(choices=[('6AM', '6 A.M.'), ('7AM', '7 A.M.'), ('8AM', '8 A.M.'), ('9AM', '9 A.M.'), ('10AM', '10 A.M.'), ('11AM', '11 A.M.'), ('12PM', '12 P.M.'), ('1PM', '1 P.M.'), ('2PM', '2 P.M.'), ('3PM', '3 P.M.'), ('4PM', '4 P.M.'), ('5PM', '5 P.M.'), ('6PM', '6 P.M.'), ('7PM', '7 P.M.'), ('8PM', '8 P.M.'), ('9PM', '9 P.M.'), ('10PM', '10 P.M.'), ('11PM', '11 P.M.')], default='12PM', max_length=4),
        ),
    ]
