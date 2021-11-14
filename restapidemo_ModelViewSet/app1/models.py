from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    city = models.CharField(max_length=50)
    class Meta:
        db_table = 'Students'
class Employee(models.Model):
    name = models.CharField(max_length=50)
    salary = models.IntegerField()
    city = models.CharField(max_length=50)
    class Meta:
        db_table = 'Employee'
