from django.db import models


class City(models.Model):
    city = models.CharField(
        verbose_name='Город',
        max_length=100,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    region = models.ForeignKey(
        verbose_name='Области',
        to='cabinet_parents.Region',
        related_name='cities',
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f'{self.city}'
