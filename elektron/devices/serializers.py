from rest_framework import serializers
from devices.models import Device
from django.contrib.auth.models import User

class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Device
        fields = ('id', 'device_ip', 'label', 'state', 'measure', 'owner')


class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices')
