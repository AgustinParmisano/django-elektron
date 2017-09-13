# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import dateutil.parser as dp
import datetime
from calendar import monthrange
from datetime import timedelta
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

class DataDayView(generic.DetailView):
    model = Data

    def get(self, request, *args, **kwargs):
        print "kwargs"
        print kwargs

        try:
            data_list = []

            day = kwargs["day"]
            month = kwargs["month"]
            year = kwargs["year"]

            date_string = day + "-" + month + "-" + year
            #date = dp.parse(date_string, timezone.now())
            date_from = datetime.datetime.strptime(date_string, "%d-%m-%Y").date()
            date_to = date_from + timedelta(hours=24)
            data_query = Data.objects.all().filter(date__gte=date_from, date__lte=date_to)
            data_query = list(data_query)

            for data in data_query:
                #print data
                data_dict = {}
                data_dict["data_value"] = data.data_value
                data_dict["data_date"] = data.date
                data_list.insert(0,data_dict)

            #print data_list
            return JsonResponse({'data': data_list})

        except Exception as e:
            print "Some error ocurred getting Day Data"
            print "Exception: " + str(e)
            return HttpResponse(status=500)


class DataMonthView(generic.DetailView):
    model = Data

    def get(self, request, *args, **kwargs):
        print "kwargs"
        print kwargs

        try:
            data_list = []

            day = "1"
            month = kwargs["month"]
            year = kwargs["year"]
            cant_days_month = monthrange(int(year), int(month))[1]

            date_string = day + "-" + month + "-" + year
            #date = dp.parse(date_string, timezone.now())
            date_from = datetime.datetime.strptime(date_string, "%d-%m-%Y").date()
            date_to = date_from + timedelta(days=cant_days_month)
            data_query = Data.objects.all().filter(date__gte=date_from, date__lte=date_to)
            data_query = list(data_query)

            for data in data_query:
                #print data
                data_dict = {}
                data_dict["data_value"] = data.data_value
                data_dict["data_date"] = data.date
                data_list.insert(0,data_dict)

            #print data_list
            return JsonResponse({'data': data_list})

        except Exception as e:
            print "Some error ocurred getting Month Data"
            print "Exception: " + str(e)
            return HttpResponse(status=500)

class DataBetweenDaysView(generic.DetailView):
    model = Data

    def get(self, request, *args, **kwargs):
        print "kwargs"
        print kwargs

        try:
            data_list = []

            day1 = kwargs["day1"]
            month1 = kwargs["month1"]
            year1 = kwargs["year1"]

            day2 = kwargs["day2"]
            month2 = kwargs["month2"]
            year2 = kwargs["year2"]

            date_string1 = day1 + "-" + month1 + "-" + year1
            date_string2 = day2 + "-" + month2 + "-" + year2

            #date = dp.parse(date_string, timezone.now())
            date_from = datetime.datetime.strptime(date_string1, "%d-%m-%Y").date()
            date_to = datetime.datetime.strptime(date_string2, "%d-%m-%Y").date()

            data_query = Data.objects.all().filter(date__gte=date_from, date__lte=date_to)
            data_query = list(data_query)

            for data in data_query:
                #print data
                data_dict = {}
                data_dict["data_value"] = data.data_value
                data_dict["data_date"] = data.date
                data_list.insert(0,data_dict)

            #print data_list
            return JsonResponse({'data': data_list})

        except Exception as e:
            print "Some error ocurred getting Between Days Data"
            print "Exception: " + str(e)
            return HttpResponse(status=500)


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
                    #data.date = datetime.datetime.now() #TODO: Device sends real datetime
                    data.save()

        return JsonResponse({'status':True})
