from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from backend.database import Base, engine

from backend.routes import auth, leads, search_logs, search
from backend.routes import admin

# Importing the models to create the tables in the database
app = FastAPI()

Base.metadata.create_all(bind=engine)

# Health check
@app.get("/api/health")
def health_check():
    return {"status": "ok"}

# CORS Middleware — allow only Streamlit default origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routers
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(leads.router, prefix="/api/leads", tags=["Leads"])
app.include_router(search_logs.router, prefix="/api/searchlogs", tags=["Search Logs"])
app.include_router(search.router, prefix="/api/search", tags=["Search"])
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])


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

## To run:
# uvicorn backend.main:app --reload
