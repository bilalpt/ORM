from rest_framework import serializers
from .models import *

class firstserializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields = ['firstname','surname','classroom','teacher']

    def validate(self, data):
        if data['age']<18 :
            raise serializers.ValidationError({'error':'age cannot be 18'})
        return data   
