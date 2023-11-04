from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

import habits.services
import main
from config import settings
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(email='swagytor@yandex,ru',
                                        telegram_id=settings.TELEGRAM_ID,
                                        number='8-800-555-35-35')
        self.user.set_password('12345')
        self.user.save()

        self.habit = Habit.objects.create(
            place='На улице',
            time='14:20:00',
            action='Потрогать траву',
            pleasant_habit=False,
            frequency=1,
            time_to_complete='00:10:00',
            award='Кислород',
            user=self.user
        )

        self.habit_data = {
            "place": "Дома",
            "time": "12:20:00",
            "action": "попить воды",
            "pleasant_habit": False,
            "frequency": 1,
            "time_to_complete": "00:02:00",
            "award": "конфетка"
        }

        self.client.force_authenticate(user=self.user)

    def test_unauthenticated_access(self):
        self.client.force_authenticate()

        response = self.client.post(reverse('habit:habit-list'), data=self.habit_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('habit:habit-list'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('habit:publish_list'))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.get(reverse('habit:habit-detail', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.put(reverse('habit:habit-detail', args=[self.habit.pk]), data=self.habit_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(reverse('habit:habit-detail', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_habit_create(self):
        response = self.client.post(reverse('habit:habit-list'), data=self.habit_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_list(self):
        response = self.client.get(reverse('habit:habit-list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "place": "На улице",
                    "time": "14:20:00",
                    "action": "Потрогать траву",
                    "pleasant_habit": False,
                    "related_habit": None,
                    "frequency": 1,
                    "award": "Кислород",
                    "time_to_complete": "00:10:00",
                    "public": True
                }
            ]
        )

    def test_habit_update(self):
        put_data = {
            "place": "У бабули",
            "time": "18:00:00",
            "action": "полоть клубнику",
            "pleasant_habit": False,
            "frequency": 1,
            "time_to_complete": "00:02:00",
            "award": "Поесть клубнику"
        }

        response = self.client.put(reverse('habit:habit-detail', args=[self.habit.pk]), data=put_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {
                "place": "У бабули",
                "time": "18:00:00",
                "action": "полоть клубнику",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "time_to_complete": "00:02:00",
                "award": "Поесть клубнику",
                "public": False
            }
        )

    def test_habit_detail(self):
        response = self.client.get(reverse('habit:habit-detail', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {
                "place": "На улице",
                "time": "14:20:00",
                "action": "Потрогать траву",
                "pleasant_habit": False,
                "related_habit": None,
                "frequency": 1,
                "award": "Кислород",
                "time_to_complete": "00:10:00",
                "public": True
            }
        )

    def test_habit_delete(self):
        response = self.client.delete(reverse('habit:habit-detail', args=[self.habit.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_public_habit_list(self):
        response = self.client.get(reverse('habit:publish_list'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [
                {
                    "place": "На улице",
                    "time": "14:20:00",
                    "action": "Потрогать траву",
                    "pleasant_habit": False,
                    "related_habit": None,
                    "frequency": 1,
                    "award": "Кислород",
                    "time_to_complete": "00:10:00",
                    "public": True
                }
            ]
        )


class TelegramTestCase(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = User.objects.create(email='swagytor@yandex,ru',
                                        telegram_id=settings.TELEGRAM_ID,
                                        number='8-800-555-35-35')
        self.user.set_password('12345')
        self.user.save()

        self.habit = Habit.objects.create(
            place='На улице',
            time='14:20:00',
            action='Потрогать траву',
            pleasant_habit=False,
            frequency=1,
            time_to_complete='00:10:00',
            award='Кислород',
            user=self.user
        )

    def test_send_test_message(self):
        main.bot.send_message(settings.TELEGRAM_ID, 'Test!')

    def test_send_habit(self):
        habits.services.send_message(self.habit)
