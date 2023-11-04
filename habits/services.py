from telebot import TeleBot
from config import settings


def send_message(habit):
    """Отправка сообщения в ТГ"""
    bot = TeleBot(settings.TELEGRAM_TOKEN)
    reward = ""
    if habit.related_habit:
        reward = (f"\n\n"
                  f"Место: {habit.related_habit.place}\n"
                  f"Действие: {habit.related_habit.action}\n"
                  f"Время действия: {habit.related_habit.time_to_complete}")

    elif habit.award:
        reward = (f"\n\n"
                  f"Твоя награда: {habit.award}")

    text = (f"Привет, {habit.user.email}\n"
            f"Ты ничего не забыл? Например пойти в\n"
            f"Место под названием: {habit.place}\n"
            f"Время: {habit.time}\n"
            f"Это займёт у тебя {habit.time_to_complete} минуту(ы)\n"
            f"Просто сделай это ===> {habit.action}{reward}")

    bot.send_message(habit.user.telegram_id, text)
