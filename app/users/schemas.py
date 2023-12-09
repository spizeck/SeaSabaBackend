from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class UserProfile(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    company_name: str
    
class UserPreferences(BaseModel):
    pass

class UpdateUser(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    company_name: Optional[str] = None

class User(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool
    profile: Optional[UserProfile] = None
    preferences: Optional[UserPreferences] = None

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    username: str