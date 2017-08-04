# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from devices.models import Device

# Create your models here.

class Data(models.Model):
    device_ip = models.CharField(max_length=100, blank=True, default='0.0.0.0')
    data_value = models.CharField(max_length=100, blank=True, default='0')
    date = models.DateTimeField(default='0')
    device = models.ForeignKey(Device)

    class Meta:
        ordering = ('date',)

    def save(self, *args, **kwargs):
        super(Data, self).save(*args, **kwargs)
