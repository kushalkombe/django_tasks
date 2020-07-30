from django.contrib.auth.models import  User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegistrationForm(UserCreationForm):
    Email=forms.EmailField()
    Address=forms.CharField(max_length=250)
    class Meta:
        model=User
        fields=['username','password1','password2']
        # fields ='__all__'