from django.db import models
from django import forms
from django.contrib.auth.models import User
import recurrence.fields


# Create your models here.

"""
class ExperimentForm(forms.Form):
    administrator = forms.charField()
    name = forms.charField()
    survey = forms.charField()
"""


class Experiment(models.Model):
    name = models.CharField(max_length=50)
    researcher = models.ForeignKey(User)


class Participant(models.Model):
    participant_name = models.CharField(max_length=30)
    phone_id = models.CharField(max_length=16)
    experiment = models.ForeignKey(Experiment)

    class Meta:
        verbose_name_plural = 'group'


class Survey(models.Model):
    participants = models.ManyToManyField(Participant)


class Trigger(models.Model):
    name = models.CharField(max_length=30)
    survey = models.ManyToManyField(Survey)

    class Meta:
        abstract = True


class TimeTrigger(Trigger):
    start = models.TimeField()
    recurrence = recurrence.fields.RecurrenceField()


class GeoTrigger(Trigger):
    ENTER_OR_EXIT = {
        ('EN', 'enter'),
        ('EX', 'exit'),
    }
    lat = models.DecimalField(verbose_name='latitude', max_digits=6, decimal_places=3)
    lon = models.DecimalField(verbose_name='longitude', max_digits=6, decimal_places=3)
    radius = models.PositiveIntegerField()
    event = models.CharField(max_length=2, choices=ENTER_OR_EXIT, default='EN')
    repeats = models.IntegerField()


class ASA(Trigger):
    EXISTS = {
        ('EX', 'exists')
    }
    exists = models.CharField(max_length=4, choices=EXISTS, default='EX')