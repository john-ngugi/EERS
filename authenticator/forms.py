from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        Widgets = {
            'username': forms.TextInput(attrs ={'class': 'form-control'}),
            'password': forms.TextInput(attrs ={'class': 'form-control'}),
        }

'''class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ('username', 'password')
        Widget = {
            'username': forms.TextInput(attrs ={'class': 'form-control'}),
            'password': forms.TextInput(attrs ={'class': 'form-control'}),
        }'''
        