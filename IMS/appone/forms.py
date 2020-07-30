from appone.models import *
from django import forms

class CourseForm(models.Form):
    class Meta:
        model=Course
        fields='__all__'

class FacultyForm(models.Form):
    class Meta:
        model=Faculty
        fields='__all__'

class BatchForm(models.Form):
    class Meta:
        model=Batch
        fields=['bno','max_strength','available_strength','bcourse']

class StudentForm(models.Form):
    class Meta:
        model=Student
        fields='__all__'

class StudymaterialForm(models.Form):
    class Meta:
        model=Studymaterial
        fields='__all__'
