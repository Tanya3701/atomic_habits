from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_reminder_in_telegram():
    """Периодическая задача отправки уведомлений в telegram за минуту до назначенного времени"""
    habits = Habit.objects.all()
    for habit in habits:
        if habit.owner.chat_id:
            message = f"Я должен {habit.action} в {habit.time} в {habit.point} в течение {habit.time_to_complete}"
            send_telegram_message(message, habit.owner.chat_id)
