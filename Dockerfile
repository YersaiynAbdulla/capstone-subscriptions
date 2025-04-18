# Dockerfile

# Базовый образ с Python
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Установка зависимостей
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Команда запуска
CMD ["gunicorn", "subscription_manager.wsgi:application", "--bind", "0.0.0.0:8000"]

