from django.db import models
from django.core.validators import RegexValidator


class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50,validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,50}$',
                message='Password must contain uppercase, lowercase, number and special character'
            )
        ])
    dateOfBirth = models.DateField()

    genchoice =[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=genchoice)
    
    classes = models.CharField(max_length=50)

    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fname
    