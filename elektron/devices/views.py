# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from devices.models import Device
from devices.serializers import DeviceSerializer, UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from devices.permissions import IsOwnerOrReadOnly

permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
class DeviceList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
class DeviceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
