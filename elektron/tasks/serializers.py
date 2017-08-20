from rest_framework import serializers
from tasks.models import Task
from devices.models import Device
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    task_detail = serializers.HyperlinkedIdentityField(view_name='task-detail', format='html')
    device_detail = serializers.HyperlinkedIdentityField(view_name='task-device', format='html')
    owner = Device.owner

    class Meta:
        model = Task
        fields = ('id',  'label', 'task_detail', 'created', 'device', 'device_detail', 'state',  'owner', 'alert_options')

class DeviceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #highlight = serializers.HyperlinkedIdentityField(view_name='device-highlight', format='html')
    data = serializers.HyperlinkedIdentityField(view_name='device-data', format='html')

    class Meta:
        model = Device
        fields = ('id', 'device_ip', 'device_mac', 'created', 'label', 'state', 'owner', 'data')

class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'tasks')
