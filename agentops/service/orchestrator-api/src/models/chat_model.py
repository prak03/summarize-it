# models/chat_model.py
from datetime import datetime
from sqlalchemy import String, DateTime, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.mutable import MutableList
from db import Base

class ChatModel(Base):
    __tablename__ = "chats"

    id: Mapped[str] = mapped_column(String, primary_key=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    summary: Mapped[str] = mapped_column(Text, default="")

    messages: Mapped[list[str]] = mapped_column(
        MutableList.as_mutable(JSON),
        default=list
    )