from django.contrib.auth import get_user_model
from django.db import models


class Response(models.Model):
    author = models.ForeignKey(verbose_name='Автор отклика', to='accounts.Account', related_name='responses',
                               null=False, blank=False, on_delete=models.CASCADE)
    hello_message = models.TextField(verbose_name='Приветственное сообщение', null=False, blank=True, max_length=3000,
                                     default='Здравствуйте. Меня заинтересовала ваша анкета!')
    subjects = models.ManyToManyField(
        to='cabinet_parents.Subject',
        verbose_name='Предметы',
        related_name='responses',
    )

    survey = models.ForeignKey(
        to='cabinet_parents.Survey',
        verbose_name='Анкета студента',
        related_name='responses',
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    cabinet_tutor = models.ForeignKey(
        to='cabinet_tutors.TutorCabinets',
        verbose_name='Анкета репетитора',
        related_name='responses',
        null=True,
        blank=False,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
