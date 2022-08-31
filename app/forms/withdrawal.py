from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class WithdrawalForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'パスワード'}))