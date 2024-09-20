from django import forms
from .models import homepage
class signup(forms.ModelForm):
    class Meta:
        model=homepage
        fields = ['name','course','hallticketno','email','password','mobile']
    