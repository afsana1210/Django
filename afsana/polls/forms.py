

from django import forms
from .models import signup

# class SignupModelForm(forms.ModelForm):
#    class Meta:
#        model=signup
#        fields='__all__'
#        widgets = {
#             'title': forms.TextInput(
# 				attrs={
# 					'class': 'form-control'
# 					}
# 				),
#         }
# 
class SignupModelForm(forms.ModelForm):
        class Meta:
            model = signup
            fields = ('user','first_name', 'second_name', 'email','password')
      
   