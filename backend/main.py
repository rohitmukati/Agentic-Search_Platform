from backend.database import Base, engine
from backend.models import User, Lead, SearchLog
from backend.routes import auth
from fastapi import FastAPI


app = FastAPI()

Base.metadata.create_all(bind=engine)

# Middleware for CORS
@app.get("/api/health")
def health_check():
    return {"status": "ok"}


# Routers

app.include_router(auth.router, prefix="/api/auth")
# app.include_router(leads.router, prefix="/api/leads")

