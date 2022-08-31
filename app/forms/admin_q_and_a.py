from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re


class QandARegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QandARegForm, self).__init__(*args, **kwargs)
        self.fields['question'] = forms.CharField(max_length=500, widget=forms.Textarea())
        self.fields['answer'] = forms.CharField(max_length=500, widget=forms.Textarea())
        self.fields['sort'] = forms.IntegerField()
    
    class Meta:
        model = QandA
        fields = (
            'question',
            'answer',
            'sort'
        )

class QandAEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(QandAEditForm, self).__init__(*args, **kwargs)
        self.fields['question'] = forms.CharField(max_length=500, widget=forms.Textarea())
        self.fields['answer'] = forms.CharField(max_length=500, widget=forms.Textarea())
    
    class Meta:
        model = QandA
        fields = (
            'question',
            'answer'
        )