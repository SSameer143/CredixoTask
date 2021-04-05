"""CredixoTask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('teacher/', TemplateView.as_view(template_name='teacher.html'), name='teacher'),
    path('addTeacher/', views.AddTeacher.as_view(), name='add'),
    path('manageTeacher/', views.manageTeacher, name="manage"),
    path('updateteacher/', views.updateTeacher, name='update'),
    path('deleteTeacher', views.deleteTeacher, name='delete'),
    path('student/', views.student, name='student'),
path('student1/', views.student1, name='student1'),
    path('addStd/', views.AddStudent.as_view(), name='addStd'),
    path('manageStd/', views.manageStudent, name="manageStd"),
    path('addStd1/', views.AddStudent1.as_view(), name='addStd1'),
    path('manageStd1/', views.manageStudent1, name="manageStd1"),
    path('updateStudent1/', views.updateStudent1, name='update1'),
    path('deleteStudent2', views.deleteTStudent1, name='delete1'),
    path('details/',views.details,name='details')
]
