# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Device
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'devices_index.html'
    context_object_name = 'latest_devices_list'

    def get_queryset(self):
        """Return the last five published devicess."""
        return Device.objects.order_by('-created')[:5]


class DetailView(generic.DetailView):
    model = Device
    template_name = 'devices_detail.html'
