from fastapi import FastAPI
from app.core.config import settings
from app.api.v1.router import api_router
from app.db.session import create_tables

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Подключаем роутер API v1
app.include_router(api_router, prefix=settings.API_V1_STR)

# Инициализация базы данных при запуске
@app.on_event("startup")
async def startup_event():
    create_tables()

# Health check endpoint
@app.get("/health", tags=["health"])
async def health_check():
    return {
        "status": "ok",
        "app_name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION
    }
