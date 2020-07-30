from django import forms
from appone.models import *

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['cname','duration','fees']


class BatchForm(ModelForm):
    class Meta:
        model = Batch
        fields=['bno','max_strength','available_strength','bcourse']
        
class FacultyForm(ModelForm):
    class Meta:
        model = Faculty
        fields ='__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
bno=models.IntegerField()
max_strength=models.IntegerField(default=20)
available_strength=models.IntegerField()
date_from=models.DateField()
bcourse=models.ManyToManyField(Faculty)
