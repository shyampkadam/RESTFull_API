from rest_framework import serializers
from app1.models import Employee

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = ('email','password','fullname','city','salary')