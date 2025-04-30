from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models, schemas
from backend.services.utils import get_current_user
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Add new search log
@router.post("/", response_model=schemas.SearchLogOut)
def create_search_log(
    log: schemas.SearchLogCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_log = models.SearchLog(
        user_id=current_user.id,
        keywords=log.keywords,
        industry=log.industry,
        countries=log.countries,
        services=log.services
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# ✅ View all logs (by current user)
@router.get("/", response_model=List[schemas.SearchLogOut])
def get_logs(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.SearchLog).filter(models.SearchLog.user_id == current_user.id).all()
