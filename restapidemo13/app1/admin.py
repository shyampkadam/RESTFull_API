from django.contrib import admin

from .models import Student,Employee

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','roll']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','salary']


