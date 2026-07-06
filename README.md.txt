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

