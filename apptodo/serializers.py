from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TaskSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']
    
    def create(self, validated_data):
        return super().create(validated_data)

class TaskSerializerList(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self, validated_data):
        user =  User(username=validated_data['username'],
        email=validated_data['email'],password=validated_data['password'])
        user.save()
        return user
