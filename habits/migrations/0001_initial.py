
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=30, verbose_name='место')),
                ('time', models.TimeField(verbose_name='время')),
                ('action', models.CharField(max_length=60, verbose_name='действие')),
                ('pleasant_habit', models.BooleanField(verbose_name='приятная привычка')),
                ('frequency', models.IntegerField(default=1, verbose_name='периодичность')),
                ('award', models.CharField(blank=True, max_length=200, null=True, verbose_name='вознаграждение')),
                ('time_to_complete', models.TimeField(verbose_name='время на выполнение')),
                ('public', models.BooleanField(default=True, verbose_name='публичная')),
                ('last_execution', models.DateField(blank=True, null=True, verbose_name='последнее выполнение')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='связанная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]
