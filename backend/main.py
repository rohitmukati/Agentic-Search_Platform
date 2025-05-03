from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from backend.database import Base, engine
from backend.models import User, Lead, SearchLog
from backend.routes import search_logs
from backend.routes import search

from backend.routes import auth

from backend.routes import leads


# Importing the models to create the tables in the database
app = FastAPI()

Base.metadata.create_all(bind=engine)

# Health check
@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(leads.router, prefix="/api/leads", tags=["Leads"])
app.include_router(search_logs.router, prefix="/api/searchlogs", tags=["Search Logs"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])



# ✅ Swagger Auth: Add Bearer token support in Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Agentic AI Search Platform API",
        version="1.0.0",
        description="API backend for Agentic AI Search Platform with JWT Auth",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"BearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Set custom OpenAPI function
app.openapi = custom_openapi


# uvicorn backend.main:app --reload
