# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from devices.models import Device

# Create your models here.

#Abstract Task
class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=100, blank=True, default='ready')
    alert_options = models.CharField(max_length=100, blank=True, default='alert')
    label = models.CharField(max_length=100, blank=True, default='tarea')
    description = models.CharField(max_length=255, blank=True, default='')
    device = models.ForeignKey(Device)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __unicode__(self):
        return self.label

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)

class DateTimeTask(Task):
    date_from = models.DateTimeField(default='0')
    date_to = models.DateTimeField(default='0')

class DataTask(Task):
    data_value = models.CharField(max_length=100, blank=True, default='0')
