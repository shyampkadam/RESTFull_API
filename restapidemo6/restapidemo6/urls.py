
from django.contrib import admin
from django.urls import path
from app1.views import StudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', StudentAPI.as_view()),
]
