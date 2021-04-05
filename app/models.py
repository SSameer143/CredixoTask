from django.db import models

class TeacherModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    sub=models.CharField(max_length=15)
    exp=models.CharField(max_length=15)
    pword=models.CharField(max_length=15,default=None)

class StudentModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    sub=models.CharField(max_length=50)
    pword=models.CharField(max_length=15,default=None)