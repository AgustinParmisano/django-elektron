# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from devices.models import Device
from devices.serializers import DeviceSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from devices.permissions import IsOwnerOrReadOnly, IsDeviceOrNothing
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework import renderers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'devices': reverse('device-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    #lookup_field = "device_ip"
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)


    #permission_classes = (IsDeviceOrNothing,)


    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def data(self, request, *args, **kwargs):
        queryset = Data.objects.all()
        device = self.get_object()
        return Response(device)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
