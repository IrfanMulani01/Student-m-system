from django import forms
from .models import *

class TeacherForm(forms.Form):
    class Meta:
        model = Teacher
        
        fields = '__all__'
        
    # def cleanAge(self):
    #     age = 