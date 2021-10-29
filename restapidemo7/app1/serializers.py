from rest_framework import serializers
from .models import Student

def first_latter_capital(value):
    if value.istitle() == False:
        raise serializers.ValidationError('First latter should be capital')
    return value
name = serializers.CharField(validators=[first_latter_capital])
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
