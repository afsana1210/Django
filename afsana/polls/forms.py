

from django import forms


class signup(forms.Form):
   
    first_name=forms.CharField()
    second_name=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField()