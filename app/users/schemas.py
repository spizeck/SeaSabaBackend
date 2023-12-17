from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None

    @field_validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'Username must be alphanumeric'
        return v

    @field_validator('email')
    def email_format(cls, v):
        assert '@' in v, 'Email must be a valid email address'
        return v


class UserProfileBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone_number: Optional[str] = None
    company_name: Optional[str] = None


class UserPreferencesBase(BaseModel):
    pass


class UserCreate(UserBase):
    username: str
    email: EmailStr
    password: str
    profile: Optional[UserProfileBase] = None
    preferences: Optional[UserPreferencesBase] = None


class UpdateUser(UserBase):
    password: Optional[str] = None


class UpdateUserStatus(BaseModel):
    is_active: Optional[bool] = None
    is_admin: Optional[bool] = None


class ReturnUser(UserBase):
    id: int
    is_active: bool
    is_admin: bool
    profile: Optional[UserProfileBase] = None
    preferences: Optional[UserPreferencesBase] = None

    class Config:
        from_attributes = True


class TokenData(BaseModel):
    username: str
    exp: datetime
    token_type: str
    access_token: str
