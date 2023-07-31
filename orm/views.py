from django.shortcuts import render
from .models import Student
from django.db import connection
from django.db.models import Q
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime




# Create your views here.

# def student(request):
#     students=Student.objects.all()
#     # print(students)
#     print(students.query)
#     print(connection.queries)

#     return render(request,'student.html',{'students':students})


def student(request):

    # student=Student.objects.filter(surname__startswith='w',firstname='h')

    student=Student.objects.filter(Q(firstname__startswith='h') & Q(surname__startswith='w'))

    # student=Student.objects.filter(Q(surname__startwith='w') and Student.objects.filter(firstname__startwith='h')





    print(student)
    print(student.query)
    print(connection.queries)

    return render(request,'student.html',{'student':student})

def crud(request):
    return render (request,'crud.html')



    
