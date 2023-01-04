from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Survey(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to='accounts.Account',
        related_name='survey',
        on_delete=models.CASCADE
    )
    subjects = models.ManyToManyField(
        to='cabinet_parents.Subject',
        verbose_name='Предметы',
        related_name='surveys',
    )
    programs = models.ManyToManyField(
        to='cabinet_parents.Program',
        verbose_name='Программа обучения',
        related_name='surveys',
    )
    tests = models.ManyToManyField(
        to='cabinet_parents.Test',
        verbose_name='Программа тестов',
        related_name='surveys',
    )
    education_time = models.ForeignKey(
        to='cabinet_parents.EducationTime',
        verbose_name='Время для обучения',
        related_name='surveys',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    min_cost = models.IntegerField(
        verbose_name='Минимальная стоимость тг./час',
        null=True,
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(499000)]

    )
    max_cost = models.IntegerField(
        verbose_name='Максимальная стоимость тг./час',
        null=True,
        blank=False,
        validators=[MinValueValidator(1), MaxValueValidator(500000)]
    )
    online = models.ManyToManyField(
        to='cabinet_parents.OnlinePlatform',
        verbose_name='Онлайн платформы',
        related_name='surveys',
    )
    tutor_area = models.ForeignKey(
        to='cabinet_parents.TutorArea',
        verbose_name='Район занятий у репетитора',
        related_name='surveys',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    student_area = models.ForeignKey(
        to='cabinet_parents.StudentArea',
        verbose_name='Район занятий у ученика',
        related_name='surveys',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(verbose_name='Активный', default=False, null=False)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
