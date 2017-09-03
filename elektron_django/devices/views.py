# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Device, DeviceState
from django.views import generic
from django.contrib.auth.models import User

def check_device(**kwargs):

    if not 'device_ip' in kwargs:
        return False
    else:
        if type(kwargs['device_ip']) is list:
            kwargs['device_ip'] = kwargs['device_ip'][0]

    if not 'device_mac' in kwargs:
        return False
    else:
        if type(kwargs['device_mac']) is list:
            kwargs['device_mac'] = kwargs['device_mac'][0]

    if not 'label' in kwargs:
        return False
    else:
        if type(kwargs['label']) is list:
            kwargs['label'] = kwargs['label'][0]

    try:
        kwargs['devicestate'] = DeviceState.objects.get(id=kwargs['devicestate'])
    except Exception as e:
        #TODO: create default devicestates in settings.py
        kwargs['devicestate'] = DeviceState.objects.get(name="off")

    try:
        kwargs['owner'] = User.objects.get(username=kwargs['owner'])
    except Exception as e:
        #TODO: create default user in settings.py
        kwargs['owner'] = User.objects.get(username="root")

    return kwargs

class IndexView(generic.ListView):
    template_name = 'devices_index.html'
    context_object_name = 'latest_devices_list'

    def get_queryset(self):
        """Return the last five published devicess."""
        return Device.objects.order_by('-created')[:5]

class DetailView(generic.DetailView):
    model = Device
    template_name = 'devices_detail.html'


class RecognitionView(generic.View):

    def post(self, request):
        return JsonResponse({'status':True})

class CreateView(generic.View):

    def post(self, request, *args, **kwargs):

        result = check_device(**request.POST)

        if result:
            try:
                device = Device.objects.get(device_mac=result["device_mac"])
                device.device_ip = result["device_ip"]
                device.label = result["label"]
                device.devicestate = result["devicestate"]


            except Device.DoesNotExist:
                device = Device(**result)

            device.save()

        return JsonResponse({'status':True})
