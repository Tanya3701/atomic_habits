from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPageNumberPagination
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer, PublicHabitSerializer


class HabitsCreateAPIView(CreateAPIView):
    """Класс создания модели привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Присваивание статуса Автор для создателя привычки"""
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class PublicHabitsAPIView(ListAPIView):
    """Вывод списка привычек с разрешенной публикацией"""

    queryset = Habit.objects.filter(published=True)
    serializer_class = PublicHabitSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumberPagination


class HabitsListAPIView(ListAPIView):
    """Вывод списка привычек текущего пользователя"""

    serializer_class = HabitSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticated,
    )
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        """Фильтр привычек для текущего пользователя"""
        return Habit.objects.filter(owner=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    """Класс просмотра одной привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticated,
    )


class HabitUpdateAPIView(UpdateAPIView):
    """Класс редактирования одной привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )


class HabitDestroyAPIView(DestroyAPIView):
    """Класс удаления привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticated,
    )
