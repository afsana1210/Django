from django import forms


class signup(forms.Form):
   # slug=models.TextField(default="this-is-new-slug")
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    second_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email=forms.EmailField(max_length=140,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
