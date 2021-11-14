from rest_framework import viewsets

from .models import Employee, Student
from .serializers import EmployeeSerializer, StudentSerializer

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer