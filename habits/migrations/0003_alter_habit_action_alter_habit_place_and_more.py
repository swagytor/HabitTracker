# Generated by Django 4.2.6 on 2023-11-04 18:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='action',
            field=models.CharField(max_length=60, verbose_name='Действие'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='place',
            field=models.CharField(max_length=30, verbose_name='Место'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='habit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
