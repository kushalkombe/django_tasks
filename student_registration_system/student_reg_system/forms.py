from firstapp.models import Student
from django import forms

class StudentRegistrationform(forms.ModelForm):
    class Meta:
        model=Student
        fields=['srollno','sname','smarks','saddr']

