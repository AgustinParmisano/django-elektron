# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Task, DateTimeTask, DataTask, TaskState, TaskFunction
from devices.models import Device
from django.views import generic

def check_device_mac(**kwargs):
    if not 'device_mac' in kwargs:
        return False
    else:
        if type(kwargs['device_mac']) is list:
            kwargs['device_mac'] = kwargs['device_mac'][0]

    return kwargs

def check_task(**kwargs):

    if not 'taskfunction' in kwargs:
        return False
    else:
        if type(kwargs['taskfunction']) is list:
            kwargs['taskfunction'] = kwargs['taskfunction'][0]

    if not 'label' in kwargs:
        return False
    else:
        if type(kwargs['label']) is list:
            kwargs['label'] = kwargs['label'][0]

    if not 'description' in kwargs:
        return False
    else:
        if type(kwargs['description']) is list:
            kwargs['description'] = kwargs['description'][0]

    try:
        kwargs['taskstate'] = TaskState.objects.get(id=kwargs['taskstate'])
    except Exception as e:
        #TODO: create default taskstates in settings.py
        kwargs['taskstate'] = TaskState.objects.get(name="ready")

    try:
        kwargs['taskfunction'] = TaskFunction.objects.get(id=kwargs['taskfunction'])
    except Exception as e:
        #TODO: create default taskfunctions in settings.py
        kwargs['taskfunction'] = TaskFunction.objects.get(name="shutdown")

    try:
        kwargs['device'] = Device.objects.get(id=kwargs['device'])
    except Exception as e:
        raise
        #TODO: Mensaje de Error: Si no hay devices entonces no se pueden hacer tasks
        #kwargs['device'] = Device.objects.get(name="Elektron")

    try:
        kwargs['owner'] = User.objects.get(username=kwargs['owner'])
    except Exception as e:
        #TODO: create default user in settings.py
        kwargs['owner'] = User.objects.get(username="root")

    return kwargs

class IndexView(generic.ListView):
    model = Task

    def get(self, request, *args, **kwargs):
        """Return all tasks."""
        return JsonResponse({'tasks': list(map(lambda x: x.serialize(), Task.objects.all()))})

class DateTimeTaskIndexView(IndexView):
    model = DateTimeTask

    def get(self, request, *args, **kwargs):
        """Return all date time tasks."""
        return JsonResponse({'datetimetasks': list(map(lambda x: x.serialize(), DateTimeTask.objects.all()))})

class DataTaskIndexView(IndexView):
    model = DataTask

    def get(self, request, *args, **kwargs):
        """Return all data tasks."""
        return JsonResponse({'datatasks': list(map(lambda x: x.serialize(), DataTask.objects.all()))})

class DataTaskDetailView(generic.DetailView):
    model = DataTask

    def get(self, request, *args, **kwargs):
        """Return the selected by id DataTask."""
        try:
            return JsonResponse({'datatasks': DataTask.objects.get(id=kwargs["pk"]).serialize()})
        except Exception as e:
            print "Some error ocurred getting Single DataTask with id: " + str(kwargs["pk"])
            print "Exception: " + str(e)
            return HttpResponse(status=500)

class DateTimeTaskDetailView(generic.DetailView):
    model = DateTimeTask

    def get(self, request, *args, **kwargs):
        """Return the selected by id DateTimeTask."""
        try:
            return JsonResponse({'datetimetasks': DateTimeTask.objects.get(id=kwargs["pk"]).serialize()})
        except Exception as e:
            print "Some error ocurred getting Single DateTimeTask with id: " + str(kwargs["pk"])
            print "Exception: " + str(e)
            return HttpResponse(status=500)

class DatetimeTaskDeviceView(generic.ListView):

    def get(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DateTimeTask.objects.all()

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

    def post(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DateTimeTask.objects.all()

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

class DataTaskDeviceView(generic.ListView):

    def get(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DataTask.objects.all()

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

    def post(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DataTask.objects.all()

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)


class CreateView(generic.View):

    def post(self, request, *args, **kwargs):

        result = check_device_mac(**request.POST)
        task_check = check_task(**request.POST)

        if result:
            try:
                device = Device.objects.get(device_mac=result["device_mac"])
                task.description = result["description"]
                task.label = result["label"]
                task.taskstate = result["taskstate"]
                task.tasksfunction = result["tasksfunction"]
                task.device = result["device"]


            except Task.DoesNotExist:
                task = Task(**result)

            task.save()

        return JsonResponse({'status':True})
