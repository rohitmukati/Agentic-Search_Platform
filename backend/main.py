from backend.database import Base, engine
from backend.models import User, Lead, SearchLog
from backend.routes import auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import leads



app = FastAPI()

Base.metadata.create_all(bind=engine)

# Middleware for CORS
@app.get("/api/health")
def health_check():
    return {"status": "ok"}


# Routers

app.include_router(auth.router, prefix="/api/auth")
# app.include_router(leads.router, prefix="/api/leads")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include leads router
app.include_router(leads.router, prefix="/api/leads", tags=["Leads"])


