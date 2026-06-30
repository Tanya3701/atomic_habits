from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import CustomPageNumberPagination
from habits.permissions import IsOwnerOrReadOnly
from habits.serializers import HabitSerializer, PublicHabitSerializer


class HabitsCreateAPIView(CreateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class PublicHabitsAPIView(ListAPIView):
    queryset = Habit.objects.filter(published=True)
    serializer_class = PublicHabitSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPageNumberPagination


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticated,
    )
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        return Habit.objects.filter(owner=self.request.user)


class HabitRetrieveAPIView(RetrieveAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticated,
    )


class HabitUpdateAPIView(UpdateAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwnerOrReadOnly,
    )


class HabitDestroyAPIView(DestroyAPIView):
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = (
        IsOwnerOrReadOnly,
        IsAuthenticated,
    )
