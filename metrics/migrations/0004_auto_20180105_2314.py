# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0003_auto_20180105_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entries',
            name='day',
            field=models.DateField(),
        ),
    ]
