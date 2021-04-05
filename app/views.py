from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth import authenticate
from .models import TeacherModel,StudentModel


class Home(View):
    def get(self,request):
        return render(request,"index.html")
    def post(self,request):
        uname=request.POST["t1"]
        pword=request.POST["t2"]
        user=authenticate(username=uname,password=pword)
        if user is not None:
            return render(request,"admin.html")
        else:
            print('1')
            try:
                print('2')
                user=TeacherModel.objects.get(name=uname,pword=pword)
                print(user)
                return render(request, "teacherHome.html")
            except TeacherModel.DoesNotExist:
                print("3")
                try:
                    print('4')
                    user=StudentModel.objects.get(name=uname,pword=pword)
                    print('5')
                    return render(request, "StudentHome.html")
                except:
                    return render(request,"index.html",{"msg":"Invalid Username Password"})




class AddTeacher(View):
    def get(self,request):
        return render(request,"addTeacher.html")
    def post(self,request):
        idno=request.POST['t1']
        name=request.POST["t2"]
        subj=request.POST["t3"]
        exp=request.POST["t4"]
        pword = request.POST["t5"]
        TeacherModel(idno=idno,name=name,sub=subj,exp=exp,pword=pword).save()
        return render(request,"teacher.html",{"msg":"Teacher Added Successfully"})


def manageTeacher(request):
    Td=TeacherModel.objects.all()
    return render(request,'manTeacher.html',{"data":Td})


def updateTeacher(request):
    idno = request.GET.get("idno")
    print(idno)
    return render(request, "addTeacher.html", {"id": idno})



def deleteTeacher(request):
    idno = request.GET.get("idno")
    TeacherModel.objects.filter(idno=idno).delete()
    return render(request, "manTeacher.html", {"msg": "Employee Details Deleted"})


class AddStudent(View):
    def get(self, request):
        print(request.GET.get('var'))
        return render(request, "addStudent.html")

    def post(self, request):
        idno = request.POST['t1']
        name = request.POST["t2"]
        subj = request.POST["t3"]
        pword = request.POST["t5"]
        StudentModel(idno=idno, name=name, sub=subj, pword=pword).save()
        return render(request, "student.html", {"msg": "Student Added Successfully"})


def manageStudent(request):
    Sd = StudentModel.objects.all()
    return render(request, 'manStudent.html', {"data": Sd})


def student(request):
    #print(request.GET.get('idno'))
    return render(request,"student.html")
def student1(request):
    #print(request.GET.get('idno'))
    return render(request,"student1.html")


class AddStudent1(View):
    def get(self, request):
        print(request.GET.get('var'))
        return render(request, "addStudent1.html")

    def post(self, request):
        idno = request.POST['t1']
        name = request.POST["t2"]
        subj = request.POST["t3"]
        pword = request.POST["t5"]
        StudentModel(idno=idno, name=name, sub=subj, pword=pword).save()
        return render(request, "student1.html", {"msg": "Student Added Successfully"})


def manageStudent1(request):
    Sd = StudentModel.objects.all()
    return render(request, 'manStudent1.html', {"data": Sd})


def updateStudent1(request):
    idno = request.GET.get("idno")
    return render(request, "addStudent1.html", {"id": idno})


def deleteTStudent1(request):
    idno = request.GET.get("idno")
    TeacherModel.objects.filter(idno=idno).delete()
    return render(request, "manStudent1.html", {"msg": "Employee Details Deleted"})


def details(request):
    Sd=StudentModel.objects.all()
    return render(request,"details.html",{"data":Sd})