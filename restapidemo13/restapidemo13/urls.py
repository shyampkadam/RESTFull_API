from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app1 import views

router = DefaultRouter()
router.register('studentapi',views.StudentModelViewSet,basename='student')
router.register('employeeapi',views.EmployeeModelViewSet,basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))
]
