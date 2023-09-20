from rest_framework import serializers
from .models import *

class firstserializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields = ['id','firstname','surname','classroom','teacher']

    # def validate(self, data):
    #     if data['classroom']<18 :
    #         raise serializers.ValidationError({'error':'age cannot be 18'})
    #     return data 
