from rest_framework import viewsets
from .serializers import StudentSerializer,EmployeeSerializer
from .models import Student,Employee
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]


class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]