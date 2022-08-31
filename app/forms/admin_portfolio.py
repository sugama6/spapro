from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class AdminPortfolioEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminPortfolioEditForm, self).__init__(*args, **kwargs)
        self.fields['url'] = forms.URLField(max_length=500)
        self.fields['title'] = forms.CharField(max_length=100)
        self.fields['content'] = forms.CharField(max_length=1000, widget=forms.Textarea())
        
    class Meta:
        model = Portfolio
        fields = (
            'url', 'title', 'content'
        )