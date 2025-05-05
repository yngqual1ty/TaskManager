# 🐌 Lazy Manager

**Lazy Manager** — это веб-приложение для управления задачами, построенное на **Django**, с удобным веб-интерфейсом и мощным REST API. Проект включает авторизацию через **JWT**, фильтрацию задач, фоновые задачи через **Celery**, автогенерируемую документацию и поддержку контейнеризации с **Docker**.

---

## 🚀 Возможности

- ✅ Регистрация и вход пользователей
- ✅ CRUD для задач
- ✅ Разделение задач на активные и завершённые
- ✅ Фильтрация и поиск по задачам
- ✅ REST API с JWT авторизацией
- ✅ Swagger-документация
- ✅ PostgreSQL база данных
- ✅ Celery + Redis: автоматическая пометка просроченных задач
- ✅ Docker-окружение
- 🚧 Создание разных таблиц под задачи (в разработке)
- 🚧 Добавление пользователей в друзья (в разработке)
- 🚧 Совместная работа над задачами (в разработке)

---

## 🛠️ Стек технологий

- Python 3.12
- Django 5
- Django REST Framework
- PostgreSQL
- Redis + Celery
- JWT (SimpleJWT)
- drf-spectacular (Swagger / ReDoc)
- Docker, Docker Compose

---

## ⚙️ Установка (без Docker)

1. **Клонируй репозиторий:**

```bash
git clone https://github.com/yngqual1ty/TaskManager.git
cd TaskManager
````

2. Создай и активируй виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Установи зависимости
```bash
pip install -r requirements.txt
```
`
4. Создай .env на основе шаблона и заполни:
``` bash
cp .env.example .env
```

Пример .env:
```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

POSTGRES_DB=manager_db
POSTGRES_USER=lazym
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_HOST=localhost
REDIS_PORT=6379
```
5. Построй и подними контейнеры:
```bash
docker-compose up --build
```

6. Применить миграции и собрать статику:
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py collectstatic --noinput
```

7. (Доп) Создай суперюзера
```bash
docker-compose exec web python manage.py createsuperuser
```

🔑 API и документация

Swagger: /swagger/

ReDoc: /redoc/

Получение токена: POST /api/token/

Обновление токена: POST /api/token/refresh/

Регистрация: POST /api/users/register/


👨‍💻 Автор - yngqual1ty

GitHub: yngqual1ty