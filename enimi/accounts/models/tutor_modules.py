from django.db import models


class TutorModule(models.Model):
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to='accounts.Account',
        related_name='tutor_module',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    place_of_study = models.CharField(
        verbose_name='Место учёбы',
        max_length=200,
        null=True,
        blank=True
    )
    working_place = models.CharField(
        verbose_name='Место работы',
        max_length=200,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)

    def __str__(self):
        return f'{self.user}'
