from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerStudent),
    path('login/', views.loginStudent),
    path('studlist/', views.studentList),
]
