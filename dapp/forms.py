from django import forms
from django.contrib.auth.models import User
#from dapp.models import employee
from dapp.models import userprofileinfo

"""class NewUserForm(forms.ModelForm):
    class Meta()    :
        model=employee
        fields='__all__'"""

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=('username', 'email', 'password')

class userprofileinfoform(forms.ModelForm):
    class Meta():
        model=userprofileinfo
        fields=('portfolio_site','profile_pic')