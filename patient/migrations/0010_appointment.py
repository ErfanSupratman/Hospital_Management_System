# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 21:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_admission_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('status', models.CharField(default='Active', max_length=50)),
                ('startTime', models.DateTimeField()),
                ('endTime', models.DateTimeField()),
            ],
        ),
    ]