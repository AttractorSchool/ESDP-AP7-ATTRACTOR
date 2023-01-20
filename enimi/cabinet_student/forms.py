from django import forms

from cabinet_parents.models import Subject, Program, EducationTime, OnlinePlatform, Survey, Region, City, District, \
    TutorArea, StudentArea, Test


class SurveyForm(forms.ModelForm):
    subjects = forms.ModelMultipleChoiceField(
        label='Предметы',
        required=True,
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    programs = forms.ModelMultipleChoiceField(
        label='Программа обучения',
        required=False,
        queryset=Program.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    tests = forms.ModelMultipleChoiceField(
        label='Тесты',
        required=False,
        queryset=Test.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    education_time = forms.ModelChoiceField(
        label='Время для занятий',
        queryset=EducationTime.objects.all(),
        initial='New'
    )
    online = forms.ModelMultipleChoiceField(
        label='Онлайн платформы',
        required=False,
        queryset=OnlinePlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Survey
        fields = ('subjects', 'programs', 'tests', 'education_time', 'min_cost', 'max_cost', 'online')

        widgets = {
            'min_cost': forms.NumberInput(attrs={'step': '500', 'placeholder': 'мин.стоимость - 500'}),
            'max_cost': forms.NumberInput(attrs={'step': '500', 'placeholder': 'макс.стоимость - 500000'}),
        }


class TutorAreaForm(forms.ModelForm):
    tutor_region = forms.ModelChoiceField(
        label='Область',
        required=False,
        empty_label='Выберите область',
        queryset=Region.objects.all().exclude(region='Не указано'),
        initial='New'
    )
    tutor_city = forms.ModelChoiceField(
        label='Город',
        required=False,
        empty_label='Выберите город',
        queryset=City.objects.all().exclude(city='Не указано'),
        initial='New'
    )
    tutor_district = forms.ModelChoiceField(
        label='Район',
        required=False,
        empty_label='Выберите район',
        queryset=District.objects.all().exclude(district='Не указано'),
        initial='New'
    )
    class Meta:
        model = TutorArea
        fields = ('tutor_region', 'tutor_city', 'tutor_district')


class StudentAreaForm(forms.ModelForm):
    student_region = forms.ModelChoiceField(
        label='Область',
        empty_label='Выберите область',
        required=False,
        queryset=Region.objects.all().exclude(region='Не указано'),
        initial='New'
    )
    student_city = forms.ModelChoiceField(
        label='Город',
        empty_label='Выберите область',
        required=False,
        queryset=City.objects.all().exclude(city='Не указано'),
        initial='New'
    )
    student_district = forms.ModelChoiceField(
        label='Район',
        empty_label='Выберите район',
        required=False,
        queryset=District.objects.all().exclude(district='Не указано'),
        initial='New'
    )
    class Meta:
        model = StudentArea
        fields = ('student_region', 'student_city', 'student_district')
