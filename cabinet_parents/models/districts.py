from django.db import models

import cabinet_parents.models


class District(models.Model):
    district = models.CharField(
        verbose_name='Район',
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
    city = models.ForeignKey(
        verbose_name='Города',
        to='cabinet_parents.City',
        related_name='districts',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f'{self.district}'
