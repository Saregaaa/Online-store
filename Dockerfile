# Используем официальный образ Python версии 3.11 на базе slim
FROM python:3.11

# Устанавливаем переменные среды для работы с Python
ENV PYTHONDONTWRITEBYTECODE 1  
ENV PYTHONUNBUFFERED 1          

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем все зависимости, указанные в requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в рабочую директорию контейнера
COPY . /app/
