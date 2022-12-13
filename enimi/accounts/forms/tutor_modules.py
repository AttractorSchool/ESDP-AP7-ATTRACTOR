from django import forms

from accounts.models import TutorModule


class TutorModuleForm(forms.ModelForm):
    place_of_study = forms.CharField(label='Место учёбы')
    working_place = forms.CharField(label='Место работы')

    class Meta:
        model = TutorModule
        fields = ('place_of_study', 'working_place')
