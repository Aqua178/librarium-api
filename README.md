# Librarium API

REST API сервис для управления библиотечным каталогом с JWT-аутентификацией.

## Технологии

- Python 3.8+
- FastAPI
- PostgreSQL
- SQLAlchemy + Alembic
- Pydantic
- PyJWT
- Pytest

## Локальная установка

1. Клонируйте репозиторий
```bash
git clone https://github.com/Aqua178/librarium-api.git
cd librarium-api
```

2. Создайте виртуальное окружение и активируйте его
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# или
venv\Scripts\activate  # Windows
```

3. Установите зависимости
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории проекта
```bash
DATABASE_URL=postgresql://user:password@localhost/librarium
SECRET_KEY=your-secret-key
```

5. Создайте базу данных PostgreSQL
```bash
createdb librarium
```

6. Примените миграции
```bash
alembic upgrade head
```

7. Запустите сервер для разработки
```bash
uvicorn app.main:app --reload
```

API будет доступно по адресу: http://localhost:8000

Документация API (Swagger): http://localhost:8000/docs
