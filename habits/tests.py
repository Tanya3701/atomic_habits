from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            point="Тест",
            owner=self.user,
            time="00:00:00",
            periodicity=1,
            published=True,
            action="Протестировать тесты",
        )

    def test_habit_retrieve(self):
        url = reverse("habits:retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habit_create(self):
        url = reverse("habits:create")
        data = {
            "point": "Тест2",
            "time": "01:01:01",
            "periodicity": 2,
            "published": True,
            "action": "Протестировать тесты2",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_habit_update(self):
        url = reverse("habits:update", args=(self.habit.pk,))
        data = {"point": "Тест3"}
        self.client.patch(url, data=data)
        self.assertEqual(data.get("point"), "Тест3")

    def test_habit_delete(self):
        url = reverse("habits:delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_habit_public_list(self):
        url = reverse("habits:public_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.count(), 1)

    def test_habit_list(self):
        url = reverse("habits:list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habit.objects.count(), 1)
