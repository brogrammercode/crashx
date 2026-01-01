from typing import Optional
from pydantic import BaseModel, EmailStr
from uuid import UUID

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str
    full_name: Optional[str] = None

class UserUpdate(UserBase):
    password: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None

class UserInDBBase(UserBase):
    id: UUID
    is_active: bool
    full_name: Optional[str] = None

    class Config:
        from_attributes = True

class User(UserInDBBase):
    pass
