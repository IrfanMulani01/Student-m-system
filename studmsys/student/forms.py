from django import forms
from .models import *

class Student_list(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'lname']

class RegStudent(forms.ModelForm):
  
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'username', 'password', 'gender', 'dateOfBirth', 'address']

    password = forms.CharField(
        widget=forms.PasswordInput()
    )
     

    
class LoginStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['username', 'password']

    password = forms.CharField(
        widget=forms.PasswordInput()
    )
     
