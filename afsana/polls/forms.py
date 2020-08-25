from django.core import validators

from django import forms
from .models import signup

class SignupModelForm(forms.ModelForm):
   class Meta():
       model=signup
       fields=['user','first_name','second_name','email','password']
       widgets = {
            'first_name': forms.TextInput(
				attrs={
					'class': 'form-control',
                    'placeholder':"First Name",
                    'required':False
					}
				),
            'second_name':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Last Name"
                }
            ),
            'email':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Email address"
                }
            ),
            'password':forms.PasswordInput(
                attrs={
                    'class':'form-control',
                    'placeholder':"Password"
                }
            ),
        }

    #    def clean_email(self,*args,**kwargs):
    #         # cleaned_data=super.clean()
    #         # print(cleaned_data)
    #         email=self.cleaned_data.get('email')
    #         print(email)
    #         qs=signup.objects.filter(email=email)
    #         if qs.exists():
    #             raise forms.ValidationError("this email has already been used please try again")
    #         return email

# class SignupModelForm(forms.ModelForm):
#         class Meta:
#             model = signup
#             fields = ('user','first_name', 'second_name', 'email','password')
      

           