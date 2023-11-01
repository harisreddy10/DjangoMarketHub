from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your Username',
        'class':'w-full py-2 py-4 roundex-xl'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'your password',
        'class':'w-full py-2 py-4 roundex-xl'
    }))


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','password1','password2')


    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'your Username',
        'class':'w-full py-2 py-4 roundex-xl'
    }))
    
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'your Email adress',
        'class':'w-full py-2 py-4 roundex-xl'
    }))
     
    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'your password',
        'class':'w-full py-2 py-4 roundex-xl'
    }))
    
    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
        'class':'w-full py-2 py-4 roundex-xl'
    }))
    
