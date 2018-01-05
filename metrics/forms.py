from django import forms
from .models import Metrics, Entries

class NewMetricForm(forms.ModelForm):

	class Meta:
		model = Metrics
		fields = ('name',)

class NewEntryForm(forms.ModelForm):

	class Meta:
		model = Entries
		fields = ('value', 'day',)