# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 06:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('address', models.TextField()),
                ('postal_code', models.TextField()),
                ('latitude', models.TextField()),
                ('longitude', models.TextField()),
                ('smsq', models.TextField()),
                ('operating_hours', models.TextField()),
                ('week_day_start_time', models.TextField()),
                ('week_day_end_time', models.TextField()),
                ('week_end_start_time', models.TextField()),
                ('week_end_end_time', models.TextField()),
            ],
        ),
    ]
