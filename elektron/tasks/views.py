# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from tasks.models import Task, DateTimeTask, DataTask
from tasks.serializers import TaskSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from tasks.permissions import IsOwnerOrReadOnly, IsTaskOrNothing
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })

class TaskViewSet(viewsets.ModelViewSet):
    lookup_field = "task_ip"
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    #permission_classes = (IsTaskOrNothing,)

    """
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)
    """

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
