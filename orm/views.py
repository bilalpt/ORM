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
from rest_framework.views import APIView




# Create your views here.

class MyApiclass(APIView):

    def get(self,request):
        std=Student.objects.all()
        serial=firstserializer(std,many=True)
        return Response({'status':200,'payload':serial.data})
    
    def post(self,request):
        serialize=firstserializer(data=request.data)
        
        if not serialize.is_valid():
            print(serialize.errors)

            return Response({'status':403, 'respond':'not valid data'})
        serialize.save()
        return Response({'status':200,'exacct':'we got exact data'})

    def patch(self,request):
        try:
            std=Student.objects.filter(id=request.data["id"])
            serialise=firstserializer(std, data=request.data)

            if not serialise.is_valid():
                return Response({'status':403,'response':'validate error'})
            serialise.save()

            return Response({'status':200,'validation':' validation compleated '})
        except Exception as e:
            print(e)
            return Response({'status':403, 'message':'invalid id'})
        
    def delete(self,request):
        try:

            id=request.GET.get('id')
            std=Student.objects.get(id=id)
            std.delete()
            return Response({"ststus":200})
        except Exception as e:
            return Response
        ({'status': 403})
    























# @api_view(['GET'])
# def Fun(request):
#     students=Student.objects.all()
#     serilize=firstserializer(students,many=True)

#     return Response({'status': 200,'payload': serilize.data})

# @api_view(['POST'])
# def post_data(request):
#     data=request.data
#     one=firstserializer(data=request.data)
#     if not one.is_valid():
#         return Response({'status':404,'errors':one.errors})
#     one.save()
#     return Response({'status':200,'payload':one.user,'message':'you passed data will be'})




    
