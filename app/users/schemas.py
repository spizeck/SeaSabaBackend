from pydantic import BaseModel, EmailStr

# Schema for user creation
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Schema for user display
class User(BaseModel):
    id: int
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
