from repository.chat_repository import ChatRepository
import uuid, json
from datetime import datetime
from models.models import Chat
from typing import Optional
from models.chat_model import ChatModel

class ChatService: 
    def __init__(self, repo: ChatRepository):
        self.repo = repo

    def create_chat(self, prompt: str):
        chat_id = f"id_{uuid.uuid4()}"
        text = (prompt or "").strip()
        chat = ChatModel(
            id=chat_id,
            summary="",                     
            messages=[text],    
            created_at=datetime.utcnow(),    
            updated_at=datetime.utcnow(),   
        )
        return self.repo.create_chat_repo(chat)

    def get_chats(self, chat_id: Optional[str] = None):
        if chat_id:
            return self.repo.get_chats_repo(chat_id)
        return self.repo.get_chats_repo()

    def update_chat(self, chat_id: str, new_message: str):
        existing = self.repo.get_chats_repo(chat_id)
        if not existing:
            return None
        existing.messages.append(new_message)
        existing.updated_at = datetime.utcnow()
        return self.repo.update_chat_repo(existing)

    def delete_chat(self, chat_id: str) -> bool:
        return self.repo.delete_chat_repo(chat_id)