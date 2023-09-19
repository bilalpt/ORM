from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response




# Create your views here.

@api_view(['GET'])
def Fun(request):
    students=Student.objects.all()
    serilize=firstserializer(students,many=True)

    return Response({'status': 200,'payload': serilize.data})

@api_view(['POST'])
def post_data(request):
    data=request.data
    one=firstserializer(data=request.data)
    if not one.is_valid():
        return Response({'status':404,'errors':one.errors})
    one.save()
    return Response({'status':200,'payload':one.user,'message':'you passed data will be'})




    
