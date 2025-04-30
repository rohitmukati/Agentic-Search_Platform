# backend/routes/leads.py

from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List, Optional
from sqlalchemy.orm import Session
from backend import models, schemas
from backend.database import SessionLocal
from backend.services.utils import get_current_user
import csv
from fastapi.responses import StreamingResponse
from io import StringIO

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------
# CSV Export of Filtered Leads
# ----------------------------
@router.get("/export")
def export_leads_csv(
    country: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    query = db.query(models.Lead).filter(models.Lead.user_id == current_user.id)

    if country:
        query = query.filter(models.Lead.country.ilike(f"%{country}%"))
    if status:
        query = query.filter(models.Lead.status.ilike(f"%{status}%"))
    if company:
        query = query.filter(models.Lead.company.ilike(f"%{company}%"))

    leads = query.all()

    # CSV content create karo
    csv_file = StringIO()
    csv_writer = csv.writer(csv_file)
    
    # Write headers
    csv_writer.writerow(["ID", "Company", "Contact", "Email", "Title", "Country", "Services", "Status", "Source", "Created At"])
    
    # Write data rows
    for lead in leads:
        csv_writer.writerow([
            lead.id, lead.company, lead.contact, lead.email,
            lead.title, lead.country, lead.services, lead.status,
            lead.source, lead.created_at.strftime("%Y-%m-%d %H:%M:%S")
        ])

    csv_file.seek(0)
    return StreamingResponse(csv_file, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=leads_export.csv"
    })

# ----------------------------------------
# Create a new Lead
# ----------------------------------------
@router.post("/", response_model=schemas.Lead)
def create_lead(
    lead: schemas.LeadCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
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

# ----------------------------------------
# Get All Leads (with optional filters)
# ----------------------------------------
@router.get("/", response_model=List[schemas.Lead])
def get_leads(
    country: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    query = db.query(models.Lead).filter(models.Lead.user_id == current_user.id)

    if country:
        query = query.filter(models.Lead.country.ilike(f"%{country}%"))

    if status:
        query = query.filter(models.Lead.status.ilike(f"%{status}%"))

    if company:
        query = query.filter(models.Lead.company.ilike(f"%{company}%"))

    leads = query.all()
    return leads

# ----------------------------------------
# Get a Specific Lead by ID
# ----------------------------------------
@router.get("/{lead_id}", response_model=schemas.Lead)
def get_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    lead = db.query(models.Lead).filter(
        models.Lead.id == lead_id,
        models.Lead.user_id == current_user.id
    ).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    return lead

# ----------------------------------------
# Update a Lead
# ----------------------------------------
@router.put("/{lead_id}", response_model=schemas.Lead)
def update_lead(
    lead_id: int,
    updated_lead: schemas.LeadCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    lead = db.query(models.Lead).filter(
        models.Lead.id == lead_id,
        models.Lead.user_id == current_user.id
    ).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    for key, value in updated_lead.dict(exclude_unset=True).items():
        setattr(lead, key, value)

    db.commit()
    db.refresh(lead)
    return lead

# ----------------------------------------
# Delete a Lead
# ----------------------------------------
@router.delete("/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    lead = db.query(models.Lead).filter(
        models.Lead.id == lead_id,
        models.Lead.user_id == current_user.id
    ).first()

    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")

    db.delete(lead)
    db.commit()
    return 