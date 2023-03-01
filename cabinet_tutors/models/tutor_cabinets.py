from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import TextChoices


class GenderChoices(TextChoices):
    MALE = 'male', 'муж.'
    FEMALE = 'female', 'жен.'


class Languages(models.Model):
    name = models.CharField(verbose_name="Язык", null=False, blank=False, max_length=100)

    def __str__(self):
        return f'{self.name}'


class TutorCabinets(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to=get_user_model(),
        related_name='tutor',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    gender = models.CharField(
        choices=GenderChoices.choices,
        default=None,
        verbose_name='Пол',
        null=True,
        blank=True,
        max_length=150
    )
    languages = models.ManyToManyField(
        to='cabinet_tutors.Languages',
        related_name='tutors',
        verbose_name='Язык преподавания',
        blank=True,
    )
    about = models.TextField(verbose_name='Коротко о себе', null=True, blank=True, max_length=1000)
    education = models.ManyToManyField(
        verbose_name='Образование и дипломы',
        to='cabinet_tutors.Education',
        related_name='tutors',
    )
    subjects_and_costs = models.ManyToManyField(
        verbose_name='Предметы и стоимость',
        to='cabinet_tutors.SubjectsAndCosts',
        related_name='tutors',
    )
    study_formats = models.ForeignKey(
        to='cabinet_tutors.TutorStudyFormats',
        verbose_name='Формат обучения',
        related_name='tutors',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'Репетитор: {self.user}'
