# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from django.http import HttpResponseForbidden
from django.utils import timezone

from forms import NewMetricForm, NewEntryForm
from models import Metrics, Entries, Daily

from collections import OrderedDict
from datetime import timedelta


@login_required
def newmetric(request):

	if request.method == "POST":
		form = NewMetricForm(request.POST)
		if form.is_valid():
			m = form.save(commit=False)
			m.user = request.user
			try:
				m.save()
			except IntegrityError:
				m = Metrics.objects.get(name=m.name)
			
			return redirect(showmetric, pk=m.pk)
	else:
		form = NewMetricForm()
		return render(request, 'metrics/newmetric.html', {'form': form})

@login_required
def showmetric(request, pk):

	m = Metrics.objects.get(pk=pk)

	if m.user != request.user:
		return HttpResponseForbidden()

	if request.method == "POST":
		form = NewEntryForm(request.POST)
		if form.is_valid():
			e = form.save(commit=False)
			e.day = e.daydate.date()
			e.metric = m
			e.save()

			d, created = Daily.objects.get_or_create(metric=m, day=e.day, defaults={'count':0})
			d.count += e.value
			d.save()
	else:
		form = NewEntryForm()

	entries = Entries.objects.filter(metric=m).order_by('day')
	days = Daily.objects.filter(metric=m).order_by('day')
	today = timezone.now().date()

	data = OrderedDict()
	try:
		iterdate = days.first().day
	except AttributeError:
		iterdate = today - timedelta(7)
	while iterdate <= today:
	
		try:
			data[iterdate] = days.get(day = iterdate).count
		except Daily.DoesNotExist:
			data[iterdate] = 0

		iterdate += timedelta(1)

	return render(request, 'metrics/showmetric.html', {'form': form, 'entries':entries, 'metric':m, 'data':data})

@login_required
def deletemetric(request, pk):
	m = get_object_or_404(Metrics, pk=pk, user=request.user)
	m.delete()
	return redirect(allmetrics)

@login_required
def allmetrics(request):

	metrics = Metrics.objects.filter(user=request.user)
	return render(request, 'metrics/allmetrics.html', {'metrics': metrics})