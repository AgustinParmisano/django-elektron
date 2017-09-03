# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Data
from django.views import generic
from django.contrib.auth.models import User

def check_device(device):
    try:
        device_object = Device.objects.get(device)
    except Device.DoesNotExist:
        print "Device does not Exist!"
    return device_object

def check_data(**kwargs):

    if not 'data_value' in kwargs:
        return False
    else:
        if type(kwargs['data_value']) is list:
            kwargs['data_value'] = kwargs['data_value'][0]

    if not 'date' in kwargs:
        return False
    else:
        if type(kwargs['date']) is list:
            kwargs['date'] = kwargs['date'][0]

    try:
        kwargs['device'] = Device.objects.get(username=kwargs['device'])
    except Exception as e:
        #TODO: create default user in settings.py
        kwargs['device'] = Device.objects.get(username="unknown")

    return kwargs

class IndexView(generic.ListView):
    template_name = 'data_index.html'
    context_object_name = 'latest_data_list'

    def get_queryset(self):
        """Return the last five published devicess."""
        return Data.objects.order_by('-created')[:5]

class DetailView(generic.DetailView):
    model = Data
    template_name = 'data_detail.html'

class CreateView(generic.View):
    data = Data()

    def post(self, request, *args, **kwargs):

        result = check_data(**request.POST)

        if result:

            device_ok = check_device(result["device"])

            if device_ok != None:
                data.data_value = result["data_value"]
                data.device = device_ok
                data.datedevicestate = datetime.datetime.now() #TODO: Device sends real datetime
                data.save()

        return JsonResponse({'status':True})
