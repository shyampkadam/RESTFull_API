from django.contrib import admin
from .models import Employee, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','roll','city']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','salary','city']
    