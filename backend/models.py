from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID, ARRAY
import uuid
from datetime import datetime
from backend.database import Base

class User(Base):
    __tablename__ = "users"  # Lowercase table name

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class Lead(Base):
    __tablename__ = "leads"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))  # Corrected table name
    company = Column(String)
    contact = Column(String)
    email = Column(String)
    title = Column(String)
    country = Column(String)
    services = Column(Text)
    status = Column(String)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class SearchLog(Base):
    __tablename__ = "search_logs"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"))
    keywords = Column(String)
    industry = Column(String)
    countries = Column(ARRAY(String))
    services = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Optional: Define any configurations here if required in future
    class Config:
        orm_mode = True
