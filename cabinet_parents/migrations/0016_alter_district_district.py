# Generated by Django 4.1.6 on 2023-02-08 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabinet_parents', '0015_alter_city_city_alter_district_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='district',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Район'),
        ),
    ]
