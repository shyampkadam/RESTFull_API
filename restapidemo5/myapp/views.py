from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http.response import HttpResponse

from .models import Student
from .serializers import StudentSerializer
@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None :
            student = Student.objects.get(id=id)
            serializer = StudentSerializer(student)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        student = Student.objects.all()
        serializer = StudentSerializer(student,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')
    

    def post(self,request,*args,**kwargs):
        jsondata= request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    def put(self,request,*args,**kwargs):
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        student = Student.objects.get(id=id)
        serializer = StudentSerializer(student, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'Data updated'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    def delete(self,request,*args,**kwargs):
        jsondata = request.body
        stream = BytesIO(jsondata)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        try:
            student = Student.objects.get(id=id)
        except:
            res = {'msg':'This object not present'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        student.delete()
        res = {'msg':'data deleted !!!'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')






