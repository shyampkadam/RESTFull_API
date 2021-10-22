from django.db import models

class Employee(models.Model):
    fullName = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    salary = models.FloatField(default=0.0)

    class Meta:
        db_table = 'employees'
