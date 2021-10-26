from rest_framework import serializers

from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=40)
    age=serializers.IntegerField()
    city=serializers.CharField(max_length=80)

    def create(self,validated_data):
        return Employee.objects.create(**validated_data)

