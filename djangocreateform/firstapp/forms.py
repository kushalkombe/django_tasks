from firstapp.models import Employee
from django import forms

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'

class NewEmployeeForm(forms.Form):
    eno = forms.IntegerField()
    ename = forms.CharField()
    esal = forms.IntegerField()
    eaddr = forms.CharField()
    email = forms.EmailField()
