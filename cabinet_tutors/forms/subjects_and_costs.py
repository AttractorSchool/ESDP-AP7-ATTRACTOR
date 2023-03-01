from django import forms
from django.core.exceptions import ValidationError
from django.forms import modelformset_factory

from cabinet_tutors.models import SubjectsAndCosts


class SubjectsAndCostsForm(forms.ModelForm):
    class Meta:
        model = SubjectsAndCosts
        fields = ('subject', 'cost', 'experience')

        widgets = {
            'cost': forms.NumberInput(attrs={'step': '500', 'placeholder': 'мин.стоимость - 500'}),
            'experience': forms.NumberInput(attrs={'step': '0.5', 'placeholder': 'опыт - 0,5'}),
        }


SubjectsAndCostsFormSet = modelformset_factory(
    SubjectsAndCosts,
    fields=('subject', 'cost', 'experience'),
    widgets={
        'cost': forms.NumberInput(
            attrs={'step': '500', 'placeholder': 'мин.стоимость - 500'}),
        'experience': forms.NumberInput(
            attrs={'step': '0.5', 'placeholder': 'опыт - 0,5'}),
    }
)
