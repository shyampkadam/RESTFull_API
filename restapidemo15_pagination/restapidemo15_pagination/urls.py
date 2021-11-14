
from django.contrib import admin
from django.urls import path,include
from app1 import views
from app1.populate import populate
populate(20)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/', views.StudentList.as_view()),
]
