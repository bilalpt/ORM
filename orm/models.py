from django.db import models
# from django.contrib.auth.models import AbstractUser

# Create your models here.


class Teacher(models.Model):
    firstname = models.CharField(max_length=255)
    surname   = models.CharField(max_length=255)

    # def __init__(self):
    #     return self.firstname
    
class Student(models.Model):
    firstname = models.CharField(max_length=255)
    surname   = models.CharField(max_length=255)
    classroom = models.IntegerField()
    teacher   = models.CharField(max_length=100)

class Event(models.Model):
    name      = models.CharField(max_length=200)
    date      = models.DateField()    

        