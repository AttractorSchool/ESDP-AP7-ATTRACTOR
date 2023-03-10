FROM python:3.10

# установка зависимостей
RUN apt-get update && apt-get install -y postgresql-client
COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

# копирование проекта в образ
COPY . /app
WORKDIR /app

# экспортируем порт 8000, который будет слушать gunicorn

# команда запуска gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi"]