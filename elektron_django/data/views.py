# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from devices.models import Device, DeviceState
from .models import Data
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

def check_data(**kwargs):

    if not 'data' in kwargs:
        return False
    else:
        if type(kwargs['data']) is list:
            kwargs['data'] = kwargs['data'][0]

    return kwargs

class IndexView(generic.ListView):
    template_name = 'data_index.html'
    context_object_name = 'latest_data_list'

    def get_queryset(self):
        """Return the last five published devicess."""
        return Data.objects.order_by('-date')[:5]

class DetailView(generic.DetailView):
    model = Data
    template_name = 'data_detail.html'

class CreateView(generic.View):

    def post(self, request, *args, **kwargs):
        data = Data()
        #print request.POST
        result = check_device(**request.POST)

        if result:
            try:
                device = Device.objects.get(device_mac=result["device_mac"])
            except Device.DoesNotExist:
                device = Device(**result)
                device.save()

            device_enabled = device.enabled
            if device_enabled:
                result = check_data(**request.POST)
                if result:
                    data.data_value = result["data"]
                    data.device = device
                    data.date = datetime.datetime.now() #TODO: Device sends real datetime
                    data.save()

        return JsonResponse({'status':True})
