from django.contrib import admin
from .models import *

class CustAdmin(admin.ModelAdmin):
    list_display = ['fname', 'lname', 'username', 'password', 'gender', 'dateOfBirth', 'address', 'create_at', 'update_at']
    ordering = ['id']
    search_fields = ['fname']
    list_filter= ['username']

admin.site.register(Student, CustAdmin)