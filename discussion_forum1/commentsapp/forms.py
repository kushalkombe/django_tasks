from commentsapp.models import Comment
from django import forms

# class Commentform(forms.ModelForm):
#     class Meta:
#         model=Comment
#         fields='__all__'
#         exclude=['commentforpost','commentbyuser']

class Commentform(forms.Form):
    commentbox=forms.CharField()
    cfileupload=forms.FileField(required=False)
    cfileupload=forms.FileField(required=False)