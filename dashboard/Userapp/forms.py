from Userapp.models import UserReg
from django import forms
from django.core import validators


class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirmpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserReg
        fields = "__all__"

class UserProfile(forms.ModelForm):
    class Meta:
        model = UserReg
        fields = '__all__'
        exclude = ['Password', 'Confirmpassword']



