from datetime import timedelta

from django.db import models
from rest_framework.exceptions import ValidationError

from users.models import User


class Habit(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Автор",
        help_text="Укажите автора",
    )
    point = models.CharField(
        max_length=100, verbose_name="Место", help_text="Укажите место"
    )
    time = models.TimeField(verbose_name="Время", help_text="Укажите время")
    action = models.CharField(
        max_length=500, verbose_name="Действие", help_text="Укажите действие"
    )
    nice_habit = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        verbose_name="Признак приятности",
        help_text="Укажите признак приятности",
    )
    tied_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Связанная привычка",
        help_text="Укажите связанную привычку",
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        verbose_name="Периодичность",
        help_text="Укажите периодичность",
    )
    award = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
    )
    time_to_complete = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        default=120,
        verbose_name="Время на выполнение в секундах",
        help_text="Укажите время на выполнение в секундах",
    )
    published = models.BooleanField(
        default=True,
        verbose_name="Признак публичности",
        help_text="Укажите признак публичности",
    )

    def clean(self):
        if self.award and self.tied_habit:
            raise ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку"
            )

        if self.nice_habit and (self.award or self.tied_habit):
            raise ValidationError(
                "У приятной привычки не может быть связанной привычки или вознаграждения"
            )

        if self.tied_habit and not self.tied_habit.nice_habit:
            raise ValidationError(
                "Только приятная привычка может быть связанной привычкой"
            )

        if self.time_to_complete > 120:
            raise ValidationError("Время на выполнение не должно превышать 120 секунд")

        if not (1 < self.periodicity < 7):
            raise ValidationError(
                "Полезная привычка должна выполняться не реже 1 раза в неделю"
            )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.point}"
