# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-20 15:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usepoll', '0008_gym_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]