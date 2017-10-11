# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 20:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20171011_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='address',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctorprofile',
            name='department',
            field=models.CharField(blank=True, choices=[('N', 'Neurology'), ('E', 'ENT (Ear, Nose & Throat)'), ('C', 'Cardiovascular'), ('NE', 'Nephrology'), ('O', 'Orthopaediatrics')], max_length=1),
        ),
    ]