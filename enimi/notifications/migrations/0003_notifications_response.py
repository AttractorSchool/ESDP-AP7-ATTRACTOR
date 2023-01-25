# Generated by Django 4.1.5 on 2023-01-24 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('responses', '0002_response_cabinet_tutor_alter_response_survey'),
        ('notifications', '0002_remove_notifications_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_response', to='responses.response', verbose_name='Отклик'),
        ),
    ]