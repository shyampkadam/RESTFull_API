import json
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
def studentview(request,pk):
    student = Student.objects.get(id=pk)
    print(student)
    serializer = StudentSerializer(student)
    print(serializer)
    json_data = JSONRenderer().render(serializer.data)
    print(json_data)
    return HttpResponse(json_data,content_type='application/json')

def allstudentinfo(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    print(serializer)
    data = serializer.data
    print(data)
    json_data = JSONRenderer().render(data)
    
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializer.data ,safe=False)

