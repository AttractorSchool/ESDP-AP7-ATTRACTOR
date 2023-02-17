from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import UserManager


class UserCategoryChoices(TextChoices):
    # STUDY_CENTER = 'study_center', 'Учебный центр'
    STUDENT = 'student', 'Ученик'
    TUTOR = 'tutor', 'Репетитор'
    PARENTS = 'parents', 'Родители'


class Account(AbstractUser):
    type = models.CharField(
        verbose_name='Тип пользователя',
        choices=UserCategoryChoices.choices,
        max_length=200,
        null=False,
        blank=False,
    )
    father_name = models.CharField(
        verbose_name='Отчество',
        max_length=200,
        null=True,
        blank=True
    )
    email = models.EmailField(
        verbose_name='Электронная почта',
        unique=True,
        blank=False
    )
    phone = PhoneNumberField(
        null=False,
        blank=False
    )
    avatar = models.ImageField(
        null=False,
        blank=True,
        upload_to='avatars',
        verbose_name='Аватар',
        default='default_avatar/default-user.png'
    )
    birthday = models.CharField(verbose_name='Дата рождения',null=True, blank=True, max_length=30)
    parent = models.ForeignKey('accounts.Account',
                               verbose_name=('Родитель'),
                               on_delete=models.CASCADE,
                               related_name='children',
                               null=True)
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )
    changed_at = models.DateTimeField(
        verbose_name='Дата изменения',
        auto_now=True
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        default=False,
        null=False
    )
    with_survey = models.BooleanField(
        verbose_name='Анкета есть',
        default=False,
        null=False
    )
    with_email = models.BooleanField(
        verbose_name='Email есть',
        default=True,
        null=False
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
