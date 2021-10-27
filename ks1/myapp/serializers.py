from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    role = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=40)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.role = validated_data.get('role',instance.role)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance