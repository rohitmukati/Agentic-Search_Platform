# leads.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend import models, schemas
from backend.database import SessionLocal
from backend.services.utils import get_current_user  # Ye authentication ke liye
from typing import List

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a lead
@router.post("/", response_model=schemas.Lead)
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    db_lead = models.Lead(
        user_id=current_user.id,
        company=lead.company,
        contact=lead.contact,
        email=lead.email,
        title=lead.title,
        country=lead.country,
        services=lead.services,
        status=lead.status,
        source=lead.source
    )
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

# Get all leads
@router.get("/", response_model=List[schemas.Lead])
def get_leads(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    leads = db.query(models.Lead).filter(models.Lead.user_id == current_user.id).all()
    return leads

# Get a specific lead by ID
@router.get("/{lead_id}", response_model=schemas.Lead)
def get_lead(lead_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id, models.Lead.user_id == current_user.id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead

# Update a lead
@router.put("/{lead_id}", response_model=schemas.Lead)
def update_lead(lead_id: int, updated_lead: schemas.LeadCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id, models.Lead.user_id == current_user.id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    for key, value in updated_lead.dict(exclude_unset=True).items():
        setattr(lead, key, value)

    db.commit()
    db.refresh(lead)
    return lead

# Delete a lead
@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(lead_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id, models.Lead.user_id == current_user.id).first()
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    db.delete(lead)
    db.commit()
    return
