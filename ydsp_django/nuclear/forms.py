from django import forms

from . import models

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=60)
    password = forms.CharField(label="Password", max_length=60, widget=forms.PasswordInput)
    class Meta:
        model = models.User
        widgets = {
            'password': forms.PasswordInput()
        }