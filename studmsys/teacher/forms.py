from django import forms
from .models import Teacher


class TeacherLogin(forms.Form):
    class Meta:
        model = Teacher
        
        fields = '__all__'
        
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age > 18:
            raise forms.ValidationError("Age must be 18 or greater than 18")
        
        return age
    
    
# class StudentList(forms.Form):
#     class Meta:
#         model = 


