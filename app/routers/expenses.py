# File: app/routers/expenses.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import crud, models, schemas
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/", response_model=schemas.ExpenseResponse)
async def create_new_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.create_expense(db=db, expense=expense, user_id=current_user.id)

@router.get("/", response_model=List[schemas.ExpenseResponse])
async def read_expenses(
    skip: int = 0, limit: int = 100, category: Optional[str] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_expenses(db, user_id=current_user.id, skip=skip, limit=limit, category=category)

@router.delete("/{expense_id}")
async def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    success = crud.delete_expense(db, expense_id=expense_id, user_id=current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}