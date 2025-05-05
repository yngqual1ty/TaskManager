# 1. Базовый образ
FROM python:3.12-slim

# 2. Переменные окружения
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 3. Системные зависимости
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      netcat-openbsd \
      gcc \
      postgresql-client \
      libpq-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# 4. Рабочая директория
WORKDIR /app

# 5. Копируем и устанавливаем Python-зависимости
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt



# 6. Копируем остальной код
COPY . .

# 7. Скрипт ожидания сервисов
COPY wait-for.sh /wait-for.sh
RUN chmod +x /wait-for.sh


CMD ["/wait-for.sh", "db:5432", "gunicorn", "LazyManager.wsgi:application", "--bind", "0.0.0.0:8000"]
