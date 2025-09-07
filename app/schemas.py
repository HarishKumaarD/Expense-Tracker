# File: app/schemas.py
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List
from enum import Enum

# Enums
class ExpenseCategory(str, Enum):
    FOOD = "food"
    TRANSPORT = "transport"
    ENTERTAINMENT = "entertainment"
    SHOPPING = "shopping"
    BILLS = "bills"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    OTHER = "other"

# Base Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str

class ExpenseBase(BaseModel):
    title: str
    amount: float
    category: ExpenseCategory
    description: Optional[str] = ""
    date: Optional[datetime] = None

class BudgetBase(BaseModel):
    category: ExpenseCategory
    limit_amount: float
    month: int
    year: int

# Create Models
class UserCreate(UserBase):
    password: str

class ExpenseCreate(ExpenseBase):
    pass

class BudgetCreate(BudgetBase):
    pass

# Response Models
class UserResponse(UserBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class ExpenseResponse(ExpenseBase):
    id: int
    date: datetime
    class Config:
        from_attributes = True

class BudgetResponse(BudgetBase):
    id: int
    class Config:
        from_attributes = True

# Token Models
class Token(BaseModel):
    access_token: str
    token_type: str

# Analytics Models
class SpendingSummary(BaseModel):
    category: str
    total_amount: float
    percentage: float