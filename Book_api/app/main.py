from fastapi import FastAPI
from app.api.v1.routes import books
import logging
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/app.log"),
        logging.StreamHandler()
    ]
)

# Create FastAPI application
app = FastAPI(
    title="Book API",
    description="A RESTful API for managing books",
    version="1.0.0"
)

# Include routers
app.include_router(books.router, prefix="/books", tags=["books"])
