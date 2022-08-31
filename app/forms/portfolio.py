from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

class PortfolioRegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PortfolioRegForm, self).__init__(*args, **kwargs)

        RELEASE_CHOICE = (
            (True, '公開'),
            (False, '非公開')
        )
        self.fields['url'] = forms.URLField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['title'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['content'] = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['release_flg'] = forms.ChoiceField(choices=RELEASE_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))
        
    class Meta:
        model = Portfolio
        fields = (
            'url', 'title', 'content', 'release_flg'
        )