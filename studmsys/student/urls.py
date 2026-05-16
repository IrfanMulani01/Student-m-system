from django.urls import path
from . import views

urlpatterns = [
    path('', views.registerStudent, name='reg'),
    path('login/', views.loginStudent, name='log'),
    path('studlist/', views.studentList, name='list'),
    path('dash/', views.studDashboard, name='dashboard'),
]
