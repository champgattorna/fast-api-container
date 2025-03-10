import os
import logging
from fastapi import FastAPI, HTTPException

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
