from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class NewsRegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsRegForm, self).__init__(*args, **kwargs)
        self.fields['title'] = forms.CharField(max_length=100)
        self.fields['content'] = forms.CharField(max_length=1000, widget=forms.Textarea())
        
    class Meta:
        model = News
        fields = (
            'title', 'content'
        )
