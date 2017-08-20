# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tasks.models import Task, DateTimeTask, DataTask
from devices.models import Device
from tasks.serializers import TaskSerializer, DeviceSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from tasks.permissions import IsOwnerOrReadOnly, IsTaskOrNothing
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer as renderers
from rest_framework import renderers
from rest_framework.parsers import JSONParser
import json
import datetime

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    #permission_classes = (IsTaskOrNothing,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer, renderers.JSONRenderer])
    def device(self, request, *args, **kwargs):
        queryset = Device.objects.all()
        task = self.request.query_params.get('task', self.get_object())

        if task is not None:
            device = queryset.filter(task=task)[0]

        device_json = device.__dict__
        device_json['created'] = device_json['created']

        return Response(json.dumps(device_json, default = myconverter))

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
