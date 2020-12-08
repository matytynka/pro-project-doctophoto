from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']