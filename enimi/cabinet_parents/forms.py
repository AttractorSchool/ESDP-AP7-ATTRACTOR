from django import forms

from cabinet_parents.models import Subject, Program, EducationTime, OnlinePlatform, Survey, Region, City, District, \
    TutorRegion, StudentRegion


class SurveyForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        label='Предметы',
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    programs = forms.ModelMultipleChoiceField(
        label='Программа обучения',
        queryset=Program.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    education_time = forms.ModelChoiceField(
        label='Время для занятий',
        queryset=EducationTime.objects.all(),
        initial='New'
    )
    online = forms.ModelMultipleChoiceField(
        label='Онлайн платформы',
        queryset=OnlinePlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Survey
        fields = ('subjects', 'programs', 'education_time', 'min_cost', 'max_cost', 'online')


class TutorRegionForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        label='Область',
        queryset=Region.objects.all(),
        initial='New'
    )
    city = forms.ModelChoiceField(
        label='Город',
        queryset=City.objects.all(),
        initial='New'
    )
    district = forms.ModelChoiceField(
        label='Район',
        queryset=District.objects.all(),
        initial='New'
    )


    class Meta:
        model = TutorRegion
        fields = ('region', 'city', 'district')


class StudentRegionForm(forms.ModelForm):
    region = forms.ModelChoiceField(
        label='Область',
        queryset=Region.objects.all(),
        initial='New'
    )
    city = forms.ModelChoiceField(
        label='Город',
        queryset=City.objects.all(),
        initial='New'
    )
    district = forms.ModelChoiceField(
        label='Район',
        queryset=District.objects.all(),
        initial='New'
    )


    class Meta:
        model = StudentRegion
        fields = ('region', 'city', 'district')
