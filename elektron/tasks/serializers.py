from rest_framework import serializers
from tasks.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ('id', 'created', 'state', 'alert_options')
