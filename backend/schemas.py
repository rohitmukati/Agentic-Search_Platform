from pydantic import BaseModel, EmailStr, field_serializer
# Lead-related schemas
from typing import Optional
from datetime import datetime
from uuid import UUID

# Input schema for signup
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# Input schema for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Output schema (After successful login - JWT Token)
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"



# Create Lead input schema
class LeadCreate(BaseModel):
    company: str
    contact: Optional[str] = None
    email: Optional[EmailStr] = None
    title: Optional[str] = None
    country: Optional[str] = None
    services: Optional[str] = None
    status: Optional[str] = "Unknown"
    source: Optional[str] = None

# Lead output schema (response model)
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
