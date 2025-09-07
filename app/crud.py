# File: app/crud.py
from sqlalchemy.orm import Session
from sqlalchemy import extract, func
from . import models, schemas, security

# User CRUD
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(email=user.email, full_name=user.full_name, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Expense CRUD
def create_expense(db: Session, expense: schemas.ExpenseCreate, user_id: int):
    db_expense = models.Expense(**expense.dict(), user_id=user_id)
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense

def get_expenses(db: Session, user_id: int, skip: int = 0, limit: int = 100, category: str = None):
    query = db.query(models.Expense).filter(models.Expense.user_id == user_id)
    if category:
        query = query.filter(models.Expense.category == category)
    return query.offset(skip).limit(limit).all()

def delete_expense(db: Session, expense_id: int, user_id: int):
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id, models.Expense.user_id == user_id).first()
    if expense:
        db.delete(expense)
        db.commit()
        return True
    return False

# Budget CRUD
def create_budget(db: Session, budget: schemas.BudgetCreate, user_id: int):
    existing = db.query(models.Budget).filter_by(
        user_id=user_id, category=budget.category, month=budget.month, year=budget.year
    ).first()
    if existing:
        return None # Indicate that it already exists
    
    db_budget = models.Budget(**budget.dict(), user_id=user_id)
    db.add(db_budget)
    db.commit()
    db.refresh(db_budget)
    return db_budget

def get_budgets(db: Session, user_id: int, month: int = None, year: int = None):
    query = db.query(models.Budget).filter(models.Budget.user_id == user_id)
    if month:
        query = query.filter(models.Budget.month == month)
    if year:
        query = query.filter(models.Budget.year == year)
    return query.all()

# Analytics
def get_spending_summary_data(db: Session, user_id: int, month: int, year: int):
    query = db.query(
        models.Expense.category,
        func.sum(models.Expense.amount).label("total_amount")
    ).filter(
        models.Expense.user_id == user_id,
        extract('month', models.Expense.date) == month,
        extract('year', models.Expense.date) == year
    ).group_by(models.Expense.category)
    
    return query.all()

def get_total_spending(db: Session, user_id: int, month: int, year: int):
    total = db.query(func.sum(models.Expense.amount)).filter(
        models.Expense.user_id == user_id,
        extract('month', models.Expense.date) == month,
        extract('year', models.Expense.date) == year
    ).scalar()
    return total or 0.0