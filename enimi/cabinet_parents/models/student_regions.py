from django.db import models


class StudentArea(models.Model):
    survey = models.ForeignKey(
        verbose_name='Анкета',
        to='cabinet_parents.Survey',
        related_name='student_areas',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    student_region = models.ForeignKey(
        to='cabinet_parents.Region',
        verbose_name='Область',
        related_name='student_areas',
        on_delete=models.CASCADE
    )
    student_city = models.ForeignKey(
        to='cabinet_parents.City',
        verbose_name='Город',
        related_name='student_areas',
        on_delete=models.CASCADE
    )
    student_district = models.ForeignKey(
        to='cabinet_parents.District',
        verbose_name='Район',
        related_name='student_areas',
        on_delete=models.CASCADE
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
        return f'{self.student_region} {self.student_city} {self.student_district}'
