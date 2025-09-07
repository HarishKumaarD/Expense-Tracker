# File: app/routers/budgets.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import crud, models, schemas
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter(prefix="/budgets", tags=["Budgets"])

@router.post("/", response_model=schemas.BudgetResponse)
async def create_new_budget(
    budget: schemas.BudgetCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_budget = crud.create_budget(db, budget=budget, user_id=current_user.id)
    if db_budget is None:
        raise HTTPException(status_code=400, detail="Budget already exists for this category and month")
    return db_budget

@router.get("/", response_model=List[schemas.BudgetResponse])
async def read_budgets(
    month: Optional[int] = None, year: Optional[int] = None,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return crud.get_budgets(db, user_id=current_user.id, month=month, year=year)