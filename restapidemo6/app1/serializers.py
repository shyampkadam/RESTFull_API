from rest_framework import serializers

from app1.models import Student
def first_letter_capital(value):
    if value.istitle()==False:
        raise serializers.ValidationError('First latter should be capital')
    return value

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40,validators=[first_letter_capital])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=40,validators=[first_letter_capital])

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance

    # Field level validation
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('seats are full')
        return value

    # Object level validation
    def validate(self, value):
        nm = value.get('name')
        ct = value.get('city')
        if nm.lower()=='shyam' and ct.lower()!='pune':
            raise serializers.ValidationError('City must be Pune')
        return value