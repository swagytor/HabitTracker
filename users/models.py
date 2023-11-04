from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='Почта', unique=True)

    number = models.CharField(max_length=25, verbose_name='Номер телефона')
    telegram_id = models.CharField(max_length=250, verbose_name='Телеграм ID')
    city = models.CharField(max_length=50, verbose_name='Город')
    token = models.CharField(max_length=250, verbose_name='Токен')
    token_created = models.DateTimeField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} {self.telegram_id}"

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
