from rest_framework import serializers
from devices.models import Device
from data.models import Data
from django.contrib.auth.models import User

class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #data = serializers.PrimaryKeyRelatedField(many=True, queryset=Data.objects.all())

    class Meta:
        model = Device
        fields = ('id', 'device_ip', 'device_mac', 'created', 'label', 'state', 'owner')#, 'data')


class UserSerializer(serializers.ModelSerializer):
    devices = serializers.PrimaryKeyRelatedField(many=True, queryset=Device.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'devices')
