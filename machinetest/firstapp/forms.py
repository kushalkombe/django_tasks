from .models import *
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
        # fields=['product_name','']
