from django.db import models


class TutorArea(models.Model):
    tutor_region = models.ForeignKey(
        to='cabinet_parents.Region',
        verbose_name='Область',
        related_name='tutor_areas',
        null=True,
        on_delete=models.CASCADE
    )
    tutor_city = models.ForeignKey(
        to='cabinet_parents.City',
        verbose_name='Город',
        related_name='tutor_areas',
        null=True,
        on_delete=models.CASCADE
    )
    tutor_district = models.ForeignKey(
        to='cabinet_parents.District',
        verbose_name='Район',
        related_name='tutor_areas',
        null=True,
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
        return f'{self.tutor_region} {self.tutor_district} {self.tutor_city}'

