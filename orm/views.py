from django.shortcuts import render
from .models import Student
from django.db import connection

# Create your views here.

def student(request):
    students=Student.objects.all()
    print(students)
    print(students.query)
    print(connection.queries)

    return render(request,'student.html',{'students':students})
