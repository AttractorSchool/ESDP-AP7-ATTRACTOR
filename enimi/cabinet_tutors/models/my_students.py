from django.db import models


class MyStudent(models.Model):
    student = models.ForeignKey(
        to='accounts.Account',
        verbose_name='Студент',
        related_name='students',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    tutor = models.ForeignKey(
        to='accounts.Account',
        verbose_name='Репетитор',
        related_name='tutors',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Студент: {self.student}'
