from fastapi import FastAPI
from routes import auth, leads, search

app = FastAPI()

# Attach route groups (modular)
app.include_router(auth.router, prefix="/api/auth")
app.include_router(leads.router, prefix="/api/leads")
app.include_router(search.router, prefix="/api/search")

# Basic health check route
@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Backend is running perfectly"}
