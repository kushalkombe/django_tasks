from django.forms import ModelForm
from django import forms
from firstapp.models import *
from django.contrib.auth.password_validation import validate_password
from django.core import validators

class PostForm(forms.ModelForm):
    user_password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    user_confirm_password=forms.CharField(widget=forms.PasswordInput,validators=[validate_password])
    class Meta:
        model = User
        fields=['user_id','user_name','user_username','user_password','user_confirm_password',
        'user_email','user_contact','gender']
    def clean(self):

        # data from the form is fetched using super function
        # super(PostForm, self).clean()
        # extract the username and text field from the data
        user_email=self.cleaned_data.get('user_email')

        # username = self.cleaned_data.get('username')
        # text = self.cleaned_data.get('text')
        # phone_number = self.cleaned_data.get('phone_number')
        user_password=self.cleaned_data.get('user_password')
        user_confirm_password=self.cleaned_data.get('user_confirm_password')

        if '.edu' in user_email:
            self._errors['user_email'] = self.error_class([
                'email should not be .edu'])

        if user_password != user_confirm_password:
            self._errors['user_confirm_password'] = self.error_class([
                'Password doesnt match'])
        # return any errors if found
        return self.cleaned_data




# if len(text) < 10:
#             self._errors['text'] = self.error_class([
#                 'Post Should Contain minimum 10 characters'])
#         if len(str(phone_number))>10:
#             self._errors['phone_number'] = self.error_class([
#                 'Phone_number Should Contain max 10 numbers'])