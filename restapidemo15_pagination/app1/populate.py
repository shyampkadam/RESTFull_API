import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','restapidemo15_pagination.settings')
import django
django.setup()

from app1.models import *
from faker import Faker
from random import *

faker = Faker()
def populate(n):
    for i in range(n):
        f_name = faker.name()
        f_rollno = randint(100,500)
        student_obj = Student.objects.get_or_create(name=f_name,roll=f_rollno)

if __name__ == '__main__':
    print('Populating data...')
    populate(20)
    print('Populating complete')