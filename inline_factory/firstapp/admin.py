from django.contrib import admin
from firstapp.models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','esal','eaddr','email']

admin.site.register(Employee,EmployeeAdmin)