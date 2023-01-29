from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class SubjectsAndCosts(models.Model):
    subject = models.ForeignKey(
        to='cabinet_parents.Subject',
        verbose_name='Предмет',
        related_name='tutors',
        on_delete=models.CASCADE
    )
    cost = models.IntegerField(
        verbose_name='Cтоимость тг./час',
        null=True,
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(499000)]
    )
    experience = models.DecimalField(null=False,
                                     blank=False,
                                     max_digits=3,
                                     decimal_places=1,
                                     verbose_name='Опыт преподавания')

    class Meta:
        ordering = ['id']
