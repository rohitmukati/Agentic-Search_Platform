from pydantic import BaseModel, EmailStr

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
