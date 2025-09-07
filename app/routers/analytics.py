# File: app/routers/analytics.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional

from .. import crud, models
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter(prefix="/analytics", tags=["Analytics"])

@router.get("/spending-summary")
async def get_spending_summary(
    month: int, year: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    summary_data = crud.get_spending_summary_data(db, user_id=current_user.id, month=month, year=year)
    total_amount = crud.get_total_spending(db, user_id=current_user.id, month=month, year=year)
    
    summary = []
    for category, amount in summary_data:
        percentage = (amount / total_amount * 100) if total_amount > 0 else 0
        summary.append({
            "category": category,
            "total_amount": amount,
            "percentage": round(percentage, 2)
        })
        
    return {
        "summary": summary,
        "total_amount": total_amount,
        "month": month,
        "year": year
    }