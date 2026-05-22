from django import forms
from django.shortcuts import render
from .models import Teacher
from student.models import *

class TeacherLogin(forms.Form):
    class Meta:
        model = Teacher
        
        fields = '__all__'
        
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 18:
            raise forms.ValidationError("Age must be 18 or greater than 18")
        
        return age
    
    
class StudentList(forms.Form):
    class Meta:
        model = Student


class ManageSubject(forms.Form):
    class Meta:
        
        model = Teacher
        
        fields = ['subject']