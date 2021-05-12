from rest_framework import serializers
from .models import *

class TaskSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']

class TaskSerializerList(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']
