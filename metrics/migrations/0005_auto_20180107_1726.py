# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-07 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0004_auto_20180105_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily',
            name='count',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='entries',
            name='value',
            field=models.FloatField(),
        ),
    ]