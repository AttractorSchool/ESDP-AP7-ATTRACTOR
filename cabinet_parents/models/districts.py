from django.db import models


class District(models.Model):
    district = models.CharField(
        verbose_name='Город',
        max_length=100,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    def __str__(self):
        return f'{self.district}'
