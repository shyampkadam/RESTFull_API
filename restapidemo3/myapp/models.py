from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=40)
    age=models.IntegerField()
    city=models.CharField(max_length=80)

    class Meta:
        db_table='Employees'