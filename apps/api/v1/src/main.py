from fastapi import FastAPI
from src.core.config import settings
from src.controllers.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="CrashX API for Flutter Crash Analytics",
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
def read_root():
    return {"message": "Welcome to CrashX API", "docs_url": "/docs"}

