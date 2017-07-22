# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from devices.models import Device
from devices.serializers import DeviceSerializer
from rest_framework import generics

class DeviceList(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer


class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
