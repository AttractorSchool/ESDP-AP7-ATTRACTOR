# Generated by Django 4.1.4 on 2022-12-28 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_tutors', '0003_alter_tutormodule_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutormodule',
            name='education',
            field=models.ManyToManyField(related_name='tutors', to='cabinet_tutors.education', verbose_name='Образование и дипломы'),
        ),
        migrations.AlterField(
            model_name='tutormodule',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='tutors', to='cabinet_tutors.language', verbose_name='Язык преподавания'),
        ),
        migrations.AlterField(
            model_name='tutormodule',
            name='study_formats',
            field=models.ManyToManyField(related_name='tutors', to='cabinet_tutors.studyformats', verbose_name='Формат обучения'),
        ),
        migrations.AlterField(
            model_name='tutormodule',
            name='subjects_and_costs',
            field=models.ManyToManyField(related_name='tutors', to='cabinet_tutors.subjectsandcosts', verbose_name='Предметы и стоимость'),
        ),
    ]