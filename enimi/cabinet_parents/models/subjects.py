from django.db import models

class Subject(models.Model):
    subject = models.CharField(
        verbose_name='Предмет',
        max_length=100,
        null=True,
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
        return f'{self.subject}'
