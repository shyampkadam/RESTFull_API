from django.shortcuts import render
from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import EmployeeSerializer
from django.http.response import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_employee(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = BytesIO(json_data)
        print(stream)
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = EmployeeSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            resp = JSONRenderer().render(res)
            return HttpResponse(resp,content_type='application/json')

