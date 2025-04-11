# 🐌 Lazy Manager

**Lazy Manager** — это веб-приложение для управления задачами, построенное на **Django**, с REST API, авторизацией через **JWT**, фильтрацией, уведомлениями и расширяемой архитектурой.

---


## 🚀 Возможности

- ✅ Регистрация и вход пользователей
- ✅ CRUD для задач
- ✅ Разделение задач на активные и завершённые
- ✅ Создание разных таблиц под задачи (в разработке)
- ✅ Возможность добавлять пользователей в друзья (в разработке)
- ✅ Ведение совместных таблиц с друзьями (в разработке)
- ✅ Фильтрация и поиск по задачам
- ✅ REST API с JWT авторизацией
- ✅ Swagger-документация
- ✅ PostgreSQL база данных
- 🔄 Поддержка Celery (в разработке)
- 📦 Docker-окружение (в разработке)

---

## 🛠️ Стек технологий

- Python 3.12
- Django 5
- Django REST Framework
- PostgreSQL
- JWT Authentication (SimpleJWT)
- drf-spectacular (Swagger Docs)
- Docker (планируется)
- Celery + Redis (планируется)

---

## 📦 Установка

1. Клонируй репозиторий:

``` bash
git clone https://github.com/yngqual1ty/TaskManager.git
cd TaskManager
```

2. Установи зависимости:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
3. Настрой базу данных (PostgreSQL) и файл .env:
``` bash
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=manager_db
DB_USER=lazym
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```
4. Выполни миграции и запусти сервер
``` bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

🔑 API и документация

Swagger: /swagger/

ReDoc: /redoc/

Получение токена: POST /api/token/

Обновление токена: POST /api/token/refresh/

Регистрация: POST /api/users/register/


👨‍💻 Автор
yngqual1ty
