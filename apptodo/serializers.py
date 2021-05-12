from rest_framework import serializers
from .models import *

class TaskSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']
    
    def validate_name(self,data):
        if data == "":
            return serializers.ValidationError("Campo nome não pode ser vazio")
        return data
    
    def validate_description(self,data):
        if data == "":
            return serializers.ValidationError("Campo description não pode ser vazio")
        return data

class TaskSerializerList(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['name','description']
    
    def validate_name(self,data):
        if data == "":
            return serializers.ValidationError("Campo nome não pode ser vazio")
        return data
    
    def validate_description(self,data):
        if data == "":
            return serializers.ValidationError("Campo description não pode ser vazio")
        return data