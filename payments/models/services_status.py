from django.db import models
from django.db.models import TextChoices


class ServiceStatusChoices(TextChoices):
    ACTIVE = '1'
    NOT_ACTIVE = '0'


class ServiceStatus(models.Model):
    user = models.ForeignKey(
        to='accounts.Account',
        verbose_name='Пользователь сервиса',
        related_name='services',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        to='payments.Service',
        verbose_name='Услуга',
        related_name='services',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    start_date = models.CharField(
        verbose_name='Дата начала',
        null=True,
        blank=False,
        max_length=30
    )
    end_date = models.CharField(
        verbose_name='Дата окончания',
        null=True,
        blank=False,
        max_length=30
    )
    status = models.CharField(
        verbose_name='Статус услуги',
        choices=ServiceStatusChoices.choices,
        max_length=200,
        null=False,
        default=ServiceStatusChoices.NOT_ACTIVE
    )
    order = models.ForeignKey(
        to='payments.Order',
        verbose_name='Заказ',
        related_name='services',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Статус сервиса'
        verbose_name_plural = 'Статус сервисов'

    def __str__(self):
        return f'{self.user} {self.service} {self.status}'