from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255,null=False,blank=False,verbose_name="Nome")
    description = models.CharField(max_length=255,null=False,blank=False,verbose_name="Descrição")
    usuario = models.ForeignKey(User,related_name="Task",on_delete=models.CASCADE)
