# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Device(models.Model):
    device_ip = models.CharField(max_length=100, blank=True, default='0.0.0.0')
    created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=100, blank=True, default='Elektron')
    state = models.CharField(max_length=100, blank=True, default='Off')
    measure = models.CharField(max_length=100, blank=True, default='') #measure puede ser un objeto en sí mismo


    class Meta:
        ordering = ('created',)
