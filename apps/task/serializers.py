from rest_framework import serializers
from apps.task.models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
