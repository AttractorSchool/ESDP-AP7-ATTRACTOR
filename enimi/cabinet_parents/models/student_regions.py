from django.db import models


class StudentRegion(models.Model):
    region = models.ForeignKey(
        to='cabinet_parents.Region',
        verbose_name='Область',
        related_name='student_regions',
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        to='cabinet_parents.City',
        verbose_name='Город',
        related_name='student_regions',
        on_delete=models.CASCADE
    )
    district = models.ForeignKey(
        to='cabinet_parents.District',
        verbose_name='Район',
        related_name='student_regions',
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
        return f'{self.region} {self.city} {self.district}'
