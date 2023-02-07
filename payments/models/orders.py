from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import TextChoices


class OrderStatusChoices(TextChoices):
    NOT_PAID = 'Not paid', 'Заказ не оплачен'
    REJECTED = 'Rejected', 'Заказ отклонён'
    PAID = 'Paid', 'Заказ оплачен'


class Order(models.Model):
    email = models.EmailField(
        verbose_name='Электронная почта',
        blank=False
    )
    amount = models.CharField(
        verbose_name='Сумма',
        null=True,
        blank=False,
        max_length=30,
        validators=[MinValueValidator(0)],
    )
    description = models.CharField(
        verbose_name='Описание услуги',
        null=True,
        blank=False,
        max_length=3000
    )
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    status = models.CharField(
        verbose_name='Статус услуги',
        choices=OrderStatusChoices.choices,
        max_length=200,
        null=False,
        default=OrderStatusChoices.NOT_PAID
    )
    service = models.ForeignKey(
        to='payments.Service',
        verbose_name='Пользователь сервиса',
        related_name='orders',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        to='accounts.Account',
        verbose_name='Пользователь сервиса',
        related_name='orders',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.amount} {self.status} {self.service} {self.user}'