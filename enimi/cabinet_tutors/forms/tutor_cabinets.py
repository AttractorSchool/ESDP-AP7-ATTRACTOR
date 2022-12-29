from django import forms
from django.forms import Select, Textarea

from cabinet_tutors.models import TutorCabinets, Languages


class TutorCabinetForm(forms.ModelForm):
    languages = forms.ModelMultipleChoiceField(
        label='Языки обучения',
        queryset=Languages.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = TutorCabinets
        fields = ('gender', 'languages', 'about')
        widgets = {
            # 'gender': Select(attrs={
            #     'class': 'form-select',
            #     'style': 'max-width: 100px; height: 36px;',
            # }),
            'about': Textarea(attrs={
                'rows': 5,
                'class': 'border-0 border-top',
                'style': 'width: 400px; overflow:auto; resize:none',
            }),
        }
