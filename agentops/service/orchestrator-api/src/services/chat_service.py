from repository.chat_repository import ChatRepository
import uuid
from datetime import datetime
from models.models import Chat
from typing import Optional

class ChatService: 
    def __init__(self, repo: ChatRepository):
        self.repo = repo

    def create_chat(self, prompt: str):
        chat_id = f"id_{uuid.uuid4()}"
        text = (prompt or "").strip()
        now = datetime.utcnow()
        chat = Chat(id=chat_id, created_at=now, updated_at=now, messages=[text])
        return self.repo.create_chat_repo(chat, chat_id)

    def get_chats(self, chat_id: Optional[str] = None):
        if chat_id:
            return self.repo.get_chats_repo(chat_id)
        return self.repo.get_chats_repo()

    def update_chat(self, chat_id: str, chat: Chat):
        self.repo.store[chat_id] = chat
        return chat

    def delete_chat(self, chat_id: str) -> bool:
        return self.repo.delete_chat_repo(chat_id)