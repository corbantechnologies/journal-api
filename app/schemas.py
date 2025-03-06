from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserResponse(UserCreate):
    id: str
    email: EmailStr

    class Config:
        from_attributes = True


"""
JWT Authentication
"""


class Token(BaseModel):
    access_token: str


class TokenData(BaseModel):
    email: Optional[str] = None


"""
Journal
"""


class JournalEntry(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    mood: Optional[str] = None


class JournalEntryResponse(JournalEntry):
    id: str
    user_id: str
    title: str
    content: str
    mood: str
    created_at: datetime

    class Config:
        from_attributes = True


"""
Search Schema
"""


class SearchQuery(BaseModel):
    query: str


"""
Export data schema
"""


class ExportData(BaseModel):
    format: str
