# Generated by Django 4.2.6 on 2023-11-04 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='telegram_id',
            field=models.CharField(max_length=250, verbose_name='телеграм ID'),
        ),
    ]