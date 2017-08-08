from rest_framework import serializers
from data.models import Data
from django.contrib.auth.models import User

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Data
        fields = ('id', 'data_value', 'date', 'device')
