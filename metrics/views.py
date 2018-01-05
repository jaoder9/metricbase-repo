# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError
from django.http import HttpResponseForbidden

from forms import NewMetricForm, NewEntryForm
from models import Metrics, Entries, Daily


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

	return render(request, 'metrics/showmetric.html', {'form': form, 'entries':entries, 'days':days, 'metric':m})

@login_required
def allmetrics(request):

	metrics = Metrics.objects.filter(user=request.user)
	return render(request, 'metrics/allmetrics.html', {'metrics': metrics})