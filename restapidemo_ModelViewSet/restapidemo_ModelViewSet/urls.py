from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app1 import views

from rest_framework.routers import DefaultRouter

#create router object
router = DefaultRouter()
#register StudentModelViewSet with router
router.register('studentapi',views.StudentModelViewSet, basename='student')
router.register('employeeapi',views.EmployeeModelViewSet, basename='employee')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
