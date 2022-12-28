from django.db import models


class Education(models.Model):
    institution = models.CharField(verbose_name='Учебное заведение', blank=True, null=True, max_length=200)
    speciality = models.CharField(verbose_name='Специальность', blank=True, null=True, max_length=200)
    degree = models.CharField(verbose_name='Полученная степень', blank=True, null=True, max_length=200)
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.institution}, {self.speciality}, {self.degree}'
