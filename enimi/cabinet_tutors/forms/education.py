from django import forms
from django.forms import TextInput

from cabinet_tutors.models import Education


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('institution', 'speciality', 'degree')
        widgets = {
            'institution': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 400px; height: 26px;'
            }),
            'speciality': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 400px; height: 26px;'
            }),
            'degree': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-width: 400px; height: 26px;'
            })
        }
