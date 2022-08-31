from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class LoginForm(forms.Form):
    login_id = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ログインID', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'パスワード', 'class': 'form-control'}))
