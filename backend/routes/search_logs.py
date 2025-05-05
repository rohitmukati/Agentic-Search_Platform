from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models, schemas
from backend.services.utils import get_current_user
from typing import List
from collections import Counter

router = APIRouter()

# ✅ DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Create new search log
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
        countries=log.countries,  # ✅ single string now
        services=log.services
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# ✅ Get all search logs for the current user
@router.get("/", response_model=List[schemas.SearchLogOut])
def get_logs(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.SearchLog).filter(models.SearchLog.user_id == current_user.id).all()

# ✅ Get analytics summary of user's search logs
@router.get("/analytics")
def get_search_analytics(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    logs = db.query(models.SearchLog).filter(models.SearchLog.user_id == current_user.id).all()

    if not logs:
        return {
            "total_searches": 0,
            "top_keywords": [],
            "top_industries": [],
            "top_countries": [],
            "top_services": []
        }

    keywords = [log.keywords for log in logs if log.keywords]
    industries = [log.industry for log in logs if log.industry]
    countries = [log.countries for log in logs if log.countries]  # ✅ changed to flat list
    services = [log.services for log in logs if log.services]

    return {
        "total_searches": len(logs),
        "top_keywords": Counter(keywords).most_common(3),
        "top_industries": Counter(industries).most_common(3),
        "top_countries": Counter(countries).most_common(3),
        "top_services": Counter(services).most_common(3)
    }
