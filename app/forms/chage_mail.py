from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class changeMailForm(forms.Form):
    old_mail_address = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_mail_address = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    new_mail_address_conf = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))