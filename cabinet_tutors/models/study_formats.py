from django.db import models


class TutorStudyFormats(models.Model):
    online = models.ManyToManyField(
        to='cabinet_parents.OnlinePlatform',
        verbose_name='Онлайн платформы',
        related_name='tutors',
    )
    tutor_area = models.ForeignKey(
        to='cabinet_parents.TutorArea',
        verbose_name='Район занятий у репетитора',
        related_name='tutors',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    student_area = models.ForeignKey(
        to='cabinet_parents.StudentArea',
        verbose_name='Район занятий у ученика',
        related_name='tutors',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    is_active = models.BooleanField(verbose_name='Активный', default=False, null=False)
    is_deleted = models.BooleanField(verbose_name='Удалено', default=False, null=False)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Дата изменения', auto_now=True)
