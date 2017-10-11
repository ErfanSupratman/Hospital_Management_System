# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('discharged_timestamp', models.DateTimeField(blank=True, null=True)),
                ('reason', models.CharField(choices=[('Pneumonia', 'Pneumonia'), ('Congestive Heart Failure', 'Congestive Heart Failure'), ('Hardening of the arteries', 'Hardening of the arteries'), ('Heart Attack', 'Heart Attack'), ('Chronic Obstruction Lung Disease', 'Chronic Obstruction Lung Disease'), ('Stroke', 'Stroke'), ('Irregular Heartbeat', 'Irregular Heartbeat'), ('Congestive Heart Failure', 'Congestive Heart Failure'), ('Complications of procedures, devices, implants and grafts', 'Complications of procedures, devices, implants and grafts'), ('Mood Disorders', 'Mood Disorders'), ('Fluid and Electrolyte Disorders', 'Fluid and Electrolyte Disorders'), ('Urinary Infections', 'Urinary Infections'), ('Asthma', 'Asthma'), ('Diabetes mellitus with and without complications', 'Diabetes mellitus with and without complications'), ('Skin Infections', 'Skin Infections'), ('Gallbladder Disease', 'Gallbladder Disease'), ('Gastrointestinal Bleeding', 'Gastrointestinal Bleeding'), ('Hip Fracture', 'Hip Fracture'), ('Appendicitis', 'Appendicitis'), ('Other', 'Other')], max_length=20)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]