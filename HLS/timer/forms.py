from django import forms 
from .models import Timer 

class SaveForm(forms.Form):
    study_hour = forms.IntegerField()
    study_min = forms.IntegerField() 
    study_sec = forms.IntegerField() 

    def clean(self):
        cleaned_data = super().clean() 
        user = cleaned_data.get('user')
        study_hour = cleaned_data.get('study_hour')
        study_min = cleaned_data.get('study_min')
        study_sec = cleaned_data.get('study_sec')
