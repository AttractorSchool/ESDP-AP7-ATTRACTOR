from django.db import models
from django.db.models import TextChoices


class TypeChoices(TextChoices):
    RESPONSE = 'response', 'Отклик'
    CHAT = 'chat', 'Чат'
    REGISTRATION = 'registration', 'Регистрация'
    ADDING_STUDENT = 'adding_student', 'Добавление ученика'


class Notifications(models.Model):
    to_whom = models.ForeignKey(
        verbose_name='Кому',
        to='accounts.Account',
        related_name='notifications',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    type = models.CharField(
        choices=TypeChoices.choices,
        verbose_name='Пол',
        null=False,
        blank=False,
        max_length=200
    )
    message = models.CharField(
        verbose_name='Уведомление',
        null=False,
        blank=False,
        max_length=500
    )
    from_whom = models.ForeignKey(
        verbose_name='От кого',
        to='accounts.Account',
        related_name='notifications_from',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    response = models.ForeignKey(
        verbose_name='Отклик',
        to='responses.Response',
        related_name='notification_response',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    viewed = models.BooleanField(
        verbose_name='Просмотрено',
        default=False,
        null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
