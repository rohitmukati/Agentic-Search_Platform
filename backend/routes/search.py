from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.schemas import SearchInput, LeadCreate, Lead
from backend.models import Lead as LeadModel, SearchLog as SearchLogModel
from backend.services.utils import get_current_user
from backend.services.agent_controller import run_agents
from backend.services.email_validator import validate_email
from typing import List

router = APIRouter()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# POST /api/search/run
@router.post("/run", response_model=List[Lead])
def run_search(
    search_input: SearchInput,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    try:
        # ✅ Step 0: Log the search input directly (no join/split needed)
        services_str = (
            ",".join(search_input.services) if isinstance(search_input.services, list)
            else search_input.services
        )
        countries_str = search_input.countries  # already a string now

        search_log = SearchLogModel(
            user_id=current_user.id,
            keywords=search_input.keywords,
            industry=search_input.industry,
            countries=countries_str,     # ✅ Store directly
            services=services_str,
        )
        db.add(search_log)
        db.commit()

        # Step 1: Run all agents with search input
        raw_leads = run_agents(search_input)

        created_leads = []

        # Step 2: Loop through raw leads and normalize + validate
        for raw in raw_leads:
            email_status = validate_email(raw.get("email", ""))
            lead_data = LeadCreate(
                company=raw.get("company", "Unknown"),
                contact=raw.get("contact", ""),
                email=raw.get("email"),
                title=raw.get("title", ""),
                country=raw.get("country", ""),
                services=services_str,
                status=email_status,
                source=raw.get("source", "Google"),
            )

            # Step 3: Save to DB
            lead_model = LeadModel(
                user_id=current_user.id,
                **lead_data.dict()
            )
            db.add(lead_model)
            db.commit()
            db.refresh(lead_model)
            created_leads.append(lead_model)

        return created_leads

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
