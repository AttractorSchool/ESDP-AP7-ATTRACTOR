from django.db import models


class Chat(models.Model):
    author = models.ForeignKey(verbose_name='Автор сообщения', to='accounts.Account', related_name='chats', null=False,
                               blank=False,
                               on_delete=models.CASCADE)
    message = models.TextField(verbose_name='Сообщение', null=False, blank=True, max_length=3000)
    response = models.ForeignKey(verbose_name='Отклик', to='responses.Response', related_name='chats', null=False,
                               blank=False, on_delete=models.CASCADE)
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False, null=False
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )

    class Meta:
        ordering = ('created_at',)
