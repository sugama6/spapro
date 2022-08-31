from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re


class TeachinRegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeachinRegForm, self).__init__(*args, **kwargs)
        RELEASE_CHOICE = (
            (True, '公開'),
            (False, '非公開')
        )
        self.fields['title'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['content'] = forms.CharField(max_length=1000, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['url'] = forms.URLField(max_length=500, widget=forms.TextInput(attrs={'class': 'form-control'}))
        # self.fields['image'] = forms.CharField(max_length=100)
        self.fields['programming_language'] = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.fields['release_flg'] = forms.ChoiceField(choices=RELEASE_CHOICE, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = TeachingMaterials
        fields = (
            'title','content','url',
            # 'image',
            'programming_language','release_flg'
        )

    
