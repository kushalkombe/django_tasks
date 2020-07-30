from django.contrib import admin

# Register your models here.
from firstapp.models import Student
class StudentAdmin(admin.ModelAdmin):
    list_display=['srollno','sname','smarks','saddr']

admin.site.register(Student,StudentAdmin)