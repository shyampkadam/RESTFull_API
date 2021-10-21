from django.db import models

class Employee(models.Model):
    email = models.CharField(primary_key=True,max_length=40)
    password = models.CharField(max_length=40)
    fullname = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return self.email + self.fullname

    class Meta:
        db_table = 'employees'
