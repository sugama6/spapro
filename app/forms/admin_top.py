from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class AdminLoginForm(forms.Form):
    mail_address = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))