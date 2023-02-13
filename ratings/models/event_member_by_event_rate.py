from django.db import models
from django.db.models import TextChoices

from calendarapp.models import Event, EventMember

class RateChoices(TextChoices):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    # NOT_RATE = 'not rate'

class MemberEventRating(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE,
        verbose_name='Занятие',
        null=False, blank=True,
        related_name="ratings"
    )
    event_member = models.ForeignKey(
        EventMember, on_delete=models.CASCADE,
        verbose_name='Ученик',
        null=False, blank=True,
        related_name="ratings"
    )
    score = models.SmallIntegerField(
        verbose_name='Оценка',
        null=True, blank=False
    )
    comment = models.TextField(
        null=False, blank=True,
        verbose_name='Комментарий',
        default='Нет комментария'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

    def __str__(self):
        return f'{self.event} {self.event_member} {self.score} {self.comment}'