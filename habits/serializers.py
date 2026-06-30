from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from habits.models import Habit


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        nice_habit = data.get("nice_habit", False)
        tied_habit = data.get("tied_habit")
        periodicity = data.get("periodicity", 1)
        award = data.get("award", "")
        time_to_complete = data.get("time_to_complete", 120)

        if award and tied_habit:
            raise ValidationError(
                "Нельзя одновременно указывать вознаграждение и связанную привычку"
            )

        if nice_habit and (award or tied_habit):
            raise ValidationError(
                "У приятной привычки не может быть связанной привычки или вознаграждения"
            )

        if tied_habit and not tied_habit.nice_habit:
            raise ValidationError(
                "Только приятная привычка может быть связанной привычкой"
            )

        if time_to_complete > 120:
            raise ValidationError("Время на выполнение не должно превышать 120 секунд")

        if not (1 < periodicity < 7):
            raise ValidationError(
                "Полезная привычка должна выполняться не реже 1 раза в неделю"
            )

        return data


class PublicHabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
