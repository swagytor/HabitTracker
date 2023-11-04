from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """Модель привычек"""

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=30, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=60, verbose_name='Действие')
    pleasant_habit = models.BooleanField(verbose_name='Приятная привычка')
    related_habit = models.ForeignKey("self", verbose_name='Связанная привычка', on_delete=models.SET_NULL, **NULLABLE)
    frequency = models.IntegerField(default=1, verbose_name='Периодичность')
    award = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    time_to_complete = models.TimeField(verbose_name='Время на выполнение')
    public = models.BooleanField(default=True, verbose_name='Публичная')

    last_execution = models.DateField(verbose_name='Последнее выполнение', **NULLABLE)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'

    def __str__(self):
        return f'{self.action} {self.place}'
