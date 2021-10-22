from django.shortcuts import render
from io import BytesIO
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import StudentSerializer
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method =='POST':
        json_data = request.body
        print(json_data)
        stream = BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializer(data=python_data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            print('done')
            res = {'msg':'Data created'}
            jsondata = JSONRenderer().render(res)
            return HttpResponse(jsondata,content_type='application/json')
        