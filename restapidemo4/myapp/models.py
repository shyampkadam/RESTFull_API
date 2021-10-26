from django.db import models

class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=40)
    city = models.CharField(max_length=50)

    class Meta:
        db_table = 'students'