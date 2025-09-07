# File: app/models.py
from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    full_name = Column(String(255))
    hashed_password = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    expenses = relationship("Expense", back_populates="owner")
    budgets = relationship("Budget", back_populates="owner")

class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    amount = Column(Float)
    category = Column(String(50))
    description = Column(Text, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="expenses")

class Budget(Base):
    __tablename__ = "budgets"
    
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(50))
    limit_amount = Column(Float)
    month = Column(Integer)  # 1-12
    year = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    owner = relationship("User", back_populates="budgets")