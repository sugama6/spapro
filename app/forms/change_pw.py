from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class changePWForm(forms.Form):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password_conf = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))