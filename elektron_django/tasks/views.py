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
    template_name = 'tasks/index.html'
    context_object_name = 'latest_tasks_list'

    def get_queryset(self):
        """Return the last five published tasks."""
        return Task.objects.order_by('-created')[:5]

class DataTaskDetailView(generic.DetailView):
    model = DataTask
    template_name = 'tasks/datatask_detail.html'

class DateTimeTaskDetailView(generic.DetailView):
    model = DateTimeTask
    template_name = 'tasks/datetimetask_detail.html'


class TaskDeviceView(generic.DetailView):
    model = Task
    #template_name = 'task_data.html'

    def get(self, request, *args, **kwargs):
        print "GETDATA"
        print request.GET
        return JsonResponse({'status':True})

    def post(self, request, *args, **kwargs):
        task = Task()

        result = check_device_mac(**request.POST)

        if result:
            try:
                device = Device.objects.get(device_mac=result["device_mac"])

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                return HttpResponse(status=500)

            if device:
                try:
                    task_list = []
                    task_query = Task.objects.all().filter(device=device)
                    task_query = list(task_query)

                    for task in task_query:
                        #print task
                        task_list.insert(0,task.task_value)

                    #print task_list
                    return JsonResponse({'task': task_list})

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
