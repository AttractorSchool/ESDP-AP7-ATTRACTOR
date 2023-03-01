from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Service(models.Model):
    title = models.CharField(
        verbose_name='Название сервиса',
        max_length=200,
        null=True,
        blank=False
    )
    description = models.CharField(
        verbose_name='Описание сервиса',
        max_length=3000,
        null=True,
        blank=False
    )
    price = models.IntegerField(
        verbose_name='Стоимость услуги',
        null=True,
        blank=False,
        validators=[MinValueValidator(0)],
    )
    duration = models.IntegerField(
        verbose_name='Продолжительность услуги',
        null=True,
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(499000)]
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )

    class Meta:
        verbose_name = 'Cервис'
        verbose_name_plural = 'Cервисы'

    def __str__(self):
        return f'{self.title} {self.duration}'