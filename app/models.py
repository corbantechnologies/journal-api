import uuid
from sqlalchemy import Column, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, index=True)
    name = Column(String, nullable=True, blank=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)


class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=True, blank=True)
    content = Column(Text, nullable=True, blank=True)
    mood = Column(String, nullable=True, blank=True)
    user_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))

    user = relationship("User")
