from typing import Optional
from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Only field the UI sends when creating a chat; everything else is backend-managed
class CreateChatBody(BaseModel):
    text: str = ""

class Chat(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str = ""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    summary: str = ""
    messages: list[str] = []

class UpdateChatBody(BaseModel):
    updated_at: Optional[datetime] = None
    messages: list[str] = []
