
from django.http.response import JsonResponse
from django.shortcuts import render
from io import BytesIO
from rest_framework.parsers import JSONParser
from .models import Employee
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

from .serializers import EmployeeSerializer
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def employee_create(request):
    if request.method == 'GET':
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')

        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data ,content_type='application/json')

    if request.method == 'POST':
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        serializer = EmployeeSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type='application/json')

    if request.method == 'PUT':
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        employee = Employee.objects.get(id=id)
        serializer = EmployeeSerializer(employee,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Updated !!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'DELETE':
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        employee = Employee.objects.get(id=id)
        employee.delete()
        res = {'msg':'Data deleted'}
        return JsonResponse(res,safe=False)







