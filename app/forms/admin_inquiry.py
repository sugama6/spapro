from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class InquiryResponseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InquiryResponseForm, self).__init__(*args, **kwargs)

        self.fields['content'] = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Inquiry
        fields = (
            'title', 'content'
        )