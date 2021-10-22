from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import renderers

def showallemployeeinjsonformat(request):
    employeeQueryset = Employee.objects.all()
    print(employeeQueryset)   # this only for understanding purpose.

    empSerializer = EmployeeSerializer(employeeQueryset,many=True)

    json_data = renderers.JSONRenderer().render(empSerializer.data)

    return HttpResponse(json_data,'application/json')


