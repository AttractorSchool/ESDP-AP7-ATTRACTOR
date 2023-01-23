from time import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from accounts.models import Account


class Review(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='reviews',
                               verbose_name='Автор')
    tutor = models.ForeignKey(to=Account, on_delete=models.CASCADE)
    review_date = models.DateTimeField(verbose_name='Дата добавления', auto_now_add=True)
    text = models.CharField(verbose_name='Отзыв', null=False, blank=False, max_length=1000)
    rate_choices = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.tutor} {self.text} {self.author}'
