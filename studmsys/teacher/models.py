from django.db import models
from django.core.validators import RegexValidator


class Teacher(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50,validators=[
            RegexValidator(
                regex=r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,50}$',
                message='Password must contain uppercase, lowercase, number and special character'
            )
        ])

    subChoice = [
        ('M','Marathi'),
        ('H','Hindi'),
        ('E','English'),
        ('S','Science'),
        ('MA','Mathematics'),
        ('SC','Social Science'),
        ('G','Deography'),
    ]
    subject = models.CharField(max_length=50, choices= subChoice)

    depChoice =[
        ('MA','Math'),
        ('S','Science'),
        ('M','Marathi'),
        ('E','English'),
        ('M','Hindi'),

    ]
    department = models.CharField(choices=depChoice, max_length=50)

    age = models.IntegerField()
    address = models.TextField()
    