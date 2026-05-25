from django.shortcuts import render
from .models import *
from .forms import *

def teacherLogin(request):
    if request == 'POST':
        form = TeacherLogin(request.post)
        if form.is_valid():
            form.save()
            return render(request, 'temp/dashboard.html')
    else:
        form = TeacherLogin()
        
    return render(request, 'temp/login.html', {'form': form})


def studentList(request):
    student = Student.objects.all()
    return render(request, 'temp/studentList.html', {'stud': student})

def manageSubject(request):
    subject = Teacher.objects.values('subject')
    return render(request, 'temp/subject.html', {'sub': subject})