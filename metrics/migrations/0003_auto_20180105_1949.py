# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 18:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_auto_20180105_1940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily',
            old_name='value',
            new_name='count',
        ),
    ]