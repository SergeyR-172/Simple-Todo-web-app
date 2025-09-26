# SimpleTodo - Приложение для управления задачами

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/django-5.2.6-green)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/django_rest_framework-3.16.1-red)](https://www.django-rest-framework.org/)
[![Docker](https://img.shields.io/badge/docker-20.10%2B-blue)](https://www.docker.com/)
[![PostgreSQL](https://img.shields.io/badge/postgresql-17.6-blue)](https://www.postgresql.org/)

SimpleTodo - это простое и интуитивно понятное приложение для управления задачами, построенное на Django и Django REST Framework. Оно предоставляет API для создания, просмотра, обновления и удаления задач. Для визуализации и тестирования API описан небольшой фронтенд.

## 🌟 Особенности

- ✅ Создание, чтение, обновление и удаление задач (CRUD)
- 🔍 Фильтрация задач по статусу выполнения
- 📱 RESTful API для интеграции с фронтендом
- 📚 Документация API с помощью drf-spectacular
- 🔌 Поддержка CORS для интеграции с фронтендом
- ⚙️ Конфигурация через переменные окружения
- 🗃️ Поддержка PostgreSQL и SQLite баз данных
- 🐳 Поддержка Docker и Docker Compose для упрощенного развертывания

## 🏗️ Архитектура проекта

```
SimpleTodo/
├── backend/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── todo_project/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── todo_app/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       └── migrations/
├── frontend/
│   ├── Dockerfile
│   ├── index.html
│   ├── config.js
│   └── nginx.conf
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

### Архитектура Docker

Проект использует микросервисную архитектуру с тремя контейнерами:

1. **frontend** - Nginx Alpine сервер для статических файлов фронтенда
2. **backend** - Django 5.2.6 приложение с REST API
3. **db** - PostgreSQL 17.6 база данных

Контейнеры связаны через docker-compose с общей сетью и томом для базы данных.

## 🚀 Начало работы

### Вариант 1: Запуск с помощью Docker (рекомендуется)

1. Убедитесь, что Docker и Docker Compose установлены
2. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SergeyR-172/Django-Simple-Todo-web-app.git
   cd Django-Simple-Todo-web-app
   ```
3. Запустите приложение:
   ```bash
   docker-compose up --build
   ```
4. Приложение будет доступно по адресам:
   - Фронтенд: http://localhost:3000
   - Backend API: http://localhost:8000/api/tasks
   - Документация API: http://localhost:8000/api/docs/

### Вариант 2: Запуск без Docker

#### Предварительные требования

- Python 3.13
- pip (менеджер пакетов Python)
- virtualenv (рекомендуется)
- PostgreSQL (опционально, для production)

#### Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/SergeyR-172/Django-Simple-Todo-web-app.git
   cd Django-Simple-Todo-web-app
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv .venv
   source .venv/scripts/activate  # На Windows: .venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. Перейдите в директорию backend:
   ```bash
   cd backend
   ```

5. Создайте файл .env на основе .env.example:
   ```bash
   cp .env.example .env
   ```
   Отредактируйте .env файл, указав ваши настройки базы данных и секретный ключ.

6. Примените миграции:
   ```bash
   python manage.py migrate
   ```
   
7. Запустите сервер разработки:
   ```bash
   python manage.py runserver
   ```

## ⚙️ Конфигурация

Приложение использует переменные окружения для конфигурации. Создайте файл `.env` в корневой директории `backend` со следующими переменными:

```env
# Секретный ключ Django
VERY_SECRET_KEY=ваш_секретный_ключ

# Режим отладки (1 для включения, 0 для выключения)
DEBUG=1

# URL фронтенда для CORS
FRONTEND_URL=http://localhost:3000

# Настройки базы данных PostgreSQL
DB_ENGINE=django.db.backends.postgresql
DB_NAME=название_базы
DB_USER=пользователь
DB_PASSWORD=пароль
DB_HOST=localhost
DB_PORT=5432
```

Для локального тестирования можно использовать SQLite, установив:
```env
DB_ENGINE=django.db.backends.sqlite3
```

## 📡 API Endpoints

После запуска сервера API будет доступен по адресу: `http://127.0.0.1:8000/api/`

| Метод | Endpoint | Описание |
|-------|----------|----------|
| GET | `/tasks/` | Получить список всех задач |
| POST | `/tasks/` | Создать новую задачу |
| GET | `/tasks/{id}/` | Получить конкретную задачу |
| PUT | `/tasks/{id}/` | Полное обновление задачи |
| PATCH | `/tasks/{id}/` | Частичное обновление задачи |
| DELETE | `/tasks/{id}/` | Удалить задачу |

### Фильтрация

Вы можете фильтровать задачи по статусу выполнения:
- `/tasks/?completed=true` - только выполненные задачи
- `/tasks/?completed=false` - только невыполненные задачи

## 📖 Примеры использования API

### Создание задачи
```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"content": "Новая задача"}'
```

### Получение всех задач
```bash
curl http://127.0.0.1:8000/api/tasks/
```

### Обновление статуса задачи
```bash
curl -X PATCH http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

## 🛠️ Технологии

- [Python 3.13](https://www.python.org/) - Язык программирования
- [Django 5.2.6](https://www.djangoproject.com/) - Веб-фреймворк
- [Django REST Framework 3.16.1](https://www.django-rest-framework.org/) - Инструмент для создания REST API
- [drf-spectacular 0.28.0](https://github.com/tfranzel/drf-spectacular) - Генерация документации API
- [django-cors-headers 4.9.0](https://github.com/adamchainz/django-cors-headers) - Поддержка CORS
- [Docker](https://www.docker.com/) - Контейнеризация приложения
- [PostgreSQL 17.6](https://www.postgresql.org/) - База данных
- [Nginx Alpine](https://nginx.org/) - Веб-сервер для фронтенда
- SQLite - Локальная база данных для разработки
