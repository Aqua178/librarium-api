from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from app.db.base import Base

# Создаем engine для PostgreSQL
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,  # Проверка соединения перед использованием
    pool_size=5,         # Размер пула соединений
    max_overflow=10      # Максимальное количество дополнительных соединений
)

# Создаем фабрику сессий
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Функция для создания таблиц
def create_tables():
    Base.metadata.create_all(bind=engine)


# Dependency для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
