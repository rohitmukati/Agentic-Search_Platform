from pydantic import BaseModel, EmailStr, field_serializer

from datetime import datetime
from uuid import UUID
from typing import Optional, List

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
    user_id: UUID  # Keep UUID type for internal logic

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
        return str(user_id)  # Convert UUID to string in response

    class Config:
        from_attributes = True

# -----------------------------
# Search Log Schemas
# -----------------------------
class SearchLogCreate(BaseModel):
    keywords: Optional[str]
    industry: Optional[str]
    countries: Optional[List[str]]
    services: Optional[str]


class SearchLogOut(SearchLogCreate):
    id: int
    user_id: UUID
    timestamp: datetime

    @field_serializer("user_id")
    def serialize_user_id(self, user_id: UUID) -> str:
        return str(user_id)  # Ensure UUID is returned as string

    class Config:
        from_attributes = True
