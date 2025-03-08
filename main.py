import os
import logging
from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings

# Configuration using Pydantic Settings
class Settings(BaseSettings):
    app_name: str = "FastAPI"
    environment: str = os.getenv("ENVIRONMENT", "development")

    class Config:
        env_file = ".env"

settings = Settings()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)

@app.get("/")
async def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello World!"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
