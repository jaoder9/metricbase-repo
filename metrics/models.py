# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Metrics(models.Model):
	name = models.CharField(max_length=100)
	user = models.ForeignKey(User)

	class Meta:
		unique_together = ('name', 'user',)

class Entries(models.Model):
	metric = models.ForeignKey(Metrics)
	day = models.DateField()
	daydate = models.DateTimeField(default=timezone.now)
	value = models.FloatField()

class Daily(models.Model):
	day = models.DateField()
	metric = models.ForeignKey(Metrics)
	count = models.FloatField()