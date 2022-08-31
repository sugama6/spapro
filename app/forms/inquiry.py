from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class InquiryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InquiryForm, self).__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['content'] = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Inquiry
        fields = (
            'title', 'content'
        )