from pydantic import BaseModel, EmailStr, field_serializer
from datetime import datetime
from uuid import UUID
from typing import Optional

# -----------------------------
# User Schemas
# -----------------------------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

# -----------------------------
# Lead Schemas
# -----------------------------
class LeadCreate(BaseModel):
    company: str
    contact: Optional[str] = None
    email: Optional[EmailStr] = None
    title: Optional[str] = None
    country: Optional[str] = None
    services: Optional[str] = None
    status: Optional[str] = "Unknown"
    source: Optional[str] = None

class Lead(BaseModel):
    id: int
    user_id: UUID
    company: str
    contact: Optional[str]
    email: Optional[EmailStr]
    title: Optional[str]
    country: Optional[str]
    services: Optional[str]
    status: Optional[str]
    source: Optional[str]
    created_at: datetime

    @field_serializer("user_id")
    def serialize_user_id(self, user_id: UUID) -> str:
        return str(user_id)

    class Config:
        from_attributes = True

# -----------------------------
# Search Log Schemas
# -----------------------------
class SearchLogCreate(BaseModel):
    keywords: Optional[str]
    industry: Optional[str]
    countries: Optional[str] = None  # single string country
    services: Optional[str] = None

class SearchLogOut(BaseModel):
    id: int
    user_id: UUID
    keywords: Optional[str]
    industry: Optional[str]
    countries: Optional[str] = None  # single string output
    services: Optional[str] = None
    timestamp: datetime

    @field_serializer("user_id")
    def serialize_user_id(self, user_id: UUID) -> str:
        return str(user_id)

    class Config:
        from_attributes = True

# -----------------------------
# Search Input Schema for AI Agents
# -----------------------------
class SearchInput(BaseModel):
    keywords: str
    industry: str
    countries: str  # single string
    services: str
    
# -----------------------------
# User Output Schema
# -----------------------------
class UserOut(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    created_at: datetime

    @field_serializer("id")
    def serialize_id(self, v: UUID) -> str:
        return str(v)

    class Config:
        from_attributes = True

