from django import forms
from django.forms.widgets import *
from researcher.models import *

class ExperimentForm(forms.Form):
    survey = forms.CharField(label='XForm ID')
    participants = forms.ModelMultipleChoiceField(queryset=Participant.objects.all())
    trigger_name = forms.CharField(label='trigger name')
    #start_time = forms.TimeField(widget=TimePickerWidget)
    recurrence = forms.CharField(label='recurrence', widget=recurrence.forms.RecurrenceWidget)