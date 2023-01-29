from django import forms

from cabinet_parents.models import OnlinePlatform
from cabinet_tutors.models import TutorStudyFormats


class TutorStudyFormatsForm(forms.ModelForm):
    online = forms.ModelMultipleChoiceField(
        label='Онлайн платформы',
        required=False,
        queryset=OnlinePlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = TutorStudyFormats
        fields = ('online',)
