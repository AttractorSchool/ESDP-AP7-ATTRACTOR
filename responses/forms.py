from django import forms
from cabinet_parents.models import Subject, Survey
from responses.models.responses import Response



class ResponseForm(forms.ModelForm):
    # def __init__(self, current_survey, *args, **kwargs):
    #     super(StudentResponseForm, self).__init__(*args, **kwargs)
    #     self.fields['subjects'].queryset = self.fields['subjects'].queryset.filter(surveys=current_survey.pk)

    hello_message = forms.CharField(max_length=3000, label='Приветственное сообщение',
                                    widget=forms.Textarea(attrs={'name': 'body', 'rows': 5, 'cols': 20,
                                                                 'placeholder': 'Вы можете написать и отправить сообщение'}))
    subjects = forms.ModelMultipleChoiceField(
        label='Выберите предметы, по которым готовы заниматься с учеником',
        required=True,
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Response
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        fields = ('hello_message', 'subjects')


class ParentResponseForm(forms.ModelForm):
    def __init__(self, survey_id_list, *args, **kwargs):
        super(ParentResponseForm, self).__init__(*args, **kwargs)
        self.fields['survey'].queryset = self.fields['survey'].queryset.filter(id__in=survey_id_list)

    hello_message = forms.CharField(max_length=3000, label='Приветственное сообщение',
                                    widget=forms.Textarea(attrs={'name': 'body', 'rows': 5, 'cols': 20,
                                                                 'placeholder': 'Вы можете написать и отправить сообщение'}))
    subjects = forms.ModelMultipleChoiceField(
        label='Выберите предметы, по которым хотите заниматься:',
        required=True,
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    survey = forms.ModelChoiceField(
        label='Необходимо выбрать анкету ребёнка:',
        required=True,
        empty_label='Выбрать анкету',
        queryset=Survey.objects.all(),
    )

    class Meta:
        model = Response
        widgets = {
            'message': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        fields = ('hello_message', 'subjects', 'survey')
