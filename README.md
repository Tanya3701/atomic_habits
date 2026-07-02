# Приложение для отправки уведомлений в telegram


## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/username/project-x.git
```
2. Установите зависимости:
```
pip install -r requirements.txt
```


### Содержание:

* Приложение Привычки

_________________________________

- Содержание моделей

`class Habit(models.Model)`
* `owner` - Автор
* `point` - Место
* `time` - Время
* `action` - Действие
* `nice_habit` - Приятная привычка
* `tied_habit` - Связанная привычка
* `time_to_complete` - Время на выполнение
* `periodicity` - Периодичность
* `award` - Вознаграждение
* `published` - Публичность

* * Вывод списка привычек текущего пользователя - `class HabitsListAPIView(ListAPIView)`
* * Возможность создать привычку - `class HabitsCreateAPIView(CreateAPIView)`
* * Возможность просматривать (пользователь должен быть автором записи) - `class HabitRetrieveAPIView(RetrieveAPIView)`
* * Возможность редактировать (пользователь должен быть автором записи) - `class HabitUpdateAPIView(UpdateAPIView)`
* * Возможность удалять (пользователь должен быть автором записи) - `HabitDestroyAPIView(DestroyAPIView)`
* * Вывод списка всех привычек с разрешенной публикацией - `class PublicHabitsAPIView(ListAPIView)`










