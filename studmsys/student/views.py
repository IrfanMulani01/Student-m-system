from django.shortcuts import render, redirect
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

    form = LoginStudent()

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        stud = Student.objects.filter(
            username=username,
            password=password
        ).first()

        if stud:
            request.session['stud_id'] = stud.id
            return redirect('dashboard')

        else:
            error = "Invalid Username or Password"
            return render(request, 'temp/login.html', {
                'form': form,
                'error': error
            })

    return render(request, 'temp/login.html', {'form': form})

def studentList(request):
    student = Student.objects.all()
    return render(request, 'temp/studlist.html', {'stud':student})


def studDashboard(request):

    stud_id = request.session.get('student_id')
    stud = Student.objects.filter(id=stud_id).first()
    return render(request, 'temp/index.html', {'stud': stud})