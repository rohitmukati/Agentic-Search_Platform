# backend/routes/admin.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend import models, schemas
from backend.services.utils import get_current_user
from collections import Counter
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_admin(user: models.User = Depends(get_current_user)):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")
    return user

@router.get("/dashboard", summary="Overall analytics")
def admin_dashboard(
    db: Session = Depends(get_db),
    admin: models.User = Depends(get_current_admin)
):
    # Fetch overall counts
    users = db.query(models.User).all()
    total_users = len(users)
    total_leads = db.query(models.Lead).count()
    total_searches = db.query(models.SearchLog).count()

    # Top users by search count
    search_counts = Counter([log.user_id for log in db.query(models.SearchLog).all()])
    top_users = []
    for uid, cnt in search_counts.most_common(10):
        user = next((u for u in users if u.id == uid), None)
        if user:
            top_users.append({
                "user_id": str(uid),
                "name": user.name,
                "count": cnt
            })

    # --- Global Top 5 across all users ---
    logs = db.query(models.SearchLog).all()
    industries = [log.industry for log in logs if log.industry]
    countries  = [log.countries for log in logs if log.countries]
    services   = [log.services for log in logs if log.services]

    top_industries = Counter(industries).most_common(5)
    top_countries  = Counter(countries).most_common(5)
    top_services   = Counter(services).most_common(5)

    return {
        "total_users": total_users,
        "total_leads": total_leads,
        "total_searches": total_searches,
        "top_users": top_users,
        "top_industries": top_industries,
        "top_countries": top_countries,
        "top_services": top_services
    }

@router.get("/users", summary="List users sorted by activity")
def list_users(
    db: Session = Depends(get_db),
    admin: models.User = Depends(get_current_admin)
):
    users = db.query(models.User).all()
    users_stats = []
    for u in users:
        searches = db.query(models.SearchLog).filter(models.SearchLog.user_id == u.id).count()
        leads    = db.query(models.Lead).filter(models.Lead.user_id == u.id).count()
        users_stats.append({
            "user_id": str(u.id),
            "name": u.name,
            "searches": searches,
            "leads": leads,
            "is_admin": u.is_admin
        })
    users_stats.sort(key=lambda x: x["searches"], reverse=True)
    return users_stats

@router.get("/users/{user_id}", summary="Per-user analytics")
def get_user_analytics(
    user_id: str,
    db: Session = Depends(get_db),
    admin: models.User = Depends(get_current_admin)
):
    uid = uuid.UUID(user_id)
    user = db.query(models.User).filter(models.User.id == uid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    logs = db.query(models.SearchLog).filter(models.SearchLog.user_id == uid).all()
    leads = db.query(models.Lead).filter(models.Lead.user_id == uid).all()

    industries = [log.industry for log in logs if log.industry]
    countries  = [log.countries for log in logs if log.countries]
    services   = [log.services for log in logs if log.services]

    return {
        "user_id": str(uid),
        "name": user.name,
        "total_searches": len(logs),
        "total_leads": len(leads),
        "top_industries": Counter(industries).most_common(10),
        "top_countries":  Counter(countries).most_common(10),
        "top_services":   Counter(services).most_common(10)
    }

@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete user + data")
def delete_user(
    user_id: str,
    db: Session = Depends(get_db),
    admin: models.User = Depends(get_current_admin)
):
    uid = uuid.UUID(user_id)

    target = db.query(models.User).filter(models.User.id == uid).first()
    if not target:
        raise HTTPException(status_code=404, detail="User not found")
    if target.is_admin:
        raise HTTPException(status_code=403, detail="Cannot delete an admin user")

    db.query(models.Lead).filter(models.Lead.user_id == uid).delete()
    db.query(models.SearchLog).filter(models.SearchLog.user_id == uid).delete()
    db.query(models.User).filter(models.User.id == uid).delete()
    db.commit()
