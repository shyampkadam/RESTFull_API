from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    fullName = serializers.CharField()
    city = serializers.CharField()
    salary = serializers.FloatField()