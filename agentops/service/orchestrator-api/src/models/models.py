from typing import Optional
from pydantic import BaseModel
from datetime import datetime

# Only field the UI sends when creating a chat; everything else is backend-managed
class CreateChatBody(BaseModel):
    text: str = ""

# Internal shape for a stored chat (id, timestamps set by backend)
class Chat(BaseModel):
    id: str = ""
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    "prompt : CreateChatBody = {}"
    messages: list[str] = []

class UpdateChatBody(BaseModel):
    updated_at: Optional[datetime] = None
    messages: list[str] = []
