# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from data.models import Data
from data.serializers import DataSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from data.permissions import IsOwnerOrReadOnly, IsDataOrNothing
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.renderers import JSONRenderer as renderers

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'data': reverse('device-list', request=request, format=format)
    })


class DataViewSet(viewsets.ModelViewSet):
    lookup_field = "data_value"
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
    """

    permission_classes = (IsDataOrNothing,)
    """
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    """

    @detail_route(methods=['get'])
    def get_data(self, request, pk=None):
        print request.data
        return request.data
