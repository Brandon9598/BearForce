# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-10 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='date',
            field=models.CharField(choices=[('JAN', 'January'), ('FEB', 'February'), ('MAR', 'March'), ('APR', 'April'), ('MAY', 'May'), ('JUN', 'June'), ('JUL', 'July'), ('AUG', 'August'), ('SEP', 'September'), ('OCT', 'October'), ('NOV', 'November'), ('DEC', 'December')], default='JAN', max_length=3),
        ),
        migrations.AlterField(
            model_name='shift',
            name='time',
            field=models.CharField(choices=[('AM6', '6 A.M.'), ('AM7', '7 A.M.'), ('AM8', '8 A.M.'), ('AM9', '9 A.M.'), ('AM10', '10 A.M.'), ('AM11', '11 A.M.'), ('PM12', '12 P.M.'), ('PM1', '1 P.M.'), ('PM2', '2 P.M.'), ('PM3', '3 P.M.'), ('PM4', '4 P.M.'), ('PM5', '5 P.M.'), ('PM6', '6 P.M.'), ('PM7', '7 P.M.'), ('PM8', '8 P.M.'), ('PM9', '9 P.M.'), ('PM10', '10 P.M.'), ('PM11', '11 P.M.')], default='PM12', max_length=4),
        ),
    ]
