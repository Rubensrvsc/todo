from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from .models import *
from django.contrib.auth.models import User
# Create your views here.
"""
TODO:
Fazer Login
Fazer Obter Token
Testar a criação e leitura de tarefas
"""

class TaskViewList(generics.ListAPIView):
    serializer_class = TaskSerializerList
    queryset = Task.objects.all()

class TaskViewCreate(generics.CreateAPIView):
    serializer_class = TaskSerializerCreate
    queryset = Task.objects.all()

class UserViewCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
