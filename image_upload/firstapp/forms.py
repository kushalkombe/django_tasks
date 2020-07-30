from django import forms
from firstapp.models import Summer

class SummerForm(forms.ModelForm):
    class Meta:
        model=Summer
        fields='__all__'

