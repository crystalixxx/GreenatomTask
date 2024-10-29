from datetime import datetime

from pydantic import EmailStr
from sqlalchemy import (
    Integer,
    Column,
    String,
    ForeignKey,
    DateTime,
    func,
    Text,
    Boolean,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    username: str = Column(String, nullable=False, unique=True)
    email: EmailStr = Column(String, nullable=False)
    is_blocked: bool = Column(Boolean, nullable=False, default=False)


class Chat(Base):
    __tablename__ = "chat"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String, nullable=False)
    created_at: datetime = Column(DateTime(timezone=True), server_default=func.now())


class Message(Base):
    __tablename__ = "message"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    sender_id: int = Column(Integer, ForeignKey("user.id"), nullable=False)
    chat_id: int = Column(Integer, ForeignKey("chat.id"), nullable=False)
    content: str = Column(Text, nullable=False)
    sent_at: datetime = Column(DateTime(timezone=True), server_default=func.now())
    is_read: bool = Column(Boolean, nullable=False, default=False)


class ChatMember(Base):
    __tablename__ = "chat_member"

    chat_id: int = Column(
        Integer, ForeignKey("chat.id"), nullable=False, primary_key=True
    )
    member_id: int = Column(
        Integer, ForeignKey("user.id"), nullable=False, primary_key=True
    )