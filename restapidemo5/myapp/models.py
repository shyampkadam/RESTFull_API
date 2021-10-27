from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField()
    city = models.CharField(max_length=40)

    class Meta:
        db_table = 'Student'
