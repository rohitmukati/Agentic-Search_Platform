from pydantic import BaseModel, EmailStr, field_serializer
from datetime import datetime
from uuid import UUID
from typing import Optional, List, Union

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
    countries: Optional[List[str]] = None
    services: Optional[str] = None


class SearchLogOut(BaseModel):
    id: int
    user_id: UUID
    keywords: Optional[str]
    industry: Optional[str]
    countries: Optional[Union[List[str], str]] = None
    services: Optional[Union[str, List[str]]] = None
    timestamp: datetime

    @field_serializer("user_id")
    def serialize_user_id(self, user_id: UUID) -> str:
        return str(user_id)

    @field_serializer("countries")
    def serialize_countries(self, countries) -> Union[str, List[str]]:
        if isinstance(countries, list):
            # Convert list of countries to a comma-separated string
            return ", ".join(countries)
        elif isinstance(countries, str):
            # If it's already a string, return as is
            return countries
        return []  # Default to empty list if countries is None

    @field_serializer("services")
    def serialize_services(self, services) -> Union[str, List[str]]:
        if isinstance(services, str) and "," in services:
            return [s.strip() for s in services.split(",")]
        return services

    class Config:
        from_attributes = True


# -----------------------------
# Search Input Schema for AI Agents
# -----------------------------
class SearchInput(BaseModel):
    keywords: str
    industry: str
    countries: List[str]
    services: Union[str, List[str]]

    @field_serializer("countries")
    def serialize_input_countries(self, countries) -> List[str]:
        if isinstance(countries, str):
            # If it's a single string, split into list
            return [country.strip() for country in countries.split(",")]
        return countries


