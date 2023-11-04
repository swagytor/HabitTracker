from datetime import datetime, timedelta

from celery import shared_task

from habits.models import Habit
from habits.services import send_message


@shared_task
def check_time_habits():
    """Проверка срабатывает каждую минуту, сравнивает текущее время со временем выполнения привычки
     и отправляет уведомление в Телеграме"""
    datetime_now = datetime.now()
    time_now = datetime_now.strftime("%H:%M:00")

    habit_queryset = Habit.objects.filter(time=time_now)

    for habit in habit_queryset:
        if habit.last_execution:
            time_send = habit.last_execution + timedelta(days=habit.frequency)
            if time_send == datetime_now.date():
                send_message(habit)
                habit.last_execution = datetime_now.date()
                habit.save()
        else:
            send_message(habit)
            habit.last_execution = datetime_now.date()
            habit.save()
