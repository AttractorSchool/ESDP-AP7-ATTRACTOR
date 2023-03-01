from django import forms
from ratings.models import MemberEventRating


class MemberEventRatingForm(forms.ModelForm):
    score = forms.ChoiceField(
        widget=forms.Select,
        choices=(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        ),
    )
    class Meta:
        model = MemberEventRating
        fields = ['score', 'comment']


        widgets = {
            'comment': forms.Textarea(attrs={'cols': 15, 'rows': 5,  "placeholder": ""}),
        }