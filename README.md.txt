# Приложение для создания базы данных 


## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/Tanya3701/atomic_habits.git
```
* cd drf-project

* python -m venv venv

* source venv/bin/activate

* pip install -r requirements.txt

* cp .env.sample .env
  (заполните переменные)

* python manage.py migrate

* python manage.py runserver

### Production-развертывание

#### На сервере выполните:

* sudo apt update && sudo apt install docker.io

* sudo systemctl enable docker

* mkdir -p ~/drf-project

* Скопируйте .env в ~/drf-project/.env

CI/CD Pipeline

Автоматически при push, pull_request:

* Собирает Docker-образ
* Пушит в Docker Hub
* Разворачивает на сервере через SSH

Необходимые Secrets:

* DOCKER_HUB_USERNAME
* DOCKER_HUB_TOKEN
* SSH_KEY
* SERVER_IP
## Содержание:
### Главная страница
#### Функционал:

class HH(BaseHH, ABC):

"""Класс для работы с платформой hh.ru"""
* _BaseHH__api_connection(self, endpoint: str)

"""Метод для соединения с API и фильтра данных по ключевому слову"""
* _BaseHH__getting_vacancies(self)

"""Метод получения списка вакансий"""
* class CreateDB:

"""Класс для создания БД и подключения к ней"""
* create_db(self):

"""Метод подключения к БД"""
* class CreateTable(CreateDB):

"""Класс для создания и заполнения таблиц БД"""
*  create_table_companies(self, data_table_c: list[dict[str, Any]])

Метод создания и заполнения таблицы companies
* create_table_vacancies(self, data_table_v: list[dict[str, Any]])

"""Метод создания и заполнения таблицы vacancies"""
* class DBManager(CreateTable):

"""Класс для создания запросов"""
*  get_companies_and_vacancies_count(self):

"""Получает список всех компаний и количество вакансий у каждой компании."""
*  get_all_vacancies(self):

"""Получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию."""
* get_avg_salary(self):

"""Получает среднюю зарплату по вакансиям."""
* get_vacancies_with_higher_salary(self):

"""Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
*  get_vacancies_with_keyword(self, keyword: str):

"""Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python."""
* list_of_actions():

"""Функция печати списка действий"""
*  user_interaction():

"""Функция взаимодействия с пользователем"""
*  id_company():

"""Выводит список id компаний"""
* select_for_id:

"""Отбирает компании по определенным id"""
* del_salary_none(data_vac: list[dict[str, Any]]) -> list[dict[str, Any]]:

"""Заменяет значения NONE на 0"""
*  main():

"""Главная функция, запускает все функциональности"""