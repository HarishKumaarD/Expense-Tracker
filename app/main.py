# File: app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

from .database import engine
from . import models
from .routers import auth, expenses, budgets, analytics

# Create all database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Expense Tracker API", 
    version="1.0.0",
    description="A comprehensive API for managing personal expenses, budgets, and analytics"
)

# CORS middleware - handle empty ALLOWED_ORIGINS gracefully
ALLOWED_ORIGINS_STR = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000,http://127.0.0.1:3000')
ALLOWED_ORIGINS = [origin.strip() for origin in ALLOWED_ORIGINS_STR.split(',') if origin.strip()]

print(f"CORS allowed origins: {ALLOWED_ORIGINS}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api", tags=["Authentication"])
app.include_router(expenses.router, prefix="/api", tags=["Expenses"])
app.include_router(budgets.router, prefix="/api", tags=["Budgets"])
app.include_router(analytics.router, prefix="/api", tags=["Analytics"])

@app.get("/", tags=["Root"])
def read_root():
    return {
        "message": "Welcome to the Personal Expense Tracker API",
        "version": "1.0.0",
        "environment": os.getenv('ENVIRONMENT', 'development'),
        "docs_url": "/docs"
    }

@app.get("/health", tags=["Health"])
def health_check():
    return {
        "status": "healthy",
        "environment": os.getenv('ENVIRONMENT', 'development')
    }