from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import *
from .models import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
# Create your views here.
"""
TODO:
Fazer Login
Fazer Obter Token
Testar a criação e leitura de tarefas
"""

class TaskViewList(generics.ListAPIView):
    serializer_class = TaskSerializerList
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(usuario=self.request.user)


class TaskViewCreate(generics.CreateAPIView):
    serializer_class = TaskSerializerCreate
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]

class TaskRetrieve(generics.RetrieveAPIView):
    serializer_class = TaskSerializerCreate
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(usuario=self.request.user)

class UserViewCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ObterTokenView(APIView):

    serializer_class = ObterTokenSerializer
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        username = self.request.POST.get('username',False)
        password = self.request.POST.get('password',False)

        if User.objects.filter(Q(username = username) & Q(password=password)).exists():
            token = Token.objects.filter(Q(user__username = username) & 
            Q(user__password=password)).first()
            return Response({"token": token.key})
        return Response(status=status.HTTP_204_NO_CONTENT)
    
