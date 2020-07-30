from .models import ITJobs,MECHJobs,CIVILJobs
from django import forms

class ITJobForms(forms.ModelForm):
    class Meta:
        model=ITJobs
        fields='__all__'
        exclude=['user_it']


class MECHJobForms(forms.ModelForm):
    class Meta:
        model=MECHJobs
        fields='__all__'
        exclude=['user_mech']


class CIVILJobForms(forms.ModelForm):
    class Meta:
        model=CIVILJobs
        fields='__all__'
        exclude=['user_civil']
