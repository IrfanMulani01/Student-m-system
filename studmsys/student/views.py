from django.shortcuts import render
from .models import *
from .forms import LoginStudent,RegStudent

def registerStudent(request):
    if request.method == 'POST':
        form = RegStudent(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/login.html')
        
    else:
        form = RegStudent()

    return render(request, 'temp/register.html', {'form': form})


def loginStudent(request):
    if request.method == 'POST':
        form = LoginStudent(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'temp/index.html')
        
    else:
        form = LoginStudent()

    return render(request, 'temp/login.html', {'form':form})

def studentList(request):
    student = Student.objects.all()
    return render(request, 'temp/studlist.html', {'stud':student})