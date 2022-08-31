from django import forms
from django.core.exceptions import ValidationError
from app.models import *
import re

from django.contrib.admin.widgets import AdminDateWidget

class GoalRegForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GoalRegForm, self).__init__(*args, **kwargs)
        self.fields['one_year_later'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['ten_years_later'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['learning_programming_why'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['selected_spapro_why'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['how_much_effort'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['what_i_can_do'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['how_can_i_be'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['how_long_want_to_be'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['keep_a_promise'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['key_man'] = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['orientation_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['html_css_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['javascript_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['python1_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['python2_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['sql_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['django_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['portfolio_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['job_change_expected_date'] = forms.DateField(widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])

    class Meta:
        model = Goal
        fields = (
            'one_year_later',
            'ten_years_later',
            'learning_programming_why',
            'selected_spapro_why',
            'how_much_effort',
            'what_i_can_do',
            'how_can_i_be',
            'how_long_want_to_be',
            'keep_a_promise',
            'key_man',
            'orientation_expected_date',
            'html_css_expected_date',
            'javascript_expected_date',
            'python1_expected_date',
            'python2_expected_date',
            'sql_expected_date',
            'django_expected_date',
            'portfolio_expected_date',
            'job_change_expected_date'
        )
        widgets = {
            'orientation_expected_date': AdminDateWidget(),    #インポートしたウィジェットを使う指示
        }

class GoalEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GoalEditForm, self).__init__(*args, **kwargs)
        self.fields['one_year_later'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['ten_years_later'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['learning_programming_why'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['selected_spapro_why'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['how_much_effort'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['what_i_can_do'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['how_can_i_be'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['how_long_want_to_be'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['keep_a_promise'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['key_man'] = forms.CharField(required=False, max_length=100, widget=forms.Textarea(attrs={'class': 'form-control'}))
        self.fields['orientation_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['html_css_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['javascript_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['python1_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['python2_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['sql_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['django_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['portfolio_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])
        self.fields['job_change_expected_date'] = forms.DateField(required=False, widget=forms.DateTimeInput(attrs={'class': 'form-control', "type": "date"}),input_formats=['%Y-%m-%d'])

    class Meta:
        model = Goal
        fields = (
            'one_year_later',
            'ten_years_later',
            'learning_programming_why',
            'selected_spapro_why',
            'how_much_effort',
            'what_i_can_do',
            'how_can_i_be',
            'how_long_want_to_be',
            'keep_a_promise',
            'key_man',
            'orientation_expected_date',
            'html_css_expected_date',
            'javascript_expected_date',
            'python1_expected_date',
            'python2_expected_date',
            'sql_expected_date',
            'django_expected_date',
            'portfolio_expected_date',
            'job_change_expected_date'
        )
        widgets = {
            'orientation_expected_date': AdminDateWidget(),    #インポートしたウィジェットを使う指示
        }