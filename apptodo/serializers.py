from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.db.models import Q

class TaskSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']
    
    def create(self, validated_data):
        return Task.objects.create(name=validated_data['name'],
        description=validated_data['description'],usuario=self.context['request'].user)

class TaskSerializerList(serializers.ModelSerializer):

    usuario = serializers.PrimaryKeyRelatedField(source='usuario.username',queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['name','description','usuario']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','email','password']
    
    def create(self, validated_data):
        user =  User(username=validated_data['username'],
        email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        """usuario = User.objects.get(pk=user.pk)
        Token.objects.create(user=usuario)"""
        return user
    
    def to_representation(self, instance):
        return {
            "nome":instance.username,
            "password":instance.password
        }

class ObterTokenSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()


