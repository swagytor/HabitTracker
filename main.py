from telebot import TeleBot

from config import settings

bot = TeleBot(settings.TELEGRAM_TOKEN)
if __name__ == '__main__':
    bot.send_message(settings.TELEGRAM_ID, "привет!")
