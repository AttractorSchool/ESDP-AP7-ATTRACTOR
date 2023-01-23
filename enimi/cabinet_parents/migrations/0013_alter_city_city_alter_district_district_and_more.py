# Generated by Django 4.1.4 on 2023-01-16 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cabinet_parents", "0012_remove_studentarea_survey"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="city",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Город"
            ),
        ),
        migrations.AlterField(
            model_name="district",
            name="district",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Город"
            ),
        ),
        migrations.AlterField(
            model_name="region",
            name="region",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Область"
            ),
        ),
        migrations.AlterField(
            model_name="studentarea",
            name="student_city",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_areas",
                to="cabinet_parents.city",
                verbose_name="Город",
            ),
        ),
        migrations.AlterField(
            model_name="studentarea",
            name="student_district",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_areas",
                to="cabinet_parents.district",
                verbose_name="Район",
            ),
        ),
        migrations.AlterField(
            model_name="studentarea",
            name="student_region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="student_areas",
                to="cabinet_parents.region",
                verbose_name="Область",
            ),
        ),
        migrations.AlterField(
            model_name="tutorarea",
            name="tutor_city",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutor_areas",
                to="cabinet_parents.city",
                verbose_name="Город",
            ),
        ),
        migrations.AlterField(
            model_name="tutorarea",
            name="tutor_district",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutor_areas",
                to="cabinet_parents.district",
                verbose_name="Район",
            ),
        ),
        migrations.AlterField(
            model_name="tutorarea",
            name="tutor_region",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tutor_areas",
                to="cabinet_parents.region",
                verbose_name="Область",
            ),
        ),
    ]