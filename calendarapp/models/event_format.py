from django.db import models
class EventFormat(models.Model):
    format_name = models.CharField(
        verbose_name='Текст задачи',
        max_length=200,
        null=False,
        blank=False
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
        return f'{self.format_name}'