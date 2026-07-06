from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitDestroyAPIView, HabitRetrieveAPIView,
                          HabitsCreateAPIView, HabitsListAPIView,
                          HabitUpdateAPIView, PublicHabitsAPIView)

app_name = HabitsConfig.name


urlpatterns = [
    path("habits/", HabitsListAPIView.as_view(), name="list"),
    path("habits/create/", HabitsCreateAPIView.as_view(), name="create"),
    path("habits/<int:pk>/", HabitRetrieveAPIView.as_view(), name="retrieve"),
    path("habits/<int:pk>/update/", HabitUpdateAPIView.as_view(), name="update"),
    path("habits/<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="delete"),
    path("habits/public_list/", PublicHabitsAPIView.as_view(), name="public_list"),
]
