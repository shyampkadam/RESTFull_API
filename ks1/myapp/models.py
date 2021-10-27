from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=40)
    role = models.CharField(max_length=50)
    city = models.CharField(max_length=70)

    class Meta:
        db_table = 'Employee'
        
