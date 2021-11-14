from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    roll = models.IntegerField()

class Employee(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    salary = models.FloatField(default=0.0)
