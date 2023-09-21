from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class firstserializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields = ['id','firstname','surname','classroom','teacher']

    # def validate(self, data):
    #     if data['classroom']<18 :
    #         raise serializers.ValidationError({'error':'age cannot be 18'})
    #     return data 


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username' , 'password']

        def create(self,validate_data):
            user=User.objects.create(username=validate_data['username'])
            user.set_password(validate_data['password'])
            user.save()
            return user
