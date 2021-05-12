from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *
# Create your views here.

class TaskViewList(generics.ListAPIView):
    serializer_class = TaskSerializerList
    queryset = Task.objects.all()

class TaskViewCreate(generics.CreateAPIView):
    serializer_class = TaskSerializerCreate
    queryset = Task.objects.all()

class UserViewCreate(generics.CreateAPIView):

    serializer_class = UserSerializer
    
